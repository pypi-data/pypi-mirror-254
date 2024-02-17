import os
import hvplot.pandas
import hvplot.xarray
import panel as pn
import holoviews as hv
import glob
import param
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
from eviz.lib.iviz import params_util as params_util
from .tabular_dashboard import TabularDash
from eviz.lib.iviz.config import configIviz
import eviz.lib.iviz.dash_utils as du
from ...lib.data.data_selector import DataSelector

import eviz.lib.const as constants

hv.extension('bokeh')
pn.extension()

class AirNowDash(TabularDash):

    """
    EPA AirNow Observations interactive visualization dashboard 
    """

    def __init__(self, config, params):
        super().__init__(config=config, params=params)


    def slice_cf_data(self, cf_data):
        lonrange=[-130,-60]
        latrange=[24,52]

        cfsel = eval(f"cf_data.sel({self.params.xc2}=slice(lonrange[0], lonrange[1]),{self.params.yc2}=slice(latrange[0], latrange[1]))")
        return cfsel

    def getCFatEPASites(self, ObsData, CFData):
        """
        Function to get CF data at EPA sites

        Inputs:
            ObsData (pandas dataframe):
                Output of the getEPAData function
            CFData (xarray dataarray):
                CF output read in through getCFaqcData

        Outputs:
        pandas dataframe with the CF forecast added

        """    

        oLon  = ObsData.Longitude
        oLat  = ObsData.Latitude

        CFatObs = []    
        for lon,lat in zip(oLon,oLat):
            CFatObs.append(CFData.sel(lat=lat, lon=lon,method='nearest'))

        df = pd.DataFrame()
        df['Longitude'] = oLon
        df['Latitude'] = oLat
        df[self.params.comparison_field] = np.array(CFatObs)

        return df

    def drop_nas(self, data):
        selds = data.query('Status=="Active" & '
                                     '10<Latitude<60 & '
                                     '-135<Longitude<-60'
                                    )
        selds=selds.sort_values(by=['AQSID','time'])
        selds=selds.set_index(['time','AQSID'])
        selds = selds[[self.params.field, 'Longitude', 'Latitude']].to_xarray()
        selds = selds.rolling(time=8, min_periods=6).mean('time').max('time')
        selds = selds.dropna(dim='AQSID')
        selds = selds.to_dataframe()
        return selds

    @param.depends('params.zero_clim', 'params.show_grid', 'params.field',
                   'params.show_grid', 'params.column_slider', 'params.show_coastlines', 'params.tabs_switch', 
                   'params.enable_basemap', 'params.basemap', 'params.xc', 'params.yc',
                   'params.colorbar_position', 'params.show_states', 'params.show_lakes', 
                   'params.enable_projection.clicks', 'params.clim_min', 'params.clim_max',
                   'params.show_rivers', 'params.add_histo', 'params.share_colorbar', 'params.clim_min', 
                   'params.cartopy_feature_scale', 'params.size',
                   'params.clim_max', 'params.apply_operation_button.clicks', 'params.plot_type.value',
                   'params.custom_title', 'params.plot_kind.value',
                   'params.title_input.value', 'params.profile_invert_yaxis', )
    def make_layout(self):
        """
        Makes a hv.Layout with xy image, xy contours, and yz contours plot. Embeds in self.tabs pn.Tabs object defined
        in __init__. Returns new self.tabs.

        Returns:
                self.tabs (pn.Tabs): returns pn.Tabs object with embedded Layout.
        """
        self.tabs.loading = True
        if self.params.field is not None:
            data2d = self.drop_nas(self.params.file)
        else:
            data2d = self.params.file

        self.data2d = data2d
        self.data_1 = self.data2d

        if self.params.share_colorbar and self.data_2 is not None:
            self.clim = du.set_clim(self.data_1[self.params.field], self.data_2[self.params.comparison_field], 
                            self.params.clim_min, self.params.clim_max)
        else:
            self.clim = (None, None)
        if self.params.zero_clim:
            self.clim = (0, None)            

        opts = {
                'width': 700, 
                'height': 500, 
                'alpha': self.params.alpha,
                'invert_yaxis': self.params.invert_yaxis, 
                'invert_xaxis': self.params.invert_xaxis,
                'cmap': self.params.cmap,
                'show_grid': self.params.show_grid,
                'size': self.params.size,
                'clim': self.clim
                }

        if self.params.enable_basemap:
            converter = hvplot.HoloViewsConverter(data2d, self.params.xc, self.params.yc, c=self.params.field,
                                        geo=True, 
                                        colorbar=True, title=self.title_function(self.params.field),
                                        legend=self.params.colorbar_position,
                                        **opts
                                        )
        else:
            converter = hvplot.HoloViewsConverter(data2d, self.params.xc, self.params.yc, c=self.params.field,
                                        colorbar=True, 
                                        title=self.title_function(self.params.field),
                                        legend=self.params.colorbar_position,
                                        **opts
                                        )

        xy = []
        for plot_kind in self.params.plot_kind.value:
            plot = self._plot(converter, plot_kind)
            plot = self.create_overlay(plot)
            if self.params.cnorm == 'log':
                plot = plot.opts(clim=(float(data2d[self.params.field].min().values), self.clim[1]))
            plot = plot.hist() if self.params.add_histo else plot
            xy.append(plot)
        self.xy = xy

        self.tabs.loading = False

        plot_list = [*self.xy]
        plots = self.create_plot_list(plot_list)

        layout = hv.Layout(plots, name=f'{self.params.field}').opts(shared_axes=False, tabs=self.params.tabs_switch,
                                                                   # sizing_mode='fixed',
                                                                   merge_tools=True).cols(self.params.column_slider)

        self.layout = layout
        self.tabs[0] = (self.params.set_input(), layout)
        self.plot_dict.update({'tabs1': self.tabs})

    def set_file2_param_values(self, file):
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
        coords = params_util.get_coords(file)
        ndims = params_util.get_ndims(file)
        dims = params_util.get_dims(file)
        model = params_util.get_model_type(coords)  # get type of model dims, str of 2nd file
        self.params.xc2, self.params.yc2, self.params.tc2, self.params.zc2 = self.params.set_xarray_dim_params(
            model=model,
            xc=self.params.xc2, yc=self.params.yc2, tc=self.params.tc2, zc=self.params.zc2)


    @param.depends('params.comparison_file', 'params.second_file_input.value')
    def set_file2_params(self, file1, file2):
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
        # file1_coords = params_util.get_coords(file1)
        file2_coords = params_util.get_coords(file2)

        self.set_file2_param_values(
            file=file2)  # by running this all the xc2, yc2, zc2, and tc2 values are set according to the determined model type

        times = len(list(file2[self.params.tc2].values))
        end_t = times - 1
        bounds_t = (0, end_t)
        if bounds_t == (0, 0):
            pass
        else:
            self.params.param.t2.bounds = bounds_t
            self.params.param.t2.precedence = +1

        timeval = self.params.t2

        if self.params.zc2 is not None:
            if self.params.zc2 in file2_coords:
                self.params.z2 = 0
                length = len(list(file2[self.params.zc2].values))
                if length > 1:
                    end_l = length - 1
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

    @param.depends('params.share_colorbar', 'params.show_grid', 'params.comparison_field', 'params.field', 
                   'params.title_input.value', 'params.custom_title', 'params.show_coastlines', 'params.z2',
                   'params.t2', 'params.tabs_switch', 'params.column_slider', 'params.size',
                   'params.zero_clim', 'params.show_states', 'params.show_lakes', 
                   'params.zero_clim', 'params.enable_basemap', 'params.basemap',
                   'self.params.plot_kind.value', 'params.add_histo', 'params.apply_operation_button.clicks', 
                   'params.plot_type.value', 'params.colorbar_position')
    def make_second_layout(self):
        """
        Returns a pn.Tabs object with xy image, xy contours, and yz contours plot for the secondary file selected.

        Returns:
                tabs2 (pn.Tabs): Tabs panel object with plots for second file.
        """
        if self.params.field is not None:
            self.tabs2.loading = True
            if self.params.plot_second_file_button.clicks == 1:
                comparison_file = DataSelector(self.params.comparison_file, 'cf').data
                self.config_dir = constants.config_path
                specs_path = os.path.join(self.config_dir, 'cf/cf_specs.yaml')

                if self.config.file_dict is not None:
                    if self.params.comparison_file in list(self.config.file_dict.keys()):
                        file_dict = {"files": self.params.comparison_file, "file_dict": self.config.file_dict,
                                    "app_data": self.config.app_data}
                        v = file_dict["file_dict"][self.params.comparison_file]
                        file_dict = {**file_dict, **v}
                        config = configIviz(specs_path, **file_dict)
                    else:
                        file_dict = {'files': self.params.comparison_file}
                        config = configIviz(specs_path, **file_dict)
                else:
                    file_dict = {'files': self.params.comparison_file}
                    config = configIviz(specs_path, **file_dict)

                timeval, levval = self.set_file2_params(file1=self.params.file, file2=comparison_file)
                try:
                    comparison_file[self.params.tc2] = comparison_file[self.params.tc2].dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    try:
                        comparison_file[self.params.tc2] = pd.DatetimeIndex(self.file[self.tc].values)
                        comparison_file[self.params.tc2] = comparison_file[self.params.tc2].dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        self.logger.info("Could not format time dimension labels")

                self.comparison_file = comparison_file

                file1_keys = params_util.get_keys(self.params.file)
                file2_keys = params_util.get_keys(self.comparison_file)

                if file2_keys != file1_keys:
                    self.params.param['comparison_field'].objects = file2_keys
                    self.params.param['comparison_field'].precedence = +1
                    if self.params.comparison_field is None or self.params.comparison_field not in file2_keys:
                        self.params.param.set_param(comparison_field=file2_keys[0])
                elif file2_keys == file1_keys:
                    self.params.comparison_field = self.params.field

                data4d_2 = self.comparison_file[self.params.comparison_field]
                self.data4d_2 = data4d_2

                file2_coords = params_util.get_coords(data4d_2)

                # Scenario for if they're different model types
                if self.params.zc2 in file2_coords and self.params.tc2 in file2_coords:
                    data2d_2 = eval(f"data4d_2.isel({self.params.zc2}=levval, {self.params.tc2}=timeval)")
                elif self.params.tc2 in file2_coords:
                    data2d_2 = eval(f"data4d_2.isel({self.params.tc2}=timeval)")
                else:
                    data2d_2 = data4d_2  # no time or lev values, just lat/lon and variable

                data2d_2 = self.slice_cf_data(data2d_2)
                data2d_2 = self.getCFatEPASites(self.data2d, data2d_2)
                data2d_2 = self.unit_conversion_check(data2d_2, self.params.comparison_field, config=config)
                data2d_2 = self.apply_operations_to_data(data2d_2)

                # Colorbar ranges
                self.data_2 = data2d_2

                if self.params.share_colorbar:
                    self.params.clim_min, self.params.clim_max = du.set_clim(self.data_1[self.params.field], 
                                            self.data_2[self.params.comparison_field], 
                                            self.params.clim_min, 
                                            self.params.clim_max)
                    self.clim = (self.params.clim_min, self.params.clim_max)
                else:
                    self.clim = (None, None)

                if self.params.zero_clim:
                    self.clim = (0, self.clim[1])

                # img_opts = self.get_img_opts(data4d_2)
                self.data_2 = data2d_2

                # proj_str = self.params.proj
                # proj_method = getattr(ccrs, proj_str)
                title = "CF at EPA Observations "
                # title = self.title_function(self.data_2, config.exp_name, self.params.zc2, self.params.tc2)

                opts = {
                        'width': 700, 
                        'height': 500, 
                        'alpha': self.params.alpha,
                        'invert_yaxis': self.params.invert_yaxis, 
                        'invert_xaxis': self.params.invert_xaxis,
                        'cmap': self.params.cmap,
                        'show_grid': self.params.show_grid,
                        'size': self.params.size, 
                        'clim': self.clim
                        }

                if self.params.enable_basemap:
                    converter = hvplot.HoloViewsConverter(self.data_2, self.params.xc, self.params.yc,
                            c=self.params.comparison_field, geo=True,
                            colorbar=True, crs=ccrs.PlateCarree(),
                            title=self.title_function(self.params.comparison_field), 
                            legend=self.params.colorbar_position, 
                            **opts)                
                else:
                    converter = hvplot.HoloViewsConverter(self.data_2, self.params.xc, self.params.yc,
                            c=self.params.comparison_field, 
                            colorbar=True,
                            title=self.title_function(self.params.comparison_field), 
                            legend=self.params.colorbar_position, 
                            **opts)

                xy = []
                for plot_kind in self.params.plot_kind.value:
                    plot = self._plot(converter, plot_kind)
                    plot = self.create_overlay(plot)
                    if self.params.cnorm == 'log':
                        plot = plot.opts(clim=(float(self.data_2[self.params.comparison_field].min().values), 
                                            self.clim[1]))
                    plot = plot.hist() if self.params.add_histo else plot
                    xy.append(plot)
                self.xy2 = xy

                self.tabs2.loading = False

                plot_list = [*self.xy2]
                plots = self.create_plot_list(plot_list)
                self.layout2 = hv.Layout(plots, name=self.params.comparison_field).opts(shared_axes=False, tabs=self.params.tabs_switch,
                                                                merge_tools=True).cols(self.params.column_slider)

            else:
                self.layout2 = None

            try:
                tabs_title = os.path.split(str(self.params.comparison_file))[-1::][0]
            except:
                tabs_title = str(self.params.comparison_file)
            self.tabs2[0] = (tabs_title, self.layout2)
            self.plot_dict.update({'tabs2': self.tabs2})

        else:
            self.params.plot_second_file_button.clicks = 0
            self.notyf.error(" Please select a field before adding CF data! ")
    
        
    @param.depends('params.tabs_switch', 'params.field', 'params.z', 'params.t', 'params.column_slider',
                   'params.show_grid', 'params.size',
                   'params.enable_projection.clicks', 'params.show_states', 'params.show_lakes', 'params.show_coastlines',
                   'params.diff_types', 'params.z2', 'params.t2', 'params.add_histo', 'params.plot_type',
                   'params.colorbar_position', 'params.tabs_switch', 'params.show_states', 'params.show_lakes', 
                   'params.apply_operation_button.clicks',)
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
            opts = {
                    'width': 700, 
                    'height': 500, 
                    'alpha': self.params.alpha,
                    'invert_yaxis': self.params.invert_yaxis, 
                    'invert_xaxis': self.params.invert_xaxis,
                    'colorbar': True,
                    'show_grid': self.params.show_grid,
                    'symmetric': True
                    }

            left = self.data_1[self.params.field]
            right = self.data_2[self.params.comparison_field]

            # Define self.data_1['diff'] depending on what type of difference is selected
            if self.params.diff_types == 'difference':
                self.data_1['diff'] = abs(left - right)
            elif self.params.diff_types == 'percent difference':
                den = abs(left + right) / 2.0
                diff = abs(left - right)
                self.data_1['diff'] = abs(diff / den) * 100.
            elif self.params.diff_types == 'percent change':
                diff = abs(left - right)
                d = abs(diff / right)
                self.data_1['diff'] = abs(d * 100)
            elif self.params.diff_types == 'ratio':
                self.data_1['diff'] = abs(left / right)

            title = " Left - Right " + f'{self.params.diff_types}'

            opts['cmap'] = self.params.cmap
            opts['invert_yaxis'] = self.params.invert_yaxis
            opts['invert_xaxis'] = self.params.invert_xaxis
            opts['alpha'] = self.params.alpha
            opts['symmetric'] = True
            opts['size'] = self.params.size

            if self.params.enable_basemap:
                converter = hvplot.HoloViewsConverter(self.data_1, self.params.xc, self.params.yc, 
                        c='diff', geo=True, title=title, legend=self.params.colorbar_position, 
                        **opts)
            else:
                converter = hvplot.HoloViewsConverter(self.data_1, self.params.xc, self.params.yc, 
                        c='diff', title=title, legend=self.params.colorbar_position, **opts)

            xy = []
            if 'xy' in self.params.plot_type.value:
                for plot_kind in self.params.plot_kind.value:
                    plot = self._plot(converter, plot_kind)
                    plot = self.create_overlay(plot)
                    plot = plot.hist() if self.params.add_histo else plot
                    xy.append(plot)
            self.xy_diff = xy

            self.tabs_diff.loading = False

            plot_list = [*self.xy_diff]
            plots = self.create_plot_list(plot_list)

            self.layout_diff = hv.Layout(plots).opts(shared_axes=False, tabs=self.params.tabs_switch,
                                                     merge_tools=True).cols(self.params.column_slider)

        else:
            self.layout_diff = None
            zonal_ov = None

        self.tabs_diff[0] = ("Difference", self.layout_diff)
        self.plot_dict.update({'tabs_diff': self.tabs_diff})