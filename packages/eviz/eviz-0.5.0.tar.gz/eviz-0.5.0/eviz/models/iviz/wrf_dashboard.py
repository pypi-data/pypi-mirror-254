import panel as pn
import holoviews as hv
import xarray as xr
import param
import hvplot.xarray
import numpy as np

import geoviews as gv

from eviz import lib as du

pn.extension()
hv.extension('bokeh')

from .base_dashboard import BaseDash
import cartopy.crs as ccrs

class WrfDash(BaseDash):
    """ WrfDash is a dashboard for visualizing output from the Weather Research & Forecasting (WRF) model.

    Attributes:
            config (dict): Config class with file and data information.
            params (dict): Input class with Parameters, configured with yaml and/or input data attributes;
                            contains input data.

    """
    def __init__(self, config, params):
        super().__init__(config=config, params=params)
        self.params.param.xy_ylim.precedence = -1
        self.params.param.xy_xlim.precedence = -1

    def convert_to_levs(self, data, zc): 
        """
        Convert vertical coordinate values in wrf data to pressure levels. 

        Parameters:
                data (xr.Dataset): data to assign new coords and get values.
                zc (str): z coordinate label

        Returns:
                data (xr.Dataset): data
        """
        try:
            p_top = data.P_TOP[0] / 1e5
            eta_full = data.ZNW[0]
            eta_mid = data.ZNU[0]
            levf = np.empty(len(eta_full))
            levs = np.empty(len(eta_mid))
        
            i = 0
            for s in eta_full:
                if s > 0:
                    levf[i] = int(p_top + s*(1000 - p_top))
                else:
                    levf[i] = p_top + s * (1000 - p_top)
                i += 1
            i = 0
            for s in eta_mid:
                if s > 0:
                    levs[i] = int(p_top + s*(1000 - p_top))
                else:
                    levs[i] = p_top + s * (1000 - p_top)
                i += 1

            data = data.assign_coords({'bottom_top': levs,
                                       'bottom_top_stag': levf})

            self.params.set_zc_yzplot_limits_sliders(data, zc)

        except Exception as e:
            data = data           
            self.logger.error(f"{e}: Unable to convert bottom_top values to pressure levels.")  

        return data        

    @param.depends('params.file', 'params.field', 'params.z', 'params.t', 'params.apply_operation_button.clicks', watch=True)
    def set_selected_data(self):
        """
        Returns unit converted and dimension selected data. If zc is found in data coords, make index selection.
        If zc not in data coords, make tc index selection. User Parameters t and z define the selection value.
        Define class vars data4d, data3d, and data2d for use by class functions.

        Parameters:
                file (xarray): use cached xarray dataset.
                zc (str): z coordinates string of current data.
                tc (str): t coordinates string of current data.
                z (int): z coordinate selection value.
                t (in): t zoordinate selection value.

        Returns:
                data2d (xarray): 2 dimensional xarray dataset.
        """
        self.get_proj_from_attrs()
        self.set_plot_options(self.params.file)
        self.params.file = self.convert_to_levs(self.params.file, self.params.zc)

        self.data4d = self.params.file[self.params.field]
        yaml_convert = self.unit_conversion_check(self.data4d, self.params.field)
        self.data4d = self.apply_operations_to_data(data=yaml_convert)

        x_stag, y_stag, z_stag = self.get_stagger_fields(self.params.file, self.params.param['field'].objects)
        for f in self.params.param['field'].objects:
            if self.params.field in x_stag:
                stagger = 'X'
            elif self.params.field in y_stag:
                stagger = 'Y'
            elif self.params.field in z_stag:
                stagger = 'Z'
            else:
                stagger = ""

        self.set_stagger_param_values(stagger)

        if self.params.zc in list(self.data4d.dims):
            self.data2d = eval(f"self.data4d.isel({self.params.zc}=self.params.z, {self.params.tc}=self.params.t)")
            self.data3d = eval(f"self.data4d.isel({self.params.tc}=self.params.t)")
            self.all_vars_data_slice = eval(f"self.params.file.isel({self.params.zc}=self.params.z, \
                                        {self.params.tc}=self.params.t)")
            self.params.param['z'].precedence = +1
        elif self.params.zc not in list(self.data4d.dims):
            self.data2d = eval(f"self.data4d.isel({self.params.tc}=self.params.t)")
            self.all_vars_data_slice = eval(f"self.params.file.isel({self.params.tc}=self.params.t)")
            self.data3d = self.data4d #data only has three dimensions 
        else:  #data is just lat/lon
            self.data2d = self.data4d
            self.data3d = self.data4d

        self.params.set_plot_types_on_var_change()

    def set_plot_options(self, data):
        """
        Get all fields that contain at least three dimensions for plotting.

        Parameters:
                data (xr.Dataset): Dataset with fields to plot.

        Sets:
                plot.objects (list): Available plotting fields.
        """
        plotting_dims = []
        xlong_keys = []
        for k in list(data.keys()):
            if len(list(data[k].dims)) >= 3:
                plotting_dims.append(k)
        plotting_dims.sort()

        self.params.param.field.objects = plotting_dims

    def get_proj_from_attrs(self):
        """
        Get projection information from the datasets metadata.

        Sets:
                proj (str): The current projection value to apply to data.
        """
        if 'projection' in self.params.file.attrs:
            proj = str(self.params.file.attrs['projection']).title().strip().replace(" ","")
        elif 'MAP_PROJ_CHAR' in self.params.file.attrs:
            proj = str(self.params.file.attrs['MAP_PROJ_CHAR']).title().strip().replace(" ","")
        elif 'MAP_PROJECTION' in self.params.file.attrs:
            proj = str(self.params.file.attrs['MAP_PROJECTION']).title().strip().replace(" ","")
        else:
            proj = self.params.proj

    def get_stagger_fields(self, data, plotting_fields):
        """
        Get all fields from the data that contain a stagger value.

        Parameters:
                data (xr.Dataset): Dataset to get z values from.
                plotting_fields (list): All plottable fields.

        Returns:
                x_stag (list): all fields that contain x stagger.
                y_stag (list): all fields that contain y stagger.
                z_stag (list): all fields that contain z stagger.
        """
        y_stag = []
        x_stag = []
        z_stag = []

        for i in plotting_fields:
            if hasattr(data[i], 'stagger'):
                if data[i].attrs['stagger'] == 'Y':
                    y_stag.append(i)
                elif data[i].attrs['stagger'] == 'X':
                    x_stag.append(i)
                elif data[i].attrs['stagger'] == 'Z':
                    z_stag.append(i)
                
        return x_stag, y_stag, z_stag

    def set_z_bounds(self, data, zc):
        """
        Set the bounds of the z coordinate slider for selection of data.

        Parameters:
                data (xr.Dataset): Dataset to get z values from.
                zc (str): The z coordinate label.

        Sets:
                z.bounds (tuple): Number of values for z.
                gif_dim (list): Adds to available dimensions for gifs.
        """
        d = data[self.params.field]
        z_length = len(d[zc].values)
        if z_length != 1:
            end_z = z_length - 1 
            z_bounds = (0,end_z)
            self.params.param['z'].bounds = z_bounds
            self.params.gif_dim.options.append(zc)

    def set_stagger_param_values(self, stagger):
        """
        Sets xc, yc, and zc coordinate labels if the plotting field is a staggered field.

        Parameters:
                stagger (str): The identified stagger value in the field.

        Sets:
                xc (str): x coordinate label.
                yc (str): y coordinate label.
                zc (str): z coordinate label.
        """
        soil_layer_fields = ['RAINNCV_SEPA', 'RAINNC_SEPA']
        soil_layer_stag_fields = ['ZS', 'DZS', 'TSLB', 'SMOIS', 'SH2O']

        tc = 'Time'

        if stagger == "":
            xc = 'west_east'
            yc = 'south_north'
            zc = 'bottom_top'
        elif stagger == 'X':
            xc = 'west_east_stag'
            yc = 'south_north'
            zc = 'bottom_top'
        elif stagger == 'Y':
            xc = 'west_east'
            yc = 'south_north_stag'
            zc = 'bottom_top'
        elif stagger == 'Z': 
            xc = 'west_east'
            yc = 'south_north'
            zc = 'bottom_top_stag'
        if self.params.field in soil_layer_fields:
            xc = 'west_east'
            yc = 'south_north'
            zc = 'soil_layers'
            self.set_z_bounds(self.params.file, zc)
        elif self.params.field in soil_layer_stag_fields:
            xc = 'west_east'
            yc = 'south_north'
            zc = 'soil_layers_stag'
            self.set_z_bounds(self.params.file, zc)

        self.params.tc = tc
        self.params.xc = xc
        self.params.yc = yc
        self.params.zc = zc

    @param.depends('params.proj', 'params.xy_xlim.value', 'params.xy_ylim.value', 'params.enable_projection.clicks',
                   'params.invert_yaxis', 'params.invert_xaxis', 'params.show_grid', 'params.cartopy_feature_scale')
    def create_overlay(self, plot):
        """
        Returns an overlay of provided plot with any selected geoviews/Cartopy features.

                Features:
                        coast (gv): Global coastlines and country borders.
                        lakes (gv): Global lakes.
                        rivers (gv): Global rivers.
                        states (gv): United States borders.
                        grid (gv): Grid lines

                Parameters:
                        plot (plot): Input xy plot to be overlayed with selected features.

                Returns:
                        overlay (overlay): xy overlay with selected features.
        """
        features = [self.params.show_coastlines, self.params.show_states, self.params.show_lakes, self.params.show_rivers, 
                    self.params.show_grid]
        if plot is not None:
            if any(features):
                if self.params.show_coastlines:
                    coast = gv.feature.coastline(scale=self.params.cartopy_feature_scale, 
                                                projection=ccrs.PlateCarree()) 
                    border = gv.feature.borders(scale=self.params.cartopy_feature_scale,
                                                projection=ccrs.PlateCarree()) 
                    coast = coast * border 
                else:
                    coast = None
                lakes = gv.feature.lakes(scale=self.params.cartopy_feature_scale).opts(
                                        fill_color='#2251dd', projection=ccrs.PlateCarree()
                                        ) if self.params.show_lakes else None
                rivers = gv.feature.rivers(scale=self.params.cartopy_feature_scale,
                                        line_color='#2251dd', projection=ccrs.PlateCarree()
                                        ) if self.params.show_rivers else None
                states = gv.feature.states(scale=self.params.cartopy_feature_scale,
                                        projection=ccrs.PlateCarree(),
                                        color=None) if self.params.show_states else None
                grid = gv.feature.grid(scale=self.params.cartopy_feature_scale,
                                        projection=ccrs.PlateCarree()
                                        ).apply.opts() if self.params.show_grid else None

                plot_features = [plot, coast, lakes, rivers, states, grid]

                features = []
                for f in plot_features:
                    if f is not None:
                        features.append(f)
                    else:
                        pass

                overlay = hv.Overlay([f for f in features]).collate() if plot is not None else None
            else:
                overlay = plot
        else:
            overlay = None

        return overlay


    def get_xy_opts(self,data):
        gen_opts = self.get_gen_opts(data)
        xy_opts = dict(clabel=str(data.name) + " " + str(data.units), invert_yaxis=self.params.invert_yaxis, 
                        invert_xaxis=self.params.invert_xaxis)
        opts = {**gen_opts, **xy_opts}

        return opts

    def get_converter(self, data, plot_type, field, xc, yc, tc, zc):
        """
        Returns a HoloViewsConverter according to plot type.

        Parameters:
                data (xr.Dataset): Data to be plotted. 

        Returns:
                plot_type (str): Plot type
        """
        if plot_type == 'xy':
            if self.params.enable_projection.clicks:
                converter = hvplot.HoloViewsConverter(data, xc, yc,
                        levels=self.params.color_levels,
                        projection=self.params.proj,
                        project=True,
                        geo=True,
                        )
            else:
                converter = hvplot.HoloViewsConverter(data, x=xc, y=yc, #
                        levels=self.params.color_levels,
                        )

        elif plot_type == 'yz':
            converter = hvplot.HoloViewsConverter(data, yc, zc, levels=self.params.color_levels,
                    )
        
        elif plot_type == 'xt':
            converter = hvplot.HoloViewsConverter(data, x=xc, y=tc, 
                        levels=self.params.color_levels,
                        )

        elif plot_type == 'yt':
            converter = hvplot.HoloViewsConverter(data, x=yc, y=tc, 
                        levels=self.params.color_levels,
                        )

        elif plot_type == 'ft':
            converter = hvplot.HoloViewsConverter(data, x=tc, y=field, 
                                                  ) 
            #this produces an error for second file when diff than first file keys 
            
        elif plot_type == 'zt':
            converter = hvplot.HoloViewsConverter(data, x=zc, y=field, 
                                                  )
                    

        return converter
