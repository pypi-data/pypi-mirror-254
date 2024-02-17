import logging

from eviz.lib.data.data_selector import DataSelector

logging.getLogger("param.main").setLevel(logging.CRITICAL)
import holoviews as hv
import pandas as pd
import xarray as xr
import param
import panel as pn
import os
import numpy as np
import logging
import hvplot.xarray
import hvplot.pandas

import geoviews as gv
import cartopy.crs as ccrs

import glob

from eviz.lib.iviz.time_average import TimeAvg

import eviz.lib.iviz.params_util as params_util
import eviz.lib.iviz.dash_utils as du
from eviz.models.iviz.root_dashboard import RootDash
from eviz.lib.iviz.config import configIviz

pn.extension()
hv.extension('bokeh', logo=False)

nalat = (0, 90)
nalon = (-170, -20)

# salat = (10, -90)
salat = (-90, 20)
salon = (-170, -10)

eulat = (0, 90)
eulon = (-20, 60)

asialat = (0, 90)
asialon = (50, 180)

auslat = (-60, 10)
auslon = (70, 180)

afrlat = (-40, 40)
afrlon = (-50, 90)


class BaseDash(RootDash):
    """ The BaseDash class represents an interactive visualization dashboard for earth system model climate data,
    using Panel, Param, Hvplot, and Xarray. 

    Attributes:
            config (dict): Config class with file and data information.
            params (dict): Input class with Parameters, configured with yaml and/or input data attributes;
                            contains input data.
    """
    data4d = None
    data3d = None
    data2d = None
    data4d_2 = None
    zonal_data2 = None
    formatter = None
    clim = None
    layout_diff = None
    comparison_file = None
    tropo = None
    tropopause = None
    data_2 = None
    zonal_clim = (None, None)
    time_series = None
    ts = None
    diff_data = None
    ft_diff = None
    zt_diff = None
    zt = None
    ztd = None
    ztd2 = None
    zt2 = None
    tc = None
    tc2 = None
    tc_diff = None
    tcd = None
    tcd2 = None
    
    logger = logging.getLogger(__name__)

    def __init__(self, config, params):
        super().__init__(config=config, params=params)

    def _postprocess_data(self, file):
        """
        Carries out post-processing of data (post unit conversion and data dimension selections),
        including checking for needed remapping of xc values.

        Sets:
                self.data2d (xr dataset)): lon_remap_check
        """
        # After data has been selected and the field has been set, check the longitude values
        # if they need to be re-mapped and relabel coordinates if needed
        self.data2d = self.lon_remap_check(self.data2d, self.params.xc, self.params.yc)
        self.data2d = self.lat_remap_check(self.data2d, self.params.xc, self.params.yc)

    def lat_remap_check(self, data, xc, yc):
        """
        After data has been selected and field has been converted, check that the longitude
        values are not 0-360. Remap to -180, 180 if so.

        Parameters:
                data (xr dataset): data to check for 0-360 lon coordinates
                xc (str): x coordinate name of data
                yc (str): y coordinate name of data

        Returns:
                data (xr dataset): data with remapped longitude values if needed
        """
        if any(data[yc].values > 90):
            data[yc] = np.where(data[yc] > 90, data[yc] - 180, data[yc])
            self.params.set_yc_xyplot_limits_sliders(data, yc)
        else:
            data = data
        return data

    def lon_remap_check(self, data, xc, yc):
        """
        After data has been selected and field has been converted, check that the longitude
        values are not 0-360. Remap to -180, 180 if so.

        Parameters:
                data (xr dataset): data to check for 0-360 lon coordinates
                xc (str): x coordinate name of data
                yc (str): y coordinate name of data

        Returns:
                data (xr dataset): data with remapped longitude values if needed
        """
        if any(data[xc].values > 180):
            data[xc] = np.where(data[xc] > 180, data[xc] - 360, data[xc])
            self.params.set_xc_xyplot_limits_sliders(data, xc)
        else:
            data = data
        return data

    @param.depends('params.multi_file', 'params.field', 'params.z', 'params.t', 
                    'params.apply_operation_button.clicks')
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
        self.data4d = self.params.file[self.params.field]
        yaml_convert = self.unit_conversion_check(self.data4d, self.params.field)
        self.data4d = self.apply_operations_to_data(data=yaml_convert)

        if self.params.tc in list(self.params.file.coords) and self.params.tc not in list(self.data4d.coords):
            self.data4d = eval(f"self.params.file.isel({self.params.tc}=self.params.t)")
            self.data4d = self.data4d[self.params.field]
        # elif self.params.tc in list(self.data4d.coords):
            # self.data4d = self.data4d[self.params.tc][self.params.t]

        if self.params.zc in list(self.data4d.coords):
            self.data2d = eval(f"self.data4d.isel({self.params.zc}=self.params.z, {self.params.tc}=self.params.t)")
            self.data3d = eval(f"self.data4d.isel({self.params.tc}=self.params.t)")
        elif self.params.zc not in list(self.data4d.coords):
            # self.params.zc = None #try
            if len(self.data4d.dims) == 2:
                self.data2d = self.data4d
            else:
                self.data2d = eval(f"self.data4d.isel({self.params.tc}=self.params.t)")
            self.data3d = self.data4d   # data only has three dimensions
        else:  # data is just lat/lon
            self.data2d = self.data4d

        self.params.set_plot_types_on_var_change(self.params.file, self.params.field, self.params.xc, 
                                                self.params.yc, self.params.tc, self.params.zc)

        return self.data2d

    # @param.depends('params.trop_field')
    def overlay_trop(self, zonal):
        """
        Returns an overlay of zonal plot with tropopause line.

        Parameters:
                zonal (plot): A Holoviz zonal (yz) plot to overlay with tropopause line.

        Returns:
                zonal_ov (overlay): Overlay plot
        """
        if self.config.trop_filename is not None:
            tropp = xr.open_dataset(self.config.trop_filename)
            trop_fields = [f for f in list(tropp.keys()) if "TROP" in f]
            self.params.param["trop_field"].objects = trop_fields
            self.params.param.set_param(trop_field=trop_fields[0])
            self.params.param.trop_field.precedence = +1
            self.params.param.add_trop.precedence = +1

            if self.params.add_trop:
                trop_var = tropp[self.params.trop_field]
                if trop_var.units == 'Pa':
                    self.config.trop_conversion = 1 / 100.0
                elif trop_var.units == 'hPa':
                    self.config.trop_conversion = 1.0
                else:
                    self.config.trop_conversion = 1.0

                # trop = trop_var.isel(time=0).mean(dim='lon')
                trop = eval(f"trop_var.isel({self.params.tc}=self.params.t).mean(dim=self.params.xc)")
                tropopause = trop * float(self.config.trop_conversion)
                self.tropopause = tropopause
                tropopause = tropopause.hvplot.line(flip_yaxis=self.params.invert_yaxis_z, line_width=2.0,
                                                    line_color='black',
                                                    line_dash='dashed')
                self.tropo = tropopause
                zonal_ov = hv.Overlay(zonal * tropopause)
            else:
                zonal_ov = zonal
        else:
            zonal_ov = zonal
            print('No tropopause height file provided. Edit yaml file with path.')
        return zonal_ov

    def profileplot(self, data, xc, yc, tc):
        """ Create a profile plot of the input variable, averaging over xc, yc, and tc.

        Parameters:
                data (xarray): data variable
                xc (int): x coordinate selection value.
                yc (int): y coordinate selection value.
                tc (int): t coordinate selection value.

        Returns:
                profile_plot (plot): line holoviews plot

        """
        if len(np.atleast_1d(data[tc].values)) > 1:
            data1d = eval(f"data.isel({tc}=self.params.t)")
            data1d = data1d.mean(dim=[xc, yc])
        else:
            data1d = data.mean(dim=[xc, yc]).isel()
        try:
            profile_plot = data1d.hvplot.line(by='time', invert=self.params.profile_invert_axes,
                                              flip_yaxis=self.params.profile_invert_yaxis,
                                              logy=self.params.profile_logy, min_height=700, min_width=700, responsive=True,
                                              aspect=1.0,
                                              max_height=900, max_width=900)
        except Exception as e:
            self.logger.error(f"{e}: Issue creating profile plot")
            profile_plot = None
            self.notyf.error(" Error creating profile plot! Please check log. ")

        return profile_plot

    @pn.depends('params.add_time_series_plot_btn.clicks', 'params.field', 'params.z')
    def time_series_plot(self):
        """
        Returns a time series plot based on the currently selected dataset in the multi_selector.

        Parameters:
                multi_selector (str): Select multiple files and navigate directories.

        Returns:
                time_series (pn.Tabs): Tabs panel object with difference plots.
        """
        if self.params.add_time_series_plot_btn.clicks:
            if self.time_series is not None:
                self.time_series = None
            if os.path.isdir(self.params.multi_selector.value[0]):
                pth = os.path.join(self.params.multi_selector.value[0] + '/*nc*')
                ds = xr.open_mfdataset(pth)
            else:
                ds = xr.open_mfdataset(self.params.multi_selector.value)
            ts_data = self.unit_conversion_check(ds, self.params.field)
            regional_selected = eval(f"ts_data.sel({self.params.xc}=slice(self.params.xy_xlim[0], self.params.xy_xlim[1]), \
                                        {self.params.yc}=slice(self.params.xy_ylim[0], self.params.xy_ylim[1]))")
            self.time_series_mean = eval(f"regional_selected.mean(dim=[self.params.xc, self.params.yc])")

            ts_data = eval(f"self.time_series_mean[self.params.field].isel({self.params.zc}=self.params.z)")
            self.time_series = ts_data.hvplot.line().opts(height=700, width=1000)

            return self.time_series

    @pn.depends('params.run_time_avg_btn.clicks', 'params.regions', 'params.zoom', watch=True)
    def create_time_av(self):
        """
        Triggered by the run_time_avg_btn, this function uses the Panel template modal where the user selects files in
        the multi_selector, enters what variables to average over, and creates a time averaged dataset. The time 
        averaged dataset is then set as the tool's input file and will immediately visualize the results.
        """
        if self.params.run_time_avg_btn.clicks:
            if self.params.multi_selector.value:
                time_ave = TimeAvg(files=self.params.multi_selector.value, run=self.params.run_time_avg_btn,
                                   tc=self.params.tc,
                                   all_vars=self.params.all_variables,
                                   var_inp=self.params.variable_input)
                self.time_ave = time_ave

                current_files = self.params.param.multi_file.objects
                current_files.insert(0, self.time_ave.output)

                new_files = [time_ave.output]
                for i in self.params.param.multi_file.objects:
                    new_files.append(i)
                self.params.param['multi_file'].objects = new_files
                self.params.multi_file = self.time_ave.output

                self.notyf.success(" Time average complete! In files/plots ")

    def get_comparison_ds(self,d1,d2):
        ds = xr.Dataset()
        ds[self.params.field] = d1
        ds[self.params.field+"_2"] = d2
        return ds

    def get_plot_data(self,data,plot_type):
        if plot_type == 'yz':
            data = self.data3d.mean(dim=self.params.xc)
        elif plot_type == 'tc':
            data = self.data3d.sum(dim=self.params.zc)


#Re-write this to use xc, yc, zc, tc
    def get_converter(self, data, plot_type, field, xc, yc, tc, zc, by=None):
        """
        Returns a HoloViewsConverter according to plot type.

        Parameters:
                data (xr.Dataset): Data to be plotted. 

        Returns:
                plot_type (str): Plot type
        """
        if plot_type == 'xy':
            if self.params.enable_projection.clicks:
                converter = hvplot.HoloViewsConverter(data, self.params.xc, self.params.yc,
                        levels=self.params.color_levels,
                        projection=self.get_cartopy_projection(data[self.params.xc], data[self.params.yc]),
                        project=True,
                        geo=True,
                        global_extent=True,
                        # **opts
                        )
            else:
                converter = hvplot.HoloViewsConverter(data, x=self.params.xc, y=self.params.yc, #
                        levels=self.params.color_levels,
                        # **opts
                        )
        elif plot_type == 'yz':
            converter = hvplot.HoloViewsConverter(data, self.params.yc, self.params.zc, levels=self.params.color_levels,
                    # **opts
                    )
        
        elif plot_type == 'xt':
            converter = hvplot.HoloViewsConverter(data, x=self.params.tc, y=self.params.xc, 
                                levels=self.params.color_levels, 
                                # **opts
                                )

        elif plot_type == 'yt':
            converter = hvplot.HoloViewsConverter(data, x=self.params.tc, y=self.params.yc, 
                                levels=self.params.color_levels, 
                                # **opts
                                )

        elif plot_type == 'ft':
            converter = hvplot.HoloViewsConverter(data, x=self.params.tc, y=field, by=by, 
                            # **opts
                            ) 

            #this produces an error for second file when diff than first file keys 

        elif plot_type == 'pn': #polar north
            converter = hvplot.HoloViewsConverter(data, x=self.params.xc, y=self.params.yc,
                    levels=self.params.color_levels, ylim = (-90, -60),
                    xlim = (-180, 180),
                    projection = ccrs.NorthPolarStereo(central_longitude=self.params.polar_central_longitude), 
                    # **opts
                    )

        elif plot_type == 'ps': #polar south
            converter = hvplot.HoloViewsConverter(data, x=self.params.xc, y=self.params.yc,
                    levels=self.params.color_levels, ylim = (-90, -60),
                    xlim = (-180, 180),
                    projection=ccrs.SouthPolarStereo(central_longitude=self.params.polar_central_longitude, 
                    # **opts
                    )
                    )

        elif plot_type == 'zt':
            # converter = hvplot.HoloViewsConverter(data, x=self.params.zc, y=self.params.field, **opts)
            converter = hvplot.HoloViewsConverter(data, x=self.params.zc, y=field, 
                                                #   **opts
                                                  )
                    

        return converter


    def _plot(self, converter, kind, opts=None):
        return eval(f"converter.{kind}().opts(**opts)")


    def set_f1_xy(self, data2d):
        """
        Set xy plot for file 1. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.

        Sets:
                xy (list): list containing xy plots.
        """
        xy = []
        if 'xy' in self.params.plot_type.value:
            img_opts = self.get_xy_opts(data2d)
            title = self.title_function(data2d, self.config.exp_name, self.params.zc, self.params.tc)
            img_opts['title'] = title
            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(data2d, 'xy', self.params.field, 
                                self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                plot_kind,
                                img_opts
                                )
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker1 = self.colorbar_ticks(plot, data2d, self.clim[0], self.clim[1])
                    plot.opts(colorbar_opts={'ticker': ticker1})
                plot = self.create_overlay(plot)
                plot = plot.hist() if self.params.add_histo else plot
                xy.append(plot)
        self.xy = xy
    
    def set_f1_yz(self, data2d):
        """
        Set yz plot for file 1. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.

        Sets:
                yz (list): list containing yz plots.
        """
        yz = []
        if 'yz' in self.params.plot_type.value:
            zonal_data = self.data3d.mean(dim=self.params.xc)
            self.zonal_data1 = zonal_data

            if (self.params.zonal_clim != None) and (self.params.set_yz_clim):
                self.zonal_clim = self.params.zonal_clim
            else:
                self.zonal_clim = self.get_clim(self.zonal_data1, self.zonal_data2) 

            zonal_title = self.zonal_title(self.data3d, self.config.exp_name)
            zonal_opts = self.get_yz_opts(data2d)
            zonal_opts['clim'] = self.zonal_clim
            zonal_opts['title'] = zonal_title

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(zonal_data, 'yz', self.params.field,
                                self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                plot_kind,
                                zonal_opts
                                )
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker2 = self.colorbar_ticks(plot, zonal_data, self.zonal_clim[0], self.zonal_clim[1])
                    plot.opts(colorbar_opts={'ticker': ticker2})
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(zonal_data.min().values), None))
                if self.config.trop_filename is not None:
                    plot = self.overlay_trop(plot)
                plot = plot.hist() if self.params.add_histo else plot
                yz.append(plot)
        self.yz = yz


    def set_f1_tc(self):
        """
        Set tc plot for file 1. 

        Sets:
                tc (list): list containing tc plots.
        """
        tc = []
        if 'tc' in self.params.plot_type.value:
            tc_data = self.data3d.sum(dim=self.params.zc)
            tc_data.attrs = self.data3d.attrs
            self.tcd = tc_data

            img_opts = self.get_xy_opts(tc_data)
            title = tc_data.name + ' Total Column'
            img_opts['title'] = title
            img_opts['clim'] = (0, None) if self.params.zero_clim else (None, None)

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(tc_data, 'xy', self.params.field, 
                                self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                plot_kind,
                                img_opts
                                )
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker2 = self.colorbar_ticks(plot, tc_data)
                    plot.opts(colorbar_opts={'ticker': ticker2})
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(tc_data.min().values), None))
                if self.config.trop_filename is not None:
                    plot = self.overlay_trop(plot)
                plot = self.create_overlay(plot)
                plot = plot.hist() if self.params.add_histo else plot
                tc.append(plot)
        self.tc = tc

    def set_f1_xt(self):
        """
        Set xt plot for file 1. 

        Sets:
                xt (list): list containing xt plots.
        """
        xt = []
        if 'xt' in self.params.plot_type.value:
            data3d = self.data4d
            if self.params.zc in list(data3d.coords):
                data2d = data3d.mean(dim=[self.params.yc, self.params.zc])
            else:
                data2d = data3d.mean(dim=self.params.yc)

            title = self.params.title_input.value + " " + self.params.xc + " / " + self.params.tc \
                    if self.params.custom_title else data3d.name + " (" + str(
                        data3d.units) + ") " + self.params.xc + " / " + self.params.tc

            img_opts = self.get_gen_opts(data3d)
            img_opts['title'] = title
            
            tvals = data2d[self.params.tc].values
            trange = (tvals[0], tvals[-1])
            img_opts['xlim'] = trange

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if plot_kind != 'contourf':
                    plot = self._plot(self.get_converter(data2d, 'xt', self.params.field, 
                                        self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                        plot_kind, 
                                        img_opts)
                    # if plot_kind == 'contour':
                    #     ticker7 = self.colorbar_ticks(plot, data2d)
                    #     plot.opts(colorbar_opts={'ticker': ticker7})
                    if self.params.cnorm == 'log':
                        plot = plot.opts(clim=(float(data2d.min().values), None))
                    plot = plot.hist() if self.params.add_histo else plot
                    xt.append(plot)
                else:
                    self.notyf.error("Filled contours unavailable for YT and XT plots. \
                        Please select a quadmesh, contour, or image plot.")
        self.xt = xt

    def set_f1_yt(self):
        """
        Set yt plot for file 1. 

        Sets:
                yt (list): list containing yt plots.
        """
        yt = []
        if 'yt' in self.params.plot_type.value:
            data3d = self.data4d
            if self.params.zc in list(data3d.coords):
                data2d = data3d.mean(dim=[self.params.xc, self.params.zc])
            else:
                data2d = data3d.mean(dim=self.params.xc)

            title = self.params.title_input.value + " " + self.params.yc + " / " + self.params.tc \
                  if self.params.custom_title else data3d.name + " (" + str(
                     data3d.units) + ") " + self.params.yc + " / " + self.params.tc

            img_opts = self.get_gen_opts(data3d)
            img_opts['title'] = title

            tvals = data2d[self.params.tc].values
            trange = (tvals[0], tvals[-1])
            img_opts['xlim'] = trange

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if plot_kind != 'contourf':
                    plot = self._plot(self.get_converter(data2d, 'yt', self.params.field,
                                      self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                      plot_kind, 
                                      img_opts)
                    # if plot_kind == 'contour':
                    #     ticker8 = self.colorbar_ticks(plot, data2d)
                    #     plot.opts(colorbar_opts={'sticker': ticker8})
                    if self.params.cnorm == 'log':
                        plot = plot.opts(clim=(float(data2d.min().values), None))
                    plot = plot.hist() if self.params.add_histo else plot
                    yt.append(plot)
                else:
                    self.notyf.error("Filled contours unavailable for YT and XT plots. \
                    Please select a quadmesh, contour, or image plot.")
        self.yt = yt

    def set_f1_polar(self, data2d):
        """
        Set polar plot for file 1. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                polar (list): list containing polar plots.
        """
        polar = []
        if 'polar' in self.params.plot_type.value:
            img_opts = self.get_gen_opts(data2d)
            img_opts['title'] = 'polar ' + self.params.polar_projection.value
            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if self.params.polar_projection.value == 'South':
                    plot = self._plot(self.get_converter(data2d, 'ps', self.params.field,
                                    self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                    plot_kind, 
                                    img_opts)
                elif self.params.polar_projection.value == 'North':
                    plot = self._plot(self.get_converter(data2d, 'pn', self.params.field, 
                                    self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                    plot_kind, 
                                    img_opts)
                # plot = plot * gv.feature.grid()
                # plot = plot.hist() if self.params.add_histo else plot
                polar.append(plot)
        self.polar = polar

    def set_f1_ts(self):
        """
        Set time series (ts) plot for file 1. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                ts (list): list containing ts plots.
        """
        if 'ts' in self.params.plot_type.value:
            if self.params.zc in list(self.data4d.coords):
                dims_to_avg = [self.params.xc, self.params.yc, self.params.zc]
            else:
                dims_to_avg = [self.params.xc, self.params.yc]

            tavg_data = self.data4d.mean(dim=dims_to_avg)

            ts = self._plot(self.get_converter(tavg_data, 'ft', 
                        self.params.field, self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                        'line', 
                        {'min_height': 700, 'min_width': 700, 'title': 'time series'})
        else:
            ts = None
        self.ts = ts

    def set_f1_zt(self):
        """
        Set zt (profile) plot for file 1. 

        Sets:
                zt (list): list containing zt plots.
        """
        if 'zt' in self.params.plot_type.value:

            data = self.data4d

            if len(np.atleast_1d(data[self.params.tc].values)) > 1:
                data1d = eval(f"data.isel({self.params.tc}=self.params.t)")
                data1d = data1d.mean(dim=[self.params.xc, self.params.yc])
            else:
                data1d = data.mean(dim=[self.params.xc, self.params.yc]).isel()
            self.ztd = data1d

            img_opts = self.get_zt_opts()
            plot = self._plot(self.get_converter(data1d, 'zt', self.params.field,
                            self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                            'line', 
                            img_opts)
            self.zt = plot
        else:
            self.zt = None

    def set_f1_ft(self, data2d, img_opts):
        """
        Set ft (field/time) plot for file 1. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                ft (list): list containing ft plots.
        """
        ft = []
        if '1d' in self.params.plot_type.value:
            for plot_kind in self.get_1d_plot_types(self.params.plot_kind.value):
                if plot_kind == 'hist':
                    img_opts['ylim'] = (None,None)
                elif plot_kind == 'box':
                    q98 = float(self.data3d.quantile(0.99))
                    ylim = (float(self.data3d.min().values), q98)
                    img_opts['ylim'] = ylim
                    img_opts['width'] = 800
                    try:
                        d[self.params.tc] = d[self.params.tc].dt.strftime('%Y-%m')
                    except:
                        pass
                else:
                    img_opts['ylim'] = (None,None)
                    img_opts['xlim'] = (None,None)

                if (self.params.avg_by_lev) and (self.params.zc in list(self.data3d.coords)):
                    d = self.data3d.mean(dim=self.params.zc)
                else:
                    d = self.data3d

                img_opts['title'] = plot_kind

                if self.params.plot_by:
                    plot = self._plot(self.get_converter(d, 'ft', self.params.field, 
                                                         self.params.xc, self.params.yc, 
                                                         self.params.tc, self.params.zc,
                                                         by=self.params.tc), plot_kind, 
                                                         img_opts)
                else:                    
                    plot = self._plot(self.get_converter(d, 'ft', self.params.field, 
                                                        self.params.xc, self.params.yc, 
                                                        self.params.tc, self.params.zc),
                                                        plot_kind, img_opts)

                plot = plot.hist() if self.params.add_histo else plot
                ft.append(plot)
        self.ft = ft

    def set_f1_2d_plots(self, data2d):
        """
        Run all file 1 2d plots. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.
        """
        self.set_f1_xy(data2d)
        self.set_f1_yz(data2d)
        self.set_f1_tc()
        self.set_f1_xt()
        self.set_f1_yt()
        self.set_f1_polar(data2d)

    def set_f1_1d_plots(self, data2d):
        """
        Run all file 1 1d plots. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.
        """
        self.ylim = self.get_ylim(self.data_1, self.data_2)

        img_opts = dict( 
                        height=700, width=700, 
                        tools=["hover"],
                        fontsize={'title': '8pt'}, 
                        ylim=self.ylim)
        
        self.set_f1_zt()
        self.set_f1_ts()
        self.set_f1_ft(data2d, img_opts)

    def get_f2_exp_name(self):
        """
        Return the experiment name for the secondary file. 

        Returns:
                exp_name (str): configured experiment name.
        """
        try:
            exp_name = self.config.file_dict[self.params.comparison_file]['exp_name']
        except:
            exp_name = " "
        return exp_name

    def set_f2_xy(self, data2d_2, field):
        """
        Set xy plot for file 2. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                xy2 (list): list containing xy plots.
        """
        xy = []
        if 'xy' in self.params.plot_type.value:
            img_opts = self.get_xy_opts(data2d_2)
            img_opts['xlim'] = self.params.xy_xlim2
            img_opts['ylim'] = self.params.xy_ylim2

            title = self.title_function(data2d_2, self.get_f2_exp_name(), self.params.zc, self.params.tc)
            img_opts['title'] = title

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(data2d_2, 'xy', field, 
                                  self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                                  plot_kind, img_opts)
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker3 = self.colorbar_ticks(plot, data2d_2, self.clim[0], self.clim[1])
                    plot.opts(colorbar_opts={'ticker': ticker3})
                plot = self.create_overlay(plot)
                plot = plot.hist() if self.params.add_histo else plot
                xy.append(plot)
        self.xy2 = xy

    def set_f2_yz(self, field):
        """
        Set yz plot for file 2. 

        Sets:
                yz2 (list): list containing yz plots.
        """
        yz = []
        if 'yz' in self.params.plot_type.value:
            zonal_data2d = self.data3d_2.mean(dim=self.params.xc2)
            zonal_data2d.attrs = self.data3d_2.attrs
            self.zonal_data2 = zonal_data2d

            # Get and set shared colorbar limits #
            if (self.params.zonal_clim != None) and (self.params.set_yz_clim):
                self.zonal_clim = self.params.zonal_clim
            else:
                self.zonal_clim = self.get_clim(self.zonal_data1, self.zonal_data2) 
            
            self.params.zonal_clim_min = self.zonal_clim[0]
            self.params.zonal_clim_max = self.zonal_clim[1]

            zonal_title = self.zonal_title(self.data3d_2, self.get_f2_exp_name())
            zonal_opts = self.get_yz_opts(zonal_data2d)
            zonal_opts['clim'] = self.zonal_clim
            zonal_opts['title'] = zonal_title

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(zonal_data2d, 'yz', field,
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                                                plot_kind, zonal_opts)
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker4 = self.colorbar_ticks(plot, zonal_data2d, self.zonal_clim[0], 
                                            self.zonal_clim[1])
                    plot.opts(colorbar_opts={'ticker': ticker4})
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(zonal_data2d.min().values), None))
                if self.config.trop_filename is not None:
                    plot = self.overlay_trop(plot)
                plot = plot.hist() if self.params.add_histo else plot
                yz.append(plot)
        self.yz2 = yz

    def set_f2_tc(self, field):
        """
        Set tc plot for file 2. 

        Sets:
                tc (list): list containing tc plots.
        """
        tc = []
        if 'tc' in self.params.plot_type.value:
            tc_data = self.data3d_2.sum(dim=self.params.zc2)
            tc_data.attrs = self.data3d.attrs
            self.tcd2 = tc_data

            # img_opts = self.get_gen_opts(tc_data)
            img_opts = self.get_xy_opts(tc_data)
            title = tc_data.name + ' Total Column'
            img_opts['title'] = title
            img_opts['clim'] = (0, None) if self.params.zero_clim else (None, None)

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(tc_data, 'xy', field, 
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                                plot_kind,
                                img_opts
                                )
                if plot_kind == 'contourf' or plot_kind == 'contour':
                    ticker2 = self.colorbar_ticks(plot, tc_data)
                    plot.opts(colorbar_opts={'ticker': ticker2})
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(tc_data.min().values), None))
                if self.config.trop_filename is not None:
                    plot = self.overlay_trop(plot)
                plot = self.create_overlay(plot)
                plot = plot.hist() if self.params.add_histo else plot
                tc.append(plot)
        self.tc2 = tc

    def set_f2_polar(self, data2d, field):
        """
        Set polar plot for file 2. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                polar2 (list): list containing polar plots.
        """
        polar = []
        if 'polar' in self.params.plot_type.value:
            # img_opts = self.get_xy_opts(data2d)
            img_opts = self.get_gen_opts(data2d)
            img_opts['title'] = 'polar ' + self.params.polar_projection.value

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if self.params.polar_projection.value == 'South':
                    plot = self._plot(self.get_converter(data2d, 'ps', field, 
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                                plot_kind, 
                                img_opts)
                elif self.params.polar_projection.value == 'North':
                    plot = self._plot(self.get_converter(data2d, 'pn', field, 
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                                plot_kind, 
                                img_opts)
                # plot = plot * gv.feature.grid()
                # plot = plot.hist() if self.params.add_histo else plot
                polar.append(plot)
        self.polar2 = polar        

    def set_f2_2d_plots(self, data2d_2, timeval, field):
        """
        Run all file 2 2d plots. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                plotval (str): variable name in data to plot.
                timeval (str): time value to select data.
                img_opts (dict): Dictionary of plot options.
        """
        self.set_f2_xy(data2d_2, field)
        self.set_f2_yz(field)
        self.set_f2_xt(field)
        self.set_f2_yt(field)
        self.set_f2_polar(data2d_2, field)
        self.set_f2_tc(field)

    def set_f2_xt(self, field):
        """
        Set xt plot for file 2. 

        Sets:
                xt (list): list containing xt plots.
        """
        xt = [] 
        if 'xt' in self.params.plot_type.value:
            data3d = self.data4d_2
            if self.params.zc2 in list(data3d.coords):
                data2d = data3d.mean(dim=[self.params.yc2, self.params.zc2])
            else:
                data2d = data3d.mean(dim=self.params.yc2)

            title = self.params.title_input.value + " " + self.params.xc2 + " / " + self.params.tc2 \
                    if self.params.custom_title else data3d.name + " (" + str(
                        data3d.units) + ") " + self.params.xc2 + " / " + self.params.tc2

            img_opts = self.get_gen_opts(data3d)
            img_opts['title'] = title

            tvals = data2d[self.params.tc2].values
            trange = (tvals[0], tvals[-1])
            img_opts['xlim'] = trange

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if plot_kind != 'contourf':
                    plot = self._plot(self.get_converter(data2d, 'xt', field, 
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                    plot_kind, 
                    img_opts)
                    if plot_kind == 'contour':
                        ticker7 = self.colorbar_ticks(plot, data2d)
                        plot.opts(colorbar_opts={'ticker': ticker7})
                    if self.params.cnorm == 'log':
                        plot = plot.opts(clim=(float(data2d.min().values), None))
                    plot = plot.hist() if self.params.add_histo else plot
                    xt.append(plot)
                else:
                    self.notyf.error("Filled contours unavailable for YT and XT plots. \
                        Please select a quadmesh, contour, or image plot.")
        self.xt2 = xt

    def set_f2_yt(self, field):
        """
        Set yt plot for file 2. 

        Sets:
                yt (list): list containing yt plots.
        """
        yt = []
        if 'yt' in self.params.plot_type.value:
            data3d = self.data4d_2

            if self.params.zc2 in list(data3d.coords):
                data2d = data3d.mean(dim=[self.params.xc2, self.params.zc2])
            else:
                data2d = data3d.mean(dim=self.params.xc2)

            title = self.params.title_input.value + " " + self.params.yc2 + " / " + self.params.tc2 \
                  if self.params.custom_title else data3d.name + " (" + str(
                     data3d.units) + ") " + self.params.yc2 + " / " + self.params.tc2

            img_opts = self.get_gen_opts(data3d)
            img_opts['title'] = title

            tvals = data2d[self.params.tc2].values
            trange = (tvals[0], tvals[-1])
            img_opts['xlim'] = trange

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                if plot_kind != 'contourf':
                    plot = self._plot(self.get_converter(data2d, 'yt', field, 
                            self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                            plot_kind, 
                            img_opts
                            )
                    if plot_kind == 'contour':
                        ticker8 = self.colorbar_ticks(plot, data2d)
                        plot.opts(colorbar_opts={'ticker': ticker8})
                    if self.params.cnorm == 'log':
                        plot = plot.opts(clim=(float(data2d.min().values), None))
                    plot = plot.hist() if self.params.add_histo else plot
                    yt.append(plot)
                else:
                    self.notyf.error("Filled contours unavailable for YT and XT plots. \
                    Please select a quadmesh, contour, or image plot.")
        self.yt2 = yt

    def set_f2_zt(self, field):
        """
        Set zt (profile) plot for file 2. 

        Sets:
                zt (list): list containing zt plots.
        """
        if 'zt' in self.params.plot_type.value:

            data = self.data4d_2

            if len(np.atleast_1d(data[self.params.tc2].values)) > 1:
                data1d = eval(f"data.isel({self.params.tc2}=self.params.t2)")
                data1d = data1d.mean(dim=[self.params.xc2, self.params.yc2])
            else:
                data1d = data.mean(dim=[self.params.xc2, self.params.yc2]).isel()
            self.ztd2 = data1d

            img_opts = self.get_zt_opts()

            plot = self._plot(self.get_converter(data1d, 'zt', field, 
                            self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                            'line', 
                            img_opts
                            )
            self.zt2 = plot

    def set_f2_ft(self, data2d_2, img_opts, field):
        """
        Set ft plot for file 2. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                ft2 (list): list containing ft plots.
        """
        ft = []
        if '1d' in self.params.plot_type.value:
            for plot_kind in self.get_1d_plot_types(self.params.plot_kind.value):
                if plot_kind == 'hist':
                    img_opts['ylim'] = (None,None)
                    img_opts['xlim'] = self.ylim
                elif plot_kind == 'box':
                    q98 = float(self.data3d_2.quantile(0.98))
                    ylim = (float(self.data3d_2.min().values), q98)
                    img_opts['ylim'] = ylim
                    img_opts['width'] = 800
                    try:
                        d[self.params.tc2] = d[self.params.tc2].dt.strftime('%Y-%m')
                    except:
                        pass
                else:
                    img_opts['ylim'] = (None,None)
                    img_opts['xlim'] = (None,None)
                img_opts['title'] = plot_kind

                d = self.data3d_2
                if (self.params.avg_by_lev) and (self.params.zc2 in list(self.data3d_2.coords)):
                    d = self.data3d_2.mean(dim=self.params.zc2)
                else:
                    d = self.data3d_2

                if self.params.plot_by:
                    plot = self._plot(self.get_converter(d, 'ft', field,
                                    self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2,
                                                         by=self.params.tc2), plot_kind, img_opts)
                else:
                    plot = self._plot(self.get_converter(d, 'ft', field, 
                                    self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                        plot_kind,
                        img_opts)
                plot = plot.hist() if self.params.add_histo else plot
                ft.append(plot)
        self.ft2 = ft

    def set_f2_1d_plots(self, data2d_2, field):
        """
        Run all file 1 1d plots. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
        """
        self.ylim = self.get_ylim(self.data_1, self.data_2)

        img_opts = dict( 
                        height=700, width=700, 
                        tools=["hover"],
                        fontsize={'title': '8pt'}, 
                        ylim=self.ylim)

        self.set_f2_zt(field)
        self.set_f2_ts(field)
        self.set_f2_ft(data2d_2, img_opts, field)

    def set_f2_ts(self, field):
        """
        Set ts (time series) plot for file 2. 

        Parameters:
                data2d (xr.Dataset): Data to be plotted.
                img_opts (dict): Dictionary of plot options.

        Sets:
                ts2 (list): list containing ts plots.
        """
        if 'ts' in self.params.plot_type.value:
            if self.params.zc2 in list(self.data4d_2.coords):
                dims_to_avg = [self.params.xc2, self.params.yc2, self.params.zc2]
            else:
                dims_to_avg = [self.params.xc2, self.params.yc2]

            tavg_data = self.data4d_2.mean(dim=dims_to_avg)

            ts = self._plot(self.get_converter(tavg_data, 'ft',
                            field, self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                    'line', 
                    {'min_height': 700, 'min_width': 700, 'title': 'time series'})
        else:
            ts = None
        self.ts2 = ts

    def get_1d_plot_types(self,plot_type_list):
        plot_types_1d = ['box', 'hist', 'violin']
        return [plot for plot in plot_types_1d if plot in plot_type_list]

    def get_2d_plot_types(self,plot_type_list):
        plot_types_2d = ['image', 'quadmesh', 'contourf', 'contour']
        return [plot for plot in plot_types_2d if plot in plot_type_list]

    @param.depends('params.multi_file', 'params.zero_clim', 'params.show_grid', 'params.z', 'params.t', 'params.field',
                   'params.show_grid', 'params.column_slider', 'params.show_coastlines', 'params.tabs_switch', 'params.logy_z',
                   'params.color_levels', 'params.cnorm', 'params.polar_projection.value', 'params.polar_coastlines', 
                   'params.colorbar_position', 'params.show_states', 'params.show_lakes', 'params.enable_projection.clicks', 
                   'params.zonal_clim_min', 'params.polar_central_longitude', 'params.show_rivers',
                   'params.zonal_clim_max', 'params.trop_field', 'params.add_trop', 'params.zonal_cnorm', 'params.add_histo',
                   'params.share_colorbar', 'params.clim_min', 'params.cartopy_feature_scale',
                   'params.clim_max', 'params.apply_operation_button.clicks', 'params.plot_type.value',
                   'params.profile_invert_axes', 'params.custom_title', 'params.plot_kind.value', 
                   'params.title_input.value', 'params.profile_invert_yaxis', 'params.profile_logy', 'params.ymin', 'params.ymax',
                   'params.cmap', 'params.invert_yaxis', 'params.invert_xaxis', 'params.alpha', 'params.invert_yaxis_z', 
                   'params.invert_xaxis_z', 'params.xy_xlim', 'params.xy_ylim', 'params.yz_xlim', 'params.yz_ylim', 
                   'params.set_xy_clim', 'params.plot_by', 'params.avg_by_lev', 'params.set_yz_clim')
    def make_layout(self):
        """
        Makes a hv.Layout with xy image, xy contours, and yz contours plot. Embeds in self.tabs pn.Tabs object defined
        in __init__. Returns new self.tabs.

        Returns:
                self.tabs (pn.Tabs): returns pn.Tabs object with embedded Layout.
        """
        self.tabs.loading = True

        self.params.tabs_switch = False if self.params.add_histo else self.params.tabs_switch
        # Set colorbar limits #
        if (self.params.clim != None) and (self.params.set_xy_clim):
            self.clim = self.params.clim
        else:
            self.clim = self.get_clim(self.data2d, self.data_2)
        self.set_cformatter()

        self.data_1 = self.data2d

        self.set_f1_2d_plots(self.data2d)
        self.set_f1_1d_plots(self.data2d)

        self.tabs.loading = False

        plot_list = [*self.xy, *self.yz, *self.tc, *self.xt, *self.yt, *self.polar, self.ts, self.zt, 
                    *self.ft
                    ]
        plots = self.create_plot_list(plot_list)

        layout = hv.Layout(plots, name=f'{self.params.field}').options(shared_axes=False, tabs=self.params.tabs_switch,
                                                                   merge_tools=True,
                                                                   width=700,
                                                                   ).cols(self.params.column_slider)

        self.layout = layout
        self.tabs[0] = (self.params.set_input(), layout)
        self.plot_dict.update({'tabs1': self.tabs})



    @pn.depends('params.second_file_input.value')
    def set_comparison_file(self):
        """
        Find files from the user entered location or from the files included in YAML configuration. Fill in the second file selector
        Parameter 'comparison_file' objects with files.

        Parameters:
                second_file_input (str): Parameter widget taking string inputs to directory to glob for files.

        Sets:
                comparison_file (selector): Object Selector parameter.
        """
        if self.params.second_file_input.value:
            nc_files = glob.glob(self.params.second_file_input.value + "/*.nc*")
            he5_files = glob.glob(self.params.second_file_input.value + "/*.he5*")
            hdf_files = glob.glob(self.params.second_file_input.value + "/*.hdf*")
            second_files = nc_files + he5_files + hdf_files
            self.params.param['comparison_file'].objects = second_files
            self.params.param['comparison_file'].default = second_files[0]
        elif self.config.is_yaml:
            if str(type(self.params.dataInput)) == 'str':
                pass
            else:
                try:
                    self.params.param['comparison_file'].objects = self.params.dataInput.objects
                    self.params.param['comparison_file'].default = self.params.dataInput.objects[0]
                except:
                    pass
        else:
            try:
                self.params.param['comparison_file'].objects = self.params.param['multi_file'].objects
                self.params.param['comparison_file'].default = self.params.param['multi_file'].objects[0]
            except:
                pass
        if self.params.comparison_file is None:
            self.params.comparison_file = self.params.param['comparison_file'].default

    def set_file2_param_values(self, file, comparison_source):
        """
        Set the secondary files Parameter default values and bounds using the data's attributes and coordinates.

        Parameters:
                file (xarray): Secondary file opened as a Xarray dataset. Info to set parameter values extracted from file.

        Sets:
                xc2 (str): X coordinate for file 2.
                yc2 (str): Y coordinate for file 2.
                tc2 (str): T coordinate for file 2.
                zc2 (str): Z coordinate for file 2.
        """
        ndims = params_util.get_ndims(file)
        self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2 = self.params.set_dim_params(
            model=self.params.comparison_source,
            xc=self.params.xc2, yc=self.params.yc2, tc=self.params.tc2, zc=self.params.zc2)
        self.params.check_for2d_file2(ndims=ndims) # check for less than 4 dims for file2, set zc2 precedence to -

    @param.depends('params.comparison_file', 
     'params.multi_file')
    def set_file2_params(self, file1, file2, comparison_source):
        """
        Set the t and z bounds, and the xy_ylim2 and xy_xlim2 values, for the secondary file accordinting to # of values in 
        each coordinate. Use the first files
        parameters and widgets if the same as 2nd file.

        Parameters:
                file1 (xarray): Primary file opened as a Xarray dataset.
                file2 (xarray): Secondary file opened as a Xarray dataset.

        Sets:
                t2 (int): T coordinate value for file 2.
                z2 (int): Z coordinate value for file 2.
                xy_ylim2 (int tuple): Tuple of integers representing the value of the xy ylim for plot 2.
                xy_xlim2 (int tuple): Tuple of integers representing the value of the xy xlim for plot 2.

        Returns:
                timeval (int):
                levval (int):
        """
        file1_coords = params_util.get_coords(file1)
        file2_coords = params_util.get_coords(file2)

        self.set_file2_param_values(
            self.comparison_file, self.params.comparison_source)
            # file=file2)  # by running this all the xc2, yc2, zc2, and tc2 values are set according to the determined model type
        if list(file2[self.params.tc2].values) == list(file1[self.params.tc].values):
            timeval = self.params.t
        else: #need to set the boundaries . and then need to set the default/value but only when its a new file. not when the value of the paramerter changes 
            times = len(list(file2[self.params.tc2].values))
            if times != 1:
                end_t = times - 1
                bounds_t = (0, end_t)
                self.params.param.t2.bounds = bounds_t
                self.params.param.t2.precedence = +1

                timeval = self.params.t2
            else:
                timeval = 0

        if self.params.zc2 in file2_coords and self.params.zc in file1_coords:
            if list(file2[self.params.zc2].values) == list(file1[self.params.zc].values):
                levval = self.params.z
            else:
                levs = len(list(file2[self.params.zc2].values))
                if levs != 1:
                    end_l = levs - 1
                    bounds_l = (0, end_l)
                    self.params.param.z2.bounds = bounds_l
                    self.params.param.z2.precedence = +1
                    levval = self.params.z2
                else:
                    levval = 0

        elif self.params.zc2 in file2_coords and self.params.zc not in file1_coords:  # if the second file has z and first does not
            levs = len(list(file2[self.params.zc2].values))
            if levs != 1:
                end_l = levs - 1
                bounds_l = (0, end_l)
                self.params.param.z2.bounds = bounds_l
                self.params.param.z2.precedence = +1
                levval = self.params.z2
        elif self.params.zc2 not in file2_coords:
            levval = None

        xvals = (file2[self.params.xc2].values.min(), file2[self.params.xc2].values.max())
        self.params.param.xy_xlim2.bounds = xvals
        self.params.xy_xlim2 = xvals
        if len(file2[self.params.xc2].values) != 1:
            self.params.param.xy_xlim2.precedence = +1 
 
        yvals = (file2[self.params.yc2].values.min(), file2[self.params.yc2].values.max())
        self.params.param.xy_ylim2.bounds = yvals
        self.params.xy_ylim2 = yvals
        if len(file2[self.params.yc2].values) != 1:
            self.params.param.xy_ylim2.precedence = +1 

        return timeval, levval

    @pn.depends('params.plot_second_file_button.clicks')
    def select_comparison_file(self):
        if self.params.plot_second_file_button.clicks == 1:

            if not self.params.comparison_source:
                self.notyf.error(" Please select a comparison source!")
            else:
                if self.params.comparison_file != None:

                    if self.params.comparison_file.startswith('http'):
                        comparison_file = DataSelector(self.params.comparison_file, self.params.comparison_source, 
                                    is_url=True).data
                    else:
                        comparison_file = DataSelector(self.params.comparison_file, self.params.comparison_source).data
                    comparison_file['O3'] = comparison_file['O3'] * 0.38
                    if self.config.file_dict is not None:
                        if self.params.comparison_file in list(self.config.file_dict.keys()):
                            file_dict = {"files": self.params.comparison_file, "file_dict": self.config.file_dict,
                                        "app_data": self.config.app_data}
                            v = file_dict["file_dict"][self.params.comparison_file]
                            file_dict = {**file_dict, **v}
                            config = configIviz(**file_dict)
                        else:
                            file_dict = {'files': self.params.comparison_file}
                            config = configIviz(**file_dict)
                    else:
                        file_dict = {'files': self.params.comparison_file}
                        config = configIviz(**file_dict)

                    self.comparison_file = comparison_file

                    self.timeval, self.levval = self.set_file2_params(self.params.file, self.comparison_file, 
                                                self.params.comparison_source)
                # try:
                #     comparison_file[self.params.tc2] = comparison_file[self.params.tc2].dt.strftime('%Y-%m-%d %H:%M:%S')
                # except:
                #     try:
                #         comparison_file[self.params.tc2] = pd.DatetimeIndex(self.file[self.tc].values)
                #         comparison_file[self.params.tc2] = comparison_file[self.params.tc2].dt.strftime('%Y-%m-%d %H:%M:%S')
                #     except:
                #         self.logger.info("Could not format time dimension labels")

                file1_keys = self.params.keys
                file2_keys = params_util.get_keys(self.comparison_file)

                self.params.set_f2_field(file1_keys, file2_keys)

                self.comparison_file = params_util.set_units_in_attrs(self.comparison_file, file2_keys)
                self.comparison_file = params_util.set_long_name_in_attrs(self.comparison_file, file2_keys)

    def set_selected_comparison_data(self):
        if self.params.param.comparison_field.precedence == -1:
            data4d_2 = self.comparison_file[self.params.field]
            field = self.params.field
        else:
            data4d_2 = self.comparison_file[self.params.comparison_field]
            field = self.params.comparison_field

        file2_coords = params_util.get_coords(data4d_2)
        yaml_convert = self.unit_conversion_check(data4d_2, field)
        self.data4d_2 = self.apply_operations_to_data(yaml_convert)

        #i should just do it here
        levval = self.params.z2 if self.params.param.z2.precedence == 1 else self.params.z
        timeval = self.params.t2 if self.params.param.t2.precedence == 1 else self.params.t

        if self.params.zc in file2_coords and self.params.tc in file2_coords:
            data2d_2 = eval(f"self.data4d_2.isel({self.params.zc}=levval, \
                                                    {self.params.tc}=timeval)")
            self.data3d_2 = eval(f"self.data4d_2.isel({self.params.tc}=timeval)")
        elif self.params.tc in file2_coords:
            data2d_2 = eval(f"self.data4d_2.isel({self.params.tc}=timeval)")
            self.data3d_2 = self.data4d_2
        elif self.params.zc in file2_coords:
            data2d_2 = eval(f"self.data4d_2.isel({self.params.zc}=levval)")
            self.data3d_2 = eval(f"self.data4d_2.isel({self.params.zc}=levval)")
        else:
            data2d_2 = data4d_2  # no time or lev values, just lat/lon and variable

        self.params.set_plot_types_on_var_change(self.comparison_file, field, self.params.xc, 
                                                 self.params.yc, self.params.tc,
                                                 self.params.zc)

        return data2d_2


    @param.depends('params.share_colorbar', 'params.show_grid', 'params.comparison_field', 'params.field', 'params.t',
                   'params.z', 'params.title_input.value', 'params.custom_title', 'params.show_coastlines', 'params.z2',
                   'params.t2', 'params.multi_file', 'params.tabs_switch', 'params.column_slider', 'params.logy_z', 
                   'params.color_levels', 'params.cnorm', 'params.zero_clim', 'params.show_states', 'params.show_lakes', 
                   'params.profile_invert_axes', 'params.profile_invert_yaxis', 'params.plot_kind.value',
                   'params.profile_logy', 'params.enable_projection.clicks', 'params.trop_field', 'params.add_trop', 
                   'params.zonal_cnorm', 'params.add_histo', 'params.apply_operation_button.clicks', 
                   'params.plot_type.value', 'params.plot_kind_1d.value', 'params.colorbar_position', 'params.cmap', 
                   'params.invert_yaxis', 'params.invert_xaxis', 'params.alpha', 'params.invert_yaxis_z', 
                   'params.invert_xaxis_z', 'params.yz_xlim', 'params.yz_ylim', 'params.xy_xlim2', 'params.xy_ylim2', 
                   'params.clim', 'params.plot_by', 'params.avg_by_lev', 'params.set_yz_clim', 'params.set_xy_clim')
    def make_second_layout(self):
        """
        Returns a pn.Tabs object with xy image, xy contours, and yz contours plot for the secondary file selected.

        Returns:
                tabs2 (pn.Tabs): Tabs panel object with plots for second file.
        """
        if self.params.plot_second_file_button.clicks == 1:
            self.tabs2.loading = True

            # Select coordinates and set data for the comparison file
            self.data2d_2 = self.set_selected_comparison_data()
            self.data_2 = self.data2d_2

            # Get projection 
            proj_str = self.params.proj
            proj_method = getattr(ccrs, proj_str)


            if self.params.param.comparison_field.precedence == +1:
                plotval = self.params.comparison_field
            else:
                plotval = self.params.field

            # Set 2d and 1d plots
            self.set_f2_1d_plots(self.data2d_2, plotval)
            self.set_f2_2d_plots(self.data2d_2, self.timeval, plotval)

            self.tabs2.loading = False

            # Assemble plots
            plot_list = [*self.xy2, *self.yz2, *self.tc2, *self.xt2, *self.yt2, *self.polar2, self.zt2, 
                        self.ts2, *self.ft2]
            plots = self.create_plot_list(plot_list)

            # Create plots
            self.layout2 = hv.Layout(plots, name=self.params.comparison_field).opts(shared_axes=False, 
                                                            tabs=self.params.tabs_switch, merge_tools=True\
                                                            ).cols(self.params.column_slider)
        else:
            self.layout2 = None

        try:
            tabs_title = os.path.split(str(self.params.comparison_file))[-1::][0]
        except:
            tabs_title = str(self.comparison_file)

        self.tabs2[0] = (tabs_title, self.layout2)
        self.plot_dict.update({'tabs2': self.tabs2})
    
    def set_diff_2d_plots(self, diff_opts):
        self.set_diff_xy(diff_opts)
        self.set_diff_yz(diff_opts)
        self.set_diff_tc(diff_opts)

    def set_diff_xy(self,diff_opts):
        """
        Set xy diff plot. 

        Parameters:
                diff_opts (dict): Options to apply to plot.

        Sets:
                xy_diff (list): list containing xy diff plots.
        """
        xy = []
        if 'xy' in self.params.plot_type.value:
            # for plot_kind in self.params.plot_kind.value:
            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(self.diff_data, 'xy', self.params.field, 
                                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2,), 
                                plot_kind, 
                                diff_opts)
                plot = self.create_overlay(plot)
                plot = plot.hist() if self.params.add_histo else plot
                xy.append(plot)
        self.xy_diff = xy

    def set_diff_tc(self,diff_opts):
        """
        Set xy diff plot. 

        Parameters:
                diff_opts (dict): Options to apply to plot.

        Sets:
                xy_diff (list): list containing xy diff plots.
        """
        tc = []
        if 'tc' in self.params.plot_type.value:
            d1 = self.tcd
            d2 = self.tcd2

            diff_data = self.get_diff_data(d1, d2)

            diff_opts['invert_xaxis'] = self.params.invert_xaxis
            diff_opts['invert_yaxis'] = self.params.invert_yaxis
            diff_opts['ylim'] = self.params.xy_ylim
            diff_opts['xlim'] = self.params.xy_xlim

            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(diff_data, 'xy', self.params.field,
                self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), 
                        plot_kind,
                        diff_opts)
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(diff_data.min().values), None))
                plot = plot.hist() if self.params.add_histo else plot
                tc.append(plot)
        self.tc_diff = tc

    def set_diff_yz(self,diff_opts):
        """
        Set yz diff plot. 

        Parameters:
                diff_opts (dict): Options to apply to plot.

        Sets:
                yz_diff (list): list containing yz diff plots.
        """
        yz = []
        if 'yz' in self.params.plot_type.value:
            d1 = self.zonal_data1
            d2 = self.zonal_data2

            zonal_diff_data = self.get_diff_data(d1, d2)

            diff_opts['invert_xaxis'] = self.params.invert_xaxis_z
            diff_opts['invert_yaxis'] = self.params.invert_yaxis_z
            diff_opts['ylim'] = self.params.yz_ylim
            diff_opts['xlim'] = self.params.yz_xlim

            # for plot_kind in self.params.plot_kind.value:
            for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                plot = self._plot(self.get_converter(zonal_diff_data, 'yz', self.params.field,
                        self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2,), 
                        plot_kind, 
                        diff_opts)
                if self.params.zonal_cnorm == 'log':
                    plot = plot.opts(clim=(float(zonal_diff_data.min().values), None))
                if self.config.trop_filename is not None:
                    plot = self.overlay_trop(plot)
                plot = plot.hist() if self.params.add_histo else plot
                yz.append(plot)
        self.yz_diff = yz

    def set_diff_1d_plots(self,field):
        img_opts = dict( 
                height=700, width=700, 
                tools=["hover"],
                fontsize={'title': '8pt'}, 
                title = " Left - Right " + f'{self.params.diff_types_1d}'
                )
        self.set_diff_ft(img_opts,field)
        self.set_diff_zt()

    def set_diff_ft(self,img_opts,field):
        """
        Set field/time diff plot. 

        Parameters:
                diff_opts (dict): Options to apply to plot.

        Sets:
                ft_diff (list): list containing ft diff plots.
        """
        ft = []
        if '1d' in self.params.plot_type.value:
            for plot_kind in self.get_1d_plot_types(self.params.plot_kind.value):
                if self.params.diff_types_1d == 'overlay':
                    plot = self._plot(self.get_converter(self.data_1, 'ft', self.params.field, 
                        self.params.xc, self.params.yc, self.params.tc, self.params.zc), plot_kind, 
                        img_opts) *\
                        self._plot(self.get_converter(self.data_2, 'ft', field, 
                        self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2), plot_kind, 
                        img_opts)
                elif self.params.diff_types_1d == 'align':
                    diff_data = xr.Dataset()
                    diff_data[self.params.field] = self.data2d
                    # diff_data[self.params.field+'_2'] = self.data_2
                    diff_data[self.params.comparison_field+'_2'] = self.data_2
                    plot = eval(f"diff_data.hvplot.{plot_kind}().opts(**img_opts)")
                else:
                    plot = self._plot(self.get_converter(self.diff_data, 'ft', field, 
                        self.params.xc, self.params.yc, self.params.tc, self.params.zc), plot_kind, img_opts)
                plot = plot.hist() if self.params.add_histo else plot
                ft.append(plot)
        self.ft_diff = ft

    def set_diff_zt(self):
        """
        Set zt diff plot. 

        Sets:
                zt_diff (list): list containing zt diff plots.
        """
        if 'zt' in self.params.plot_type.value:
            img_opts = self.get_zt_opts()
            d = self.get_diff_data(self.ztd.squeeze(), self.ztd2.squeeze())
            zt = self._plot(self.get_converter(d, 'zt', self.params.field, 
                        self.params.xc, self.params.yc, self.params.zc, self.params.tc), 'line', img_opts)
            self.zt_diff = zt

    @param.depends('params.tabs_switch', 'params.field', 'params.z', 'params.t', 'params.column_slider',
                   'params.color_levels', 'params.multi_file', 'params.logy_z', 'params.cnorm', 'params.show_grid',
                   'params.enable_projection.clicks', 'params.show_states', 'params.show_lakes', 'params.show_coastlines',
                   'params.diff_types', 'params.z2', 'params.t2', 'params.add_histo', 'params.plot_type.value',
                   'params.colorbar_position', 'params.tabs_switch', 'params.show_states', 'params.show_lakes', 
                   'params.apply_operation_button.clicks', 'params.zonal_cnorm', 'params.plot_kind.value', 
                   'params.comparison_field', 'params.diff_cmap', 'params.diff_types_1d')
    def make_differences(self):
        """
        Returns a pn.Tabs object with xy image, xy contours, and yz contours plots of the difference between the
        two files. Checks if regridding is needed between the files, and regrids if needed. Calculates difference,
        depending on difference type.

        Returns:
                diff_layout (pn.Tabs): Tabs panel object with difference plots.
        """
        if self.params.difference_button.clicks == 1:
            self.tabs_diff.loading = True
            d1 = self.data_1
            d2 = self.data_2

            d1_size = d1.shape
            d2_size = d2.shape  

            new_arr, regridded_dataset_number = du.get_regridded_ds(d1_size, d1, d2_size, d2)

            if regridded_dataset_number == 0:
                left_side = d1
                right_side = new_arr
            elif regridded_dataset_number == 1:
                left_side = new_arr
                right_side = d2
            elif regridded_dataset_number == 2:
                left_side = d1
                right_side = new_arr

            diff_data = self.get_diff_data(left_side, right_side)
            self.diff_data = diff_data

            diff_opts = self.get_diff_opts()

            if self.params.param.comparison_field.precedence == -1:
                plotval = self.params.field
            else:
                plotval = self.params.comparison_field

            self.set_diff_2d_plots(diff_opts)
            self.set_diff_1d_plots(plotval)

            self.tabs_diff.loading = False

            plot_list = [*self.xy_diff, *self.yz_diff, *self.tc_diff, self.zt_diff, *self.ft_diff]
            plots = self.create_plot_list(plot_list)

            self.layout_diff = hv.Layout(plots).opts(shared_axes=False, tabs=self.params.tabs_switch,
                                                     merge_tools=True).cols(self.params.column_slider)

        else:
            self.layout_diff = None
            zonal_ov = None

        self.tabs_diff[0] = ("Difference", self.layout_diff)
        self.plot_dict.update({'tabs_diff': self.tabs_diff})