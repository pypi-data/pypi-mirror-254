import panel as pn
import holoviews as hv
import hvplot.xarray
import xarray as xr
import param
import os
import numpy as np

import geoviews as gv
import cartopy.crs as ccrs

from eviz.lib.iviz import dash_utils as du
from .base_dashboard import BaseDash
from eviz.lib.data.data_selector import DataSelector
from eviz.lib.iviz.config import configIviz
import eviz.lib.iviz.params_util as params_util


pn.extension()
hv.extension('bokeh', logo=False)


class LisDash(BaseDash):

    def __init__(self, config, params):
        super().__init__(config=config, params=params)

    def set_zc(self, field, zc, file, z): # need something like this for the comparison file 
        """
        Set the z coordinate label according to the currently selected field for plotting.

        Sets:
                plot_type.options (params): Updates available plot types.
    """
        data = file
        add_plot = False

        if field == 'SoilMoist_inst':
            eval(f"self.params.param.set_param({zc}='SoilMoist_profiles')")
            data = data.assign_coords({'SoilMoist_profiles': data['SoilMoist_profiles']})
            add_plot = True
            self.params.param.z.label = 'SoilMoist_profiles'
        elif field == 'SoilMoist_tavg':
            eval(f"self.params.param.set_param({zc}='SoilMoist_profiles')")
            data = data.assign_coords({'SoilMoist_profiles': data['SoilMoist_profiles']})
            self.params.param.z.label = 'SoilMoist_profiles'
            add_plot = True
        elif field == 'SoilTemp_inst':
            eval(f"self.params.param.set_param({zc}='SoilTemp_profiles')")
            data = data.assign_coords({'SoilTemp_profiles': data['SoilTemp_profiles']})
            self.params.param.z.label = 'SoilTemp_profiles'
            add_plot = True
        elif field == 'SmLiqFrac_inst':
            eval(f"self.params.param.set_param({zc}='SmLiqFrac_profiles')")
            data = data.assign_coords({'SmLiqFrac_profiles': data['SmLiqFrac_profiles']})
            self.params.param.z.label = 'SmLiqFrac_profiles'
            add_plot = True
        elif field == 'RelSMC_inst':
            eval(f"self.params.param.set_param({zc}='RelSMC_profiles')")
            data = data.assign_coords({'RelSMC_profiles': data['RelSMC_profiles']})
            self.params.param.z.label = 'RelSMC_profiles'
            add_plot = True

        if add_plot:
            file = data
            self.set_z_bounds(data, self.params.zc, z)
            plot_types = self.params.plot_type.options
            new_plots = {'Profile (field/lev) Plot': 'profile'}
            self.params.plot_type.options = {**plot_types, **new_plots}

        return file

    def set_z_bounds(self, data, zc, z):
        """
        Set the bounds of the z coordinate slider for selection of data.

                Parameters:
                        data (xr.Dataset): Dataset to get z values from.
                        zc (params.zc): The z coordinate label.

                Sets:
                        z.bounds (param.z.bounds): Number of values for z. 
                        gif_dim (params.gif_dim): Adds to available dimensions for gifs.
        """
        d = data[self.params.field]
        z_length = len(d[zc].values)
        if z_length != 1:
            end_z = z_length - 1 
            z_bounds = (0,end_z)
            self.params.param[z].bounds = z_bounds
            self.params.gif_dim.options.append(zc)

            self.params.param.yz_xlim.bounds = self.params.xy_ylim
            self.params.yz_xlim = self.params.param.yz_xlim.bounds
            self.params.param.yz_ylim.bounds = z_bounds
            self.params.yz_ylim = self.params.param.yz_ylim.bounds

    def get_proj_from_attrs(self):
        """
        Get projection information from the datasets metadata.

        Sets:
                proj (params.proj): The current projection value to apply to data.
        """
        if 'projection' in self.params.file.attrs:
            proj = str(self.params.file.attrs['projection']).title().strip().replace(" ","")
        elif 'MAP_PROJ_CHAR' in self.params.file.attrs:
            proj = str(self.params.file.attrs['MAP_PROJ_CHAR']).title().strip().replace(" ","")
        elif 'MAP_PROJECTION' in self.params.file.attrs:
            proj = str(self.params.file.attrs['MAP_PROJECTION']).title().strip().replace(" ","")
        else:
            proj = self.params.proj

    @param.depends('params.file', 'params.field', 'params.z', 'params.t', 'params.apply_operation_button.clicks', 
                    watch=True)
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
        self.params.file = self.set_zc(self.params.field, 'zc', self.params.file, 'z')
        self.data4d = self.params.file[self.params.field]
        yaml_convert = self.unit_conversion_check(self.data4d, self.params.field)
        self.data4d = self.apply_operations_to_data(data=yaml_convert)

        if self.params.tc in list(self.params.file.coords) and self.params.tc not in list(self.data4d.coords):
            self.data4d = eval(f"self.params.file.isel({self.params.tc}=self.params.t)")
            self.data4d = self.data4d[self.params.field]
        elif self.params.tc in list(self.data4d.coords):
            self.data4d = self.data[self.params.tc][self.params.t]

        if self.params.zc in list(self.data4d.dims):
            self.data2d = eval(f"self.data4d.isel({self.params.zc}=self.params.z)")
            self.data3d = self.data4d
            self.all_vars_data_slice = eval(f"self.params.file.isel({self.params.zc}=self.params.z)")
            self.params.param['z'].precedence = +1
        elif self.params.zc not in list(self.data4d.dims):
            self.data2d = self.data4d
            self.all_vars_data_slice = self.params.file
            self.data3d = self.data4d #data only has three dimensions 
        else:  #data is just lat/lon
            self.data2d = self.data4d
            self.data3d = self.data4d

        self.update_plot_limits()
        self.params.set_plot_types_on_var_change()

    @param.depends('params.field', 'params.t', 'params.z', 'params.file')
    def update_plot_limits(self):
        """
        Update the x and y limit values according to the data for the xy (lat/lon) plot.

                Sets:
                        xy_ylim.start (params): start of y limit values
                        xy_ylim.end (params): end of y limit values
                        xy_ylim.value (params): current value of y limit
                        xy_xlim.start (params): start of x limit values
                        xy_xlim.end (params): end of x limit values
                        xy_xlim.value (params): current value of x limit

        """
        data2d = self.data2d
        if len(data2d[self.params.xc].values) != 1:
            xvals = (data2d[self.params.xc].values.min(), data2d[self.params.xc].values.max())
        else:
            xvals = (data2d[self.params.xc].values.min(), data2d[self.params.xc].values.max())
            self.params.xy_xlim.precedence = -1

        if len(data2d[self.params.yc].values) != 1:
            yvals = (data2d[self.params.yc].values.min(), data2d[self.params.yc].values.max())
        else:
            yvals = (data2d[self.params.yc].values.min(), data2d[self.params.yc].values.max())
            self.params.xy_ylim.precedence = -1
            self.params.yz_ylim.precedence = -1

        self.params.param.xy_ylim.bounds = yvals
        self.params.xy_ylim = yvals

        self.params.param.xy_xlim.bounds = xvals
        self.params.xy_xlim = xvals

        self.globallons = xvals
        self.globallats = yvals

    def title_function(self, data, exp, zc, tc):
        """
        Returns a title based off the input data, experiment name if available, zc and tc coordinates, or if
        the user has selected a custom title, title input will come from title_input widget.

                Parameters:
                        data (xarray): xarray dataset to get attributes from, including .name and .units.
                        exp (str): experiment name, if available, from yaml configuration.
                        zc (str): Input zc coordinate, will check to confirm in data, used for .units and .values.
                        tc (str): Input tc coordinate, confirm in data, uses .name, .units, .values
                Returns:
                        title (str): Plot title.
        """
        if hasattr(data, 'long_name'):
            pass
        else:
            data.attrs['long_name'] = data.name

        if hasattr(data, 'units'):
            pass
        else:
            data.attrs['units'] = ''

        if exp is not None:
            if zc in list(data.coords):
                if hasattr(data[zc], 'units'):
                    pass
                else:
                    data[zc].attrs['units'] = ''
                title = self.params.title_input.value if self.params.custom_title else (str(exp) + ': ' + str(data.long_name) +
                                                                                " (" + str(data.units) + ") @ " + str(
                            data[zc].values) + " " + str(data[zc].units) )
            else:
                title = self.params.title_input.value if self.params.custom_title else (str(exp) + ': ' + str(data.long_name) +
                                                                                " (" + str(data.units) + ") " + str(
                            data[tc].values))
        else:
            if zc in list(data.coords):
                if hasattr(data[zc], 'units'):
                    pass
                else:
                    data[zc].attrs['units'] = ''
                title = self.params.title_input.value if self.params.custom_title else (str(data.long_name) + " (" +
                                                                                str(data.units) + ") @ " + str(
                            data[zc].values) + " " + str(data[zc].units))
            else:
                title = self.params.title_input.value if self.params.custom_title else (str(data.long_name) + " " +
                                                                                str(data.units) + "")
        return title

    @param.depends('params.gif_button.clicks')
    def gif(self):
        """
        Creates and returns a gif based on the user selected dimension to animate through.

                Returns:
                        gif (gif): Animated gif plotted and saved to current working directory. User selects which
                                    dimension to animate through.
        """
        if self.params.gif_button.clicks:
            self.params.progressbar.visible = True
            data = self.data4d
            params_list = self.params.get_param_values()
            params = dict((x, y) for x, y in params_list)
            img_opts = self.get_img_opts(data)
            proj_str = self.params.proj
            proj_method = getattr(ccrs, proj_str)
            filename = self.filename()

            if self.params.gif_dim.value == self.params.zc:
                # data3d = eval(f"data.isel({self.params.tc}=self.params.t)")
                pass
            elif self.params.gif_dim.value == self.params.tc:
                if self.params.zc is not None:
                    data3d = eval(f"data.isel({self.params.zc}=self.params.z)")
                else:
                    data3d = data
            if self.params.enable_projection.clicks:
                plot = data3d.hvplot(x=self.params.xc, y=self.params.yc, cmap=self.params.cmap, crs=ccrs.PlateCarree(),
                                     projection=self.get_cartopy_projection(data3d[self.params.xc], self.params.xc,
                                     data3d[self.params.yc], self.params.yc),
                                     project=True, xlim=self.params.xy_xlim.value,
                                     ylim=self.params.xy_ylim.value, cnorm=self.params.cnorm, dynamic=False).opts(
                    clabel=str(data3d.name) + " " + str(data3d.units), cformatter=self.formatter,
                    framewise=False,
                    rasterize=True, )
            else:
                plot = data3d.hvplot(x=self.params.xc, y=self.params.yc, cmap=self.params.cmap, cnorm=self.params.cnorm,
                                     xlim=self.params.xy_xlim.value, ylim=self.params.xy_ylim.value,
                                     # rasterize=True,
                                     dynamic=False).opts(clabel=str(data3d.name) + " " + str(data3d.units),
                                                         cformatter=self.formatter,
                                                         framewise=False)

            if self.config.output_dir is not None:
                output_dir = self.config.output_dir
            else:
                output_dir = os.getcwd()
            filepath = os.path.join(output_dir, filename)

            if self.params.show_coastlines:
                proj_str = self.params.proj
                proj_method = getattr(ccrs, proj_str)
                coast = gv.feature.coastline().opts(projection=self.get_cartopy_projection(data3d[self.params.xc],
                                     self.params.xc, data3d[self.params.yc], self.params.yc), 
                                     xlim=self.params.xy_xlim.value, ylim=self.params.xy_ylim.value)
                border = gv.feature.borders().opts(projection=self.get_cartopy_projection(data3d[self.params.xc],
                                     self.params.xc, data3d[self.params.yc], self.params.yc), 
                                     xlim=self.params.xy_xlim.value, ylim=self.params.xy_ylim.value)
                borders = coast * border
                giffer = hv.Overlay(plot * borders).collate()  # .opts(framewise=True)
                gif = hv.save(giffer, f'{filepath}.gif', fmt='gif', fps=2, toolbar=False)
            else:
                gif = hv.save(plot, f'{filepath}.gif', fmt='gif', fps=2, toolbar=False)
            self.params.progressbar.visible = False
            self.notyf.success(" Gif saved! ")
            # return gif      

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

        elif plot_type == 'pn': #polar north
            converter = hvplot.HoloViewsConverter(data, x=xc, y=yc,
                    levels=self.params.color_levels, ylim = (-90, -60),
                    xlim = (-180, 180),
                    projection = ccrs.NorthPolarStereo(central_longitude=self.params.polar_central_longitude),
                    )

        elif plot_type == 'ps': #polar south
            converter = hvplot.HoloViewsConverter(data, x=xc, y=yc,
                    levels=self.params.color_levels, ylim = (-90, -60),
                    xlim = (-180, 180),
                    projection=ccrs.SouthPolarStereo(central_longitude=self.params.polar_central_longitude),
                    )

        elif plot_type == 'zt':
            converter = hvplot.HoloViewsConverter(data, x=zc, y=field, 
                                                  )
                    

        return converter