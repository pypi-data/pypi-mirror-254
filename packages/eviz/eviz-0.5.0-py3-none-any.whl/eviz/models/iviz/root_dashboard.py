import holoviews as hv
import param
import panel as pn
import yaml
import os
import numpy as np

import geoviews as gv
import cartopy.crs as ccrs
import xarray as xr

import glob
from bokeh.models import FixedTicker

from eviz.lib.iviz.notyf import Notyf

import eviz.lib.iviz.dash_utils as du
from eviz.models.iviz.multi_file import MultiFile
from eviz.lib.iviz.config import configIviz
from eviz.lib.iviz import params_util

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
asialon = (50, 179)

auslat = (-60, 10)
auslon = (70, 179)

afrlat = (-40, 40)
afrlon = (-50, 90)


class RootDash(param.Parameterized):
    """ RootDash contains basic model-agnostic functions for preparing an iViz dashboard.

    Attributes:
            config (dict): Config class with file and data information.
            params (dict): Input class with Parameters, configured with yaml and/or input data attributes;
                            contains input data.
    """

    def __init__(self, config, params):
        self.config = config
        self.params = params

        self.cache_data()
        self._process_data()
        pn.Row(self.set_selected_data, self.select_comparison_file)

        self.tabs = pn.Tabs([], closable=True,
                             width=700
                            )
        self.tabs2 = pn.Tabs([], closable=True,
                             width=700
                             )
        self.tabs_diff = pn.Tabs([], closable=True,
                             width=700
                             )

        self.plot_dict = {}
        pn.Column(self.make_layout)
        self.plot_column = pn.Column(self.time_series_plot, 
                                       width=700,
                                       scroll=False)
        self.column = pn.Row(*list(self.plot_dict.values()), self.plot_column
                                )  # use self.column as the final object
        self.create_time_av()

        self.notyf = Notyf(types=[{"type": "error", "background": "red"}, {"type": "success", 
                            "background": "green"}],
                            duration=10000)
        super().__init__()

    def _process_data(self):
        pass

    @param.depends('params.multi_file', watch=True)
    def update_config(self):
        """
        Update config class and re-set to self.config if a file change is detected.

        Sets:
                self.config (dict): Config class initialized.
        """
        if self.config.file_dict is not None:
            if self.params.multi_file in list(self.config.file_dict.keys()):
                config_dict = {"files": self.params.file, "file_dict": self.config.file_dict,
                               "app_data": self.config.app_data, "specs_data": self.config.specs_data,
                               "is_yaml": self.config.is_yaml}
                vals = config_dict["file_dict"][self.params.multi_file]
                config_dict = {**config_dict, **vals}
                self.config = configIviz(**config_dict)

    @param.depends('params.multi_file')
    def cache_data(self):
        """
        Add the input xarray dataset to the Panel cache.

                Parameters:
                        file (xarray): xarray dataset.

                Cached:
                        file (xarray): xarray dataset.
        """
        if 'file' in pn.state.cache:
            if pn.state.cache['file'].equals(self.params.file):
                pass
            else:
                pn.state.cache['file'] = self.params.file
        else:
            pn.state.cache['file'] = self.params.file

    @param.depends('params.cmap_category', 'params.cmap_reverse', 'params.cmap_provider')
    def explore_cmaps(self):
        """
        Returns a Layout of hv.Images of possible colormaps, options filtered by the colormap category, provider,
        and reverse parameters. Filters through all colormaps with user input to select category, whether it's a
        reversed, and whether it's provided by matplotlib, bokeh, or colrocet. Sets the options of the filtered
        colormaps selector for the user to select a new colormap.

        Parameters:
                cmap_category (str): filter colormaps by category.
                cmap_reverse (bool): Whether to reverse the colormap.
                cmap_provider (str): Colormap provider.

        Returns:
                cmaps (hv.Layout): hv.Images depicting color ranges of available filtered colormaps.
        """
        if self.params.cmap_category == 'Diverging':
            cms = hv.plotting.list_cmaps(category='Diverging', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Rainbow':
            cms = hv.plotting.list_cmaps(category='Rainbow', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Categorical':
            cms = hv.plotting.list_cmaps(category='Categorical', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Miscellaneous':
            cms = hv.plotting.list_cmaps(category='Miscellaneous', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Uniform Sequential':
            cms = hv.plotting.list_cmaps(category='Uniform Sequential', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Mono Sequential':
            cms = hv.plotting.list_cmaps(category='Mono Sequential', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)
        elif self.params.cmap_category == 'Other Sequential':
            cms = hv.plotting.list_cmaps(category='Other Sequential', reverse=self.params.cmap_reverse,
                                         provider=self.params.cmap_provider)

        self.params.param.cmaps_available.objects = cms
        cmaps = du.cmap_examples(cms, self.params.cmap_provider, cols=6)

        return cmaps

    @param.depends('params.cmaps_available')
    def set_new_cmap(self):
        """
        Sets new colormap using selected colormap from explore colormaps in plot options tabs.
        """
        if self.params.cmaps_available is not None:
            self.params.param.cmap.objects.append(self.params.cmaps_available)
            self.params.param.set_param(cmap=self.params.cmaps_available)
        else:
            self.notyf.error(" Please select a colormap! ")


    @param.depends('params.apply_operation_button.clicks')
    def apply_operations_to_data(self, data):
        """
        Returns data with a basic operation applied to it based on user inputs. Multiply, divide, add,
        subtract factors extracted from the literal user input parameter.

        Parameters:
                data (xarray): xarray dataset to apply factor to.
                operations (str): what kind of operation to do: multiply, divide, add, subtract.

        Returns:
                title (str): Plot title.
        """
        if self.params.apply_operation_button.clicks:
            attrs = data.attrs
            if self.params.operations.value == 'multiply':
                data2 = data * self.params.lit_input.value
            elif self.params.operations.value == 'divide':
                data2 = data / self.params.lit_input.value
            elif self.params.operations.value == 'add':
                data2 = data + self.params.lit_input.value
            elif self.params.operations.value == 'subtract':
                data2 = data - self.params.lit_input.value
            data2.attrs = attrs
        else:
            data2 = data
        return data2

    def unit_conversion_check(self, data, field, config=None):
        """
        If input is a yaml configuratio with unitconversion specs available for the current field,
        apply conversion factor to data and return new data.

        Parameters:
                data (xarray): xarray dataset to get attributes from, including .name and .units.
                exp (str): experiment name, if available, from yaml configuration.
                zc (str): Input zc coordinate, will check to confirm in data, used for .units and .values.
                tc (str): Input tc coordinate, confirm in data, uses .name, .units, .values
        Returns:
                title (str): Plot title.
        """
        if self.config.is_yaml:
            if config is not None:
                config = config
            else:
                config = self.config
            try:
                cfg_var = config.specs_data[field]
                if 'unitconversion' in cfg_var:
                    newdata = data * float(cfg_var['unitconversion'])
                    newdata.attrs = data.attrs
                else:
                    newdata = data

                if ( 'units' in cfg_var ) and ( 'unitconversion' in cfg_var ):
                    newdata.attrs['units'] = cfg_var['units']
                else:
                    newdata.attrs['units'] = ''
            except Exception as e:
                self.logger.debug(f"{e}: Variable's spec information not found.")
                newdata = data
            if field.lower() == 'aoa':
                newdata = data / np.timedelta64(1, 'ns') / 1000000000 / 86400
                newdata.attrs = data.attrs
                newdata.attrs['units'] = 'days'
        else:
            if field.lower() == 'aoa':
                newdata = data / np.timedelta64(1, 'ns') / 1000000000 / 86400
                newdata.attrs = data.attrs
                newdata.attrs['units'] = 'days'
            else:
                newdata = data

        return newdata

    @param.depends('params.zoom_plot_button.clicks')
    def regional_selection(self):
        """
        Set the spatial extent, the ylim and xlim, of a plot, with current regional selection value. Available regions:
            global, north america, south america, europe, asia, australia and oceania, africa.

        Parameters:
                regions (str): user selected region to spatially select.
                xy_xlim (tuple): set parameter xy_xlim to selected region, the xlim of xy plot.
                xy_ylim (tuple): set parameter xy_ylim to selected region, the ylim of xy plot.
        """
        if self.params.zoom_plot_button.clicks:
            if self.params.regions == 'global':
                self.params.xy_xlim = self.params.globallons
                self.params.xy_ylim = self.params.globallats
                self.params.xy_xlim2 = self.params.globallons
                self.params.xy_ylim2 = self.params.globallats
            if self.params.regions == 'north america':
                self.params.xy_xlim = nalon
                self.params.xy_ylim = nalat
                self.params.xy_xlim2 = nalon
                self.params.xy_ylim2 = nalat
            if self.params.regions == 'south america':
                self.params.xy_xlim = salon
                self.params.xy_ylim = salat
                self.params.xy_xlim2 = salon
                self.params.xy_ylim2 = salat
            if self.params.regions == 'europe':
                self.params.xy_xlim = eulon
                self.params.xy_ylim = eulat
                self.params.xy_xlim2 = eulon
                self.params.xy_ylim2 = eulat
            if self.params.regions == 'asia':
                self.params.xy_xlim = asialon
                self.params.xy_ylim = asialat
                self.params.xy_xlim2 = asialon
                self.params.xy_ylim2 = asialat
            if self.params.regions == 'aus + oceania':
                self.params.xy_xlim = auslon
                self.params.xy_ylim = auslat
                self.params.xy_xlim2 = auslon
                self.params.xy_ylim2 = auslat
            if self.params.regions == 'africa':
                self.params.xy_xlim = afrlon
                self.params.xy_ylim = afrlat
                self.params.xy_xlim2 = afrlon
                self.params.xy_ylim2 = afrlat

    def get_clim(self, d1, d2):
        if self.params.share_colorbar and d2 is not None:
            clim = du.set_clim(d1, d2)
        else:
            clim = (None, None)
        if self.params.zero_clim:
            clim = (0, clim[1])

        return clim

    def get_ylim(self, d1, d2):
        if self.params.share_colorbar and d2 is not None:
            ylim = du.get_ylim(d1, d2)
            self.params.ymin = ylim[0]
            self.params.ymax = ylim[1]
        else:
            ylim = (None, None)
        return ylim

    def set_cformatter(self):
        if abs(float(self.data2d.max().values) - float(self.data2d.min().values)) <= 0.00001:
            self.formatter = '%.2e'
        elif abs(float(self.data2d.max().values) - float(self.data2d.min().values)) >= abs(9999.9):
            self.formatter = '%.1f'
        else:
            self.formatter = None

    def get_diff_data(self, left_side, right_side):
        if self.params.diff_types == 'difference':
            diff_data = abs(left_side - right_side)
        elif self.params.diff_types == 'percent difference':
            den = abs(left_side + right_side) / 2.0
            diff = abs(left_side - right_side)
            diff_data = abs(diff / den) * 100.
        elif self.params.diff_types == 'percent change':
            diff = abs(left_side - right_side)
            d = abs(diff / right_side)
            diff_data = abs(d * 100)
        elif self.params.diff_types == 'ratio':
            diff_data = abs(left_side / right_side)

        return diff_data

    def get_gen_opts(self, data):
        """
        Returns a dictionary of general plot options and settings applicable to all plots.

        Parameters:
                data (xarray): xarray dataset input to get attributes, .name and .units, from.
        Returns:
                img_opts (dict): Dictionary of plot options and settings, defaults and user parameters.
        """
        gen_opts = dict(padding=0, clabel=str(data.name) + " " + str(data.units), 
                        height=700, width=700, cformatter=self.formatter, 
                        tools=["hover"], colorbar_position=self.params.colorbar_position, toolbar='above',
                        fontsize={'title': '8pt'}, cnorm=self.params.cnorm, cmap=self.params.cmap,
                        alpha=self.params.alpha)
        return gen_opts

    def get_diff_opts(self):
        if self.params.diff_cmap is None:
            cmap = self.params.cmap
        else:
            cmap = self.params.diff_cmap
        diff_opts = dict(padding=0, xlim=self.params.xy_xlim, ylim=self.params.xy_ylim,
                        height=700, width=700, title='Left - Right ' + self.params.diff_types,
                        tools=["hover"], colorbar_position=self.params.colorbar_position, toolbar='above',
                        fontsize={'title': '8pt'}, cnorm=self.params.cnorm, cmap=cmap,
                        alpha=self.params.alpha, symmetric=True, invert_yaxis=self.params.invert_yaxis, 
                        invert_xaxis=self.params.invert_xaxis,
                        # title = " Left - Right " + f'{self.params.diff_types}'
                        )
        return diff_opts

    def get_xy_opts(self,data):
        gen_opts = self.get_gen_opts(data)
        xy_opts = dict(invert_yaxis=self.params.invert_yaxis, invert_xaxis=self.params.invert_xaxis, 
                        xlim=self.params.xy_xlim, ylim=self.params.xy_ylim,
                        clim=self.clim)
        opts = {**gen_opts, **xy_opts}

        return opts

    def get_yz_opts(self,data):
        """
        Returns a dictionary of plot options and settings.

        Parameters:
                data (xarray): xarray dataset input to get attributes, .name and .units, from.
        Returns:
                img_opts (dict): Dictionary of plot options and settings, defaults and user parameters.
        """
        gen_opts = self.get_gen_opts(data)
        yz_opts = dict(logy=self.params.logy_z, invert_xaxis=self.params.invert_xaxis_z,
                        invert_yaxis=self.params.invert_yaxis_z, ylim=self.params.yz_ylim,
                        xlim=self.params.yz_xlim)
        opts = {**gen_opts, **yz_opts}

        return opts

    def get_zt_opts(self):
        img_opts = {
            'invert_axes': self.params.profile_invert_axes, 
            'invert_yaxis': self.params.profile_invert_yaxis, 
            'logy': self.params.profile_logy, 
            'height': 600, 
            'width': 700, 
            'title': 'vertical profile'
        }
        return img_opts

    def zonal_title(self, data, exp_name):
        """
        Returns a zonal title based off the input data, experiment name if available, or if
        the user has selected a custom title, title input will come from title_input widget.

                Parameters:
                        data (xarray): xarray dataset to get attributes from, including .name and .units.
                        exp_name (str): experiment name, if available, from yaml configuration.
                Returns:
                        zonal_title (str): Plot title.
        """
        # if hasattr(data, 'long_name'):
            # pass
        # else:
            # data.attrs['long_name'] = data.name

        if hasattr(data, 'units'):
            pass
        else:
            data.attrs['units'] = ''

        
        if exp_name is not None:
            zonal_title = self.params.title_input.value + " Zonal Mean " if self.params.custom_title else str(
                    exp_name) + " " + str(
                    data.name) +  " " + str(
                    data.units) + " Zonal Mean"
        else:
            zonal_title = self.params.title_input.value + " Zonal Mean " if self.params.custom_title else str(
                    data.name) +  " " + str(
                    data.units) + " Zonal Mean"

        return zonal_title

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

        if len(str(data[tc].values)) > 19:
            timestr = str(data[tc].values)[0:19]
        else:
            timestr = str(data[tc].values)

        if exp is not None:
            if zc in list(data.coords):
                if hasattr(data[zc], 'units'):
                    pass
                else:
                    data[zc].attrs['units'] = ''
                title = self.params.title_input.value if self.params.custom_title else (str(exp) + ': ' + str(data.name) +
                                                                                " " + str(data.units) + " @ " + str(
                            data[zc].values) + " " + str(data[zc].units) + " " + timestr)
            elif tc in list(data.coords):
                title = self.params.title_input.value if self.params.custom_title else (str(exp) + ': ' + str(data.name) +
                                                                                " " + str(data.units) + " " + timestr)
            else:
                title = self.params.title_input.value if self.params.custom_title else (str(exp) + ': ' + str(data.name) +
                                                                                " " + str(data.units))
        else:
            if zc in list(data.coords):
                if hasattr(data[zc], 'units'):
                    pass
                else:
                    data[zc].attrs['units'] = ''
                title = self.params.title_input.value if self.params.custom_title else (str(data.name) + " " +
                                                                                str(data.units) + " @ " + str(
                            data[zc].values) + " " + str(data[zc].units) + " " + timestr)
            elif tc in list(data.coords):
                title = self.params.title_input.value if self.params.custom_title else (str(data.name) + " " +
                                                                                str(data.units) + " " + timestr)
            else:
                title = self.params.title_input.value if self.params.custom_title else (str(data.name) + " " +
                                                                                str(data.units))                
        return title

    @param.depends('params.show_data', 'params.multi_file', watch=True)
    def data_show(self):
        """
        Returns an interactive Panel pane of current Xarray Dataset.

                Returns:
                        pane (panel): Panel pane of an interactive Xarray dataset.
        """
        if self.params.show_data:
            self.plot_dict['data'] = pn.Column(self.params.file)
            self.column.objects = list(self.plot_dict.values())
        else:
            self.plot_dict.pop('data', None)
            self.column.objects = list(self.plot_dict.values())

    @param.depends('params.t', 'params.field', 'params.show_statistics', 'params.z', 'params.multi_file',
                   'params.apply_operation_button.clicks', watch=True)
    def statistics_box(self):
        """
        Calculates basic statistics (median, mean, min, max, std), formats and creates a panel Markdown
        object, which is appended to the side of the main column.

        Returns:
                column (list): A formatted box of basic statistics.
        """
        if self.params.show_statistics:
            data = self.data2d

            # Get rounded statistics
            mean = data.mean().round(3).values
            max_ = data.max().round(3).values
            min_ = data.min().round(3).values
            std = data.std().round(3).values
            med = data.median().round(3).values

            # Sci notation formatting
            if mean == 0.0:
                mean = '{:0.3e}'.format(data.mean().values)
            if max_ == 0.0:
                max_ = '{:0.3e}'.format(data.max().values)
            if min_ == 0.0:
                min_ = '{:0.3e}'.format(data.min().values)
            if std == 0.0:
                std = '{:0.3e}'.format(data.std().values)
            if med == 0.0:
                med = '{:0.3e}'.format(data.median().values)
            stats_box = pn.pane.Markdown("""
    ###### <div align="center">  Mean:  {}  <br />  Median: {} <br />  Max:  {}  <br />  Min:  {}  <br />  Std:  {}  </div> </font>
            """.format(
                str(mean), str(med), str(max_), str(min_), str(std)), style={'font-family': "Times New Roman",
                                                                             'color': '#92a8d1'}, align='center',
                width=200, background='#1B345C')
            self.plot_dict['stats_box'] = stats_box
            self.column.objects = list(self.plot_dict.values())
        else:
            self.plot_dict.pop('stats_box', None)
            self.column.objects = list(self.plot_dict.values())

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
            img_opts = self.get_xy_opts(data)
            proj_str = self.params.proj
            proj_method = getattr(ccrs, proj_str)
            filename = self.filename()

            if self.params.gif_dim.value == self.params.zc:
                data3d = eval(f"data.isel({self.params.tc}=self.params.t)")
            elif self.params.gif_dim.value == self.params.tc:
                if self.params.zc is not None:
                    data3d = eval(f"data.isel({self.params.zc}=self.params.z)")
                else:
                    data3d = data
            if self.params.enable_projection.clicks:
                plot = data3d.hvplot.contourf(x=self.params.xc, y=self.params.yc, cmap=self.params.cmap, crs=ccrs.PlateCarree(),
                                     projection=self.get_cartopy_projection(data3d[self.params.xc],
                                     data3d[self.params.yc]),
                                     levels=self.params.color_levels,
                                     project=True, xlim=self.params.xy_xlim,
                                     coast=True,
                                     ylim=self.params.xy_ylim, cnorm=self.params.cnorm, dynamic=False).opts(
                    # clabel=str(data3d.name) + " " + str(data3d.units), 
                    cformatter=self.formatter,
                    framewise=False,
                    rasterize=True, )
            else:
                plot = data3d.hvplot.contourf(x=self.params.xc, y=self.params.yc, cmap=self.params.cmap, cnorm=self.params.cnorm,
                                     xlim=self.params.xy_xlim, ylim=self.params.xy_ylim,
                                     # rasterize=True,
                                     coastline=True,
                                     levels=self.params.color_levels,
                                     dynamic=False).opts(
                                        # clabel=str(data3d.name) + " " + str(data3d.units),
                                                        #  cformatter=self.formatter,
                                                         framewise=True)

            if self.config.output_dir is not None:
                output_dir = self.config.output_dir
            else:
                output_dir = os.getcwd()
            filepath = os.path.join(output_dir, filename)

            if self.params.show_coastlines:
                proj_str = self.params.proj
                proj_method = getattr(ccrs, proj_str)
                coast = gv.feature.coastline().opts(projection=self.get_cartopy_projection(
                                     data3d[self.params.xc], data3d[self.params.yc]), 
                                     xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)
                border = gv.feature.borders().opts(projection=self.get_cartopy_projection(
                                     data3d[self.params.xc], data3d[self.params.yc]), 
                                     xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)
                borders = coast * border
                giffer = hv.Overlay(plot * borders).collate()  # .opts(framewise=True)
                gif = hv.save(giffer, f'{filepath}.gif', fmt='gif', fps=2, toolbar=False)
            else:
                gif = hv.save(plot, f'{filepath}.gif', fmt='gif', fps=2, toolbar=False)
            self.params.progressbar.visible = False
            self.notyf.success(" Gif saved! ")
            # return gif         

    def get_cartopy_projection(self, x, y):
        """
        Check if cartopy projection has central_longitude or central_latitude parameters, use
        x and y median value of data if found. 

        Parameters:
                x (xarray): Input x values from data
                y (xarray): Input y values from data
        Returns:
                projection (ccrs): cartopy projection.
        """
        x_med = float(x.median().values)
        y_med = float(y.median().values)

        proj = getattr(ccrs, self.params.proj)
        from inspect import signature
        sig = signature(proj)
        if 'central_longitude' and 'central_latitude' in sig.parameters:
            projection = proj(central_longitude=x_med, central_latitude=y_med)
        else: #only go here if there isn't both 
            if 'central_longitude' in sig.parameters:
                projection = proj(central_longitude=x_med)
            else:
                projection = proj()
        return projection

    @param.depends('params.proj', 'params.xy_xlim', 'params.xy_ylim', 'params.enable_projection.clicks',
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
        features = [self.params.show_coastlines, self.params.show_states, self.params.show_lakes, self.params.show_grid]
        if plot is not None:
            if any(features):
                proj_str = self.params.proj
                proj_method = getattr(ccrs, proj_str)
                coast = gv.feature.coastline(scale=self.params.cartopy_feature_scale).apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc])
                            )
                border = gv.feature.borders(scale=self.params.cartopy_feature_scale).apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc])
                            )
                borders = coast * border
                lakes = gv.feature.lakes(scale=self.params.cartopy_feature_scale).apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc]), fill_color='#2251dd'
                            )
                rivers = gv.feature.rivers(scale=self.params.cartopy_feature_scale).apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc]), line_color='#2251dd')
                states = gv.feature.states(scale=self.params.cartopy_feature_scale).apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc]), 
                            fill_alpha=0, line_color='gray', line_width=0.6)
                grid = gv.feature.grid().apply.opts(
                            projection=self.get_cartopy_projection(self.data2d[self.params.xc],
                            self.data2d[self.params.yc]), 
                            line_color='black')

                borders = borders.apply.opts(xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)
                lakes = lakes.apply.opts(xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)
                rivers = rivers.apply.opts(xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)
                states = states.apply.opts(xlim=self.params.xy_xlim, ylim=self.params.xy_ylim)

                if 'coastlines' in pn.state.cache:
                    pass
                else:
                    pn.state.cache['borders'] = borders

                if 'states' in pn.state.cache:
                    pass
                else:
                    pn.state.cache['states'] = states

                if 'lakes' in pn.state.cache:
                    pass
                else:
                    pn.state.cache['lakes'] = lakes

                if 'rivers' in pn.state.cache:
                    pass
                else:
                    pn.state.cache['rivers'] = rivers

                plot_features = [plot]

                if self.params.show_coastlines:
                    plot_features.append(pn.state.cache['borders'])
                if self.params.show_states:
                    plot_features.append(pn.state.cache['states'])
                if self.params.show_rivers:
                    plot_features.append(pn.states.cache['rivers'])
                if self.params.show_lakes:
                    plot_features.append(pn.state.cache['lakes'])
                if self.params.show_grid:
                    plot_features.append(grid)

                overlay = hv.Overlay([f for f in plot_features]).collate() if plot is not None else None
            else:
                overlay = plot
        else:
            overlay = None

        return overlay

    @param.depends('params.field', 'params.z', 'params.t', 'params.zero_clim', 'params.color_levels')
    def colorbar_ticks(self, img, data, begin=None, end=None):
        """
        Returns a Bokeh Fixed Ticker object, containing tick locations for a plots colorbar. Calculated
        from inputs, plot range, and number of color levels.

        Parameters:
                img (plot): Input Holoviz plot
                begin (float): If provided, value to use as first tick mark.
                end (float): If provided, value to use as last tick mark.

        Returns:
                ticker: Bokeh fixed ticker.
        """
        # ticker = None
        # if float(data.min().values) != 0.0:
        # reset_output()
        try:
            info = img.vdims[0]
            r = info.range
        except:
            r = (float(data.min().values), float(data.max().values))

        try:
            if begin is None:
                begin = r[0]
            else:
                begin = begin

            if end is None:
                end = r[1]
            else:
                end = end
            if self.params.zero_clim:
                if begin == 0.0:
                    pass
                else:
                    begin = 0.0
            sub = end - begin
            cl = sub / self.params.color_levels

            ticks = [begin]
            for i in du.frange(begin, end, cl):
                ticks.append(i)

            ticks.append(end)
            ticker = FixedTicker(ticks=ticks)
            return ticker
        except Exception as e:
            self.logger.error(f"{e}: Could not create colorbar tick marks")
            ticker = FixedTicker()
            return ticker
            # ticker = FixedTicker()
        # return ticker


    def create_plot_list(self, plot_list):
        """
        Returns a list of plots that are not empty. 

        Parameters:
                plot_list (list): All possible plots in a layout.

        Returns:
                plots (list): list of plots that are not empty.
        """
        plots = []
        for p in plot_list:
            if p is not None:
                plots.append(p)
            else:
                pass
        return plots

    def add_plot_histogram(self, plot):
        """
        Add a histogram to all plots in a list.

        Parameters:
                plot (list): All plots to add a histogram.

        Returns:
                newplots (list): List of plots with histograms.
        """
        newplots = []
        for p in plot:
            plot_histogram = p.hist() 
            newplots.append(plot_histogram)
        return newplots

    @pn.depends('params.gif_dim.value')
    def get_player(self):
        """
        Returns a media player, with play, pause, next, back, controls, that can animate or step
        through time or vertical levels.

        Returns:
                player (pn.widgets.Player): A media player widget from Panel.
        """
        player = pn.widgets.Player.from_param(
            self.params.param.z if self.params.gif_dim.value == 'level' and self.params.zc in list(
                self.data4d.coords) else self.params.param.t, step=1, margin=(5, 10))
        return player

    def filename(self):
        """
        Create a filename to write a gif or layout to file.

        Returns:
                filename (str): filename of saved object
        """
        if self.params.zc in list(self.data2d.coords):
            filename = str(str(self.params.field) + "_" + str(self.data2d[self.params.zc].values))
        else:
            filename = str(self.params.field)
        return filename

    @pn.depends('params.save_menu_button.clicked')
    def save_layout(self):
        """
        Saves the current entire tool view (stored as 'column') to the output directory, which is 
        either configured with yaml or the current working directory. Format type of the saved plots 
        determined by user input, save_menu_button.

        Parameters:
                output_dir (str): Configured with YAML or current working directory.
                save_menu_button (event): Button that includes further menu options with save formats.
        """
        if self.params.save_menu_button.clicked:
            try:
                filename = self.filename()
                if self.config.output_dir is not None:
                    output_dir = self.config.output_dir
                else:
                    output_dir = os.getcwd()

                if os.path.exists(output_dir):
                    pass
                else:
                    os.makedirs(output_dir)

                filepath = os.path.join(output_dir, filename)
                if self.params.save_menu_button.clicked == 'png':
                    from bokeh.io import export_png
                    self.params.tabs_switch = False
                    row = pn.Row(*list(self.plot_dict.values()))
                    root = row.get_root()
                    filename = filepath + '.png'
                    export_png(root, filename=filename)
                    self.notyf.success(f" Layout saved at {filename} ")
                    self.params.save_menu_button.clicked = None
                else:
                    self.column.save(f"{filepath}.{self.params.save_menu_button.clicked}")
                    self.notyf.success(f" Layout saved at {filepath}")
                    self.params.save_menu_button.clicked = None
                # from bokeh.io import curdoc
                # curdoc().clear()
                # curdoc()
                # reset_output()
            except Exception as e:
                self.logger.error(f"{e}: Issue saving layout")
                self.notyf.error(f'Layout not saved! {e}')

    @pn.depends('params.save_session_button.clicks')
    def save_session(self):
        """
        Saves the user's current session by getting the value of all params and params_const values. Created a dictionary of
        those settings, and saving as a YAML file to the current working directory.

        Outputs:
                session_file (yaml): YAML dictionary containing all params values of current session.
        """
        if self.params.save_session_button.clicks:
            params = self.params.param.get_param_values()
            if self.params.plot_second_file_button.clicks >= 1:
                params.append(('plot_second_file_button.clicks', 1))
            if self.params.clear_button.clicks >= 1:
                params.append(('clear_button.clicks', 1))
            if self.params.difference_button.clicks >= 1:
                params.append(('difference_button.clicks', 1))
            if self.params.clear_diff_button.clicks >= 1:
                params.append(('clear_diff_button.clicks', 1))
            if self.params.gif_button.clicks >= 1:
                params.append(('gif_button.clicks', 1))
            if self.params.apply_operation_button.clicks >= 1:
                params.append(('apply_operation_button.clicks', 1))
            if self.params.zoom_plot_button.clicks >= 1:
                params.append(('zoom_plot_button.clicks', 1))
            if self.params.save_menu_button.clicked:
                params.append(('save_menu_button.clicked', self.save_menu_button.clicked))
            if self.params.enable_projection.clicks >= 1:
                params.append(('enable_projection.clicks', 1))
            if self.params.add_plots_button.clicks >= 1:
                params.append(('add_plots_button.clicks', 1))
            if self.params.add_time_series_plot_btn.clicks >= 1:
                params.append(('add_time_series_plot_btn.clicks', 1))

            params.append(('differencing_toggle', self.params.differencing_toggle.value))
            params.append(('animate_toggle', self.params.animate_toggle.value))
            params.append(('second_file_input', self.params.second_file_input.value))
            params.append(('title_input', self.params.title_input.value))
            params.append(('operations', self.params.operations.value))

            params.append(('invert_yaxis', self.params.invert_yaxis))
            params.append(('invert_xaxis', self.params.invert_xaxis))
            params.append(('invert_yaxis_z', self.params.invert_yaxis_z))
            params.append(('invert_xaxis_z', self.params.invert_xaxis_z))
            params.append(('alpha', self.params.alpha))
            
            params.append(('yz_ylim.value.1', float(self.params.yz_ylim[0])))
            params.append(('yz_ylim.value.2', float(self.params.yz_ylim[1])))
            params.append(('yz_xlim.value.1', float(self.params.yz_xlim[0])))
            params.append(('yz_xlim.value.2', float(self.params.yz_xlim[1])))
            params.append(('xy_ylim.value.1', float(self.params.xy_ylim[0])))
            params.append(('xy_ylim.value.2', float(self.params.xy_ylim[1])))
            params.append(('xy_xlim.value.1', float(self.params.xy_xlim[0])))
            params.append(('xy_xlim.value.2', float(self.params.xy_xlim[1])))
            params.append(('xy_ylim2.value.1', float(self.params.xy_ylim2[0])))
            params.append(('xy_ylim2.value.2', float(self.params.xy_ylim2[1])))
            params.append(('plot_type.value', self.params.plot_type.value))
            params.append(('plot_kind.value', self.params.plot_kind.value))

            dct_params = dict((x, y) for x, y in params)

            from datetime import datetime
            now = datetime.now()
            now = now.strftime("%d.%m.%Y_%H:%M:%S")
            session_file = now + '.' + 'iViz_session.yaml'

            with open(session_file, 'w') as file:
                documents = yaml.dump(dct_params, file)
            self.notyf.success(" Session file saved! ")

    @pn.depends('params.save_plot_opts_button.clicks')
    def save_plot_opts(self):
        """
        Saves the user's current plot options by getting the value of corresponding params and params_const values. 
        Created a dictionary of those settings, and saving as a YAML file to the current working directory.

        Outputs:
                plot_options (yaml): YAML dictionary containing all params values of currently applied plot options.
        """
        if self.params.save_plot_opts_button.clicks:
            params = self.params.param.get_param_values()
            dct_params = dict((x, y) for x, y in params)

            dct = {**dct_params, 'invert_yaxis_z': self.params.invert_yaxis_z,
                   'invert_xaxis_z': self.params.invert_xaxis_z, 'invert_yaxis': self.params.invert_yaxis,
                   'invert_xaxis': self.params.invert_xaxis, 'alpha': self.params.alpha,
                   'custom_title': self.params.custom_title, 'tabs_switch': self.params.tabs_switch,
                   'color_levels': self.params.color_levels, 'title_input': self.params.title_input}

            plot_opt_keys = ['show_coastlines', 'show_lakes', 'show_states', 'show_data', 'custom_title', 'tabs_switch',
                             'column_slider', 'show_grid', 'color_levels', 'cnorm', 'zonal_cnorm', 'zero_clim',
                             'share_colorbar', 'regions', 'zoom', 'logy_z',
                             'invert_yaxis_z', 'invert_xaxis_z', 'invert_yaxis',
                             'invert_xaxis',
                             'proj', 'diff_types', 'add_trop', 'add_histo', 'alpha', 'cmap']

            plot_opts_subset = {key: dct[key] for key in plot_opt_keys}
            with open(r'plot_options.yaml', 'w') as file:
                documents = yaml.dump(plot_opts_subset, file)
            self.notyf.success(" Plot options file saved! ")

    @pn.depends('params.add_files_button.clicks', watch=True)
    def add_files(self):
        """
        Adds files being explored with the multi_selector to the current files available in the file selector.

        Returns:
                files (str): New files parameter with updated files available.
        """
        if self.params.add_files_button.clicks == 1:
            if len(self.params.multi_selector.value) >= 1:

                new_files = self.params.multi_selector.value
                all_files = self.params.param.multi_file.objects + new_files

                self.params.param.multi_file.objects = all_files
                self.notyf.success(" Files added! ")
                self.params.add_files_button.clicks = 0

    @pn.depends('params.add_to_tabs_btn.clicks')
    def add_to_tabs(self):
        """
        Adds the current plots to the main tabs object so that a user can refer to plots they've already created without saving.
        """
        if self.params.add_to_tabs_btn.clicks:
            self.tabs.append(self.layout)

    @pn.depends('params.differencing_toggle.value')
    def do_diff(self):
        """
        Returns a panel Column with the differencing workflow widgets when toggled by the user, otherwise empty. Includes the 
        directory input, the files found in the directory, a selector for the diff types, and buttons that add the second file, 
        clear the second file, add the difference plots, and clear the difference plots.

        Returns:
                diff_pane : A panel Column with differencing widgets.
        """
        if self.params.differencing_toggle.value:
            diff_pane = pn.Row(
                pn.Column(self.params.second_file_input, self.params.param.comparison_file, self.params.param.comparison_source,
                         self.set_comparison_file),
                pn.Column(self.params.plot_second_file_button, self.params.clear_button, self.params.difference_button,
                          self.params.clear_diff_button, margin=(15, 0)))
        elif not self.params.differencing_toggle.value:
            diff_pane = None
        return diff_pane

    @pn.depends('params.explore_files.value', 'params.add_plots_button.clicks')
    def do_explorer(self):
        if self.params.explore_files.value:
            modal = pn.Column(self.params.multi_selector, 
                              self.params.add_plots_button, 
                              self.params.add_files_button, 
                              pn.Row(self.params.param.all_variables,
                                    self.params.variable_input, width=400),
                              self.params.run_time_avg_btn, 
                              self.params.add_time_series_plot_btn, 
                            #   self.add_files, self.run_multi,
                              width=550)
        elif not self.params.explore_files.value:
            modal = None
        return modal

    @pn.depends('params.animate_toggle.value')
    def animate(self):
        """
        Returns a panel WidgetBox with the widgets for creating a gif when toggled by the user, otherwise empty. Includes a 
        selector of the available dimensions to animate over, and a gif button.

        Returns:
                gif_pane : A panel with gif widgets.
        """
        if self.params.animate_toggle.value:
            gif_pane = pn.WidgetBox(self.params.gif_dim, self.params.gif_button, self.gif, width=200)  # self.get_player)
        elif not self.params.animate_toggle.value:
            gif_pane = None
        return gif_pane

    @pn.depends('params.add_plots_button.clicks', watch=True)
    def run_multi(self):
        """
        Creates mini visualization tool using MultiFile class for each file selected in the multiple file selector. Creates xy 
        image, xy contours, and yz contours plots, arranged in a pn.Tabs object, and with corresponding widgets. Appends the 
        result to the layout tabs object. Triggered user clicking add_plots_button.
        """
        if self.params.add_plots_button.clicks:
            objs = []
            for file in self.params.multi_selector.value:
                classes = MultiFile(file, self.params.model, name='')

                spacer = pn.Row(pn.Spacer(background='#FFFFFF', sizing_mode='stretch_both', height=5, width=200))

                options = pn.Tabs(
                    ("Plot", pn.WidgetBox(classes.param.show_grid, classes.param.color_levels, classes.param.cnorm,
                                          background='#0A1832')),
                    ("Zonal",
                     pn.WidgetBox(classes.param.invert_zonal_x, classes.param.invert_zonal_y, classes.param.logy,
                                  background='#0A1832')),
                    ("Title", pn.WidgetBox(classes.param.custom_title, classes.text_input, background='#0A1832')))
                dims = pn.WidgetBox(pn.Column(classes.param.plot, classes.param.z, classes.param.t, classes.param.cmap,
                                              pn.Row(classes.param.show_data, classes.param.show_statistics, width=310),
                                              pn.Row(classes.param.tabs_switch, classes.param.show_coastlines,
                                                     width=310), width=320), background='#0A1832')
                rows = pn.Row(classes.tabs, pn.Column(spacer, dims, options),
                              pn.Column(classes.statistics_box, classes.data_show), name=file)
                objs.append(rows)

            pnls = []
            for o in objs:
                pnls.append(pn.panel(o))

            for i in range(len(pnls)):
                self.tabs.append(pnls[i])  # appends to the object which is filling into the tabs Layout

    def plot_type_tabs(self):
        """
        Returns panel tabs with different plot types widgets. 

        Returns:
                plot_type_tabs (pn.Tabs): tabs containing plot type widgets. 
        """
        plot_type_tabs = pn.Tabs(('XY', pn.Column(#self.params.plot_kind_2d, 
                                    pn.Row(self.params.param.clim, self.params.param.set_xy_clim),
                                    self.params.param.xy_ylim, self.params.param.xy_xlim,
                                    self.params.param.xy_ylim2, self.params.param.xy_xlim2,
                                    self.params.param.invert_yaxis, self.params.param.invert_xaxis,
                                    self.params.param.cnorm, width=450)),
                ('YZ', pn.Column(#self.params.plot_kind_2d, 
                                    pn.Row(self.params.param.zonal_clim, self.params.param.set_yz_clim),
                                    self.params.param.yz_ylim,
                                    self.params.param.yz_xlim,
                                    self.params.param.add_trop, self.params.param.trop_field,
                                    self.params.param.logy_z, self.params.param.invert_yaxis_z,
                                    self.params.param.invert_xaxis_z,
                                    self.params.param.zonal_cnorm, width=450)), 
                ('Diff', pn.Column(self.params.param.diff_cmap, self.params.param.diff_types)),
                # ('Field avg', self.params.param.plot_by),
                ('1d', pn.Column(self.params.param.diff_types_1d, self.params.param.plot_by, self.params.param.avg_by_lev)),
                ('Polar', pn.Column(#self.params.plot_kind_2d, 
                          self.params.polar_projection, self.params.param.polar_central_longitude, 
                          self.params.param.polar_coastlines)), 
                ('Profile', pn.Column(self.params.plot_kind_profile, self.params.param.profile_invert_yaxis, 
                                      self.params.param.profile_invert_axes, 
                                      self.params.param.profile_logy)), 
                # ('Hov Mollar')
                width=550)
        return plot_type_tabs

    def plot_opts(self):
        """
        Returns a panel Tabs object with all the available plot options and parameters controlling visualizations.

        Returns:
                plot_opts_tabs : A panel with plot options widgets.
        """
        plot_opts_tabs = pn.Tabs(('Plot type + Settings', pn.Column(self.params.plot_type, self.params.plot_kind, 
                                                                    self.params.param.alpha,
                                                                    self.params.param.color_levels, 
                                                                    self.params.param.show_grid,
                                                                    self.params.param.custom_title, 
                                                                    self.params.title_input,
                                                                    self.params.param.column_slider,
                                                                    self.params.param.show_coastlines,
                                                                    self.params.param.show_states,
                                                                    self.params.param.show_lakes,
                                                                    self.params.param.show_rivers,
                                                                    self.params.param.cartopy_feature_scale)),

                                 ('Axes + Colorbar',
                                  pn.Column(self.params.param.colorbar_position, self.params.param.share_colorbar,
                                            self.params.param.zero_clim,
                                            self.plot_type_tabs(),
                                            width=400
                                            )),
                                 ('Explore colormaps',
                                  pn.Column(self.params.param.cmap_category, self.params.param.cmap_provider,
                                            self.params.param.cmap_reverse, self.explore_cmaps,
                                            self.params.param.cmaps_available, self.set_new_cmap)),
                                 ('Advanced',
                                  pn.Column(self.params.lit_input, self.params.operations, self.params.apply_operation_button,
                                            self.regional_selection, self.params.param.regions, self.params.zoom_plot_button,
                                            self.params.param.proj, self.params.enable_projection)),
                                width=500,
                                scroll=False,
                                 margin=(0, 20),
                                 sizing_mode='stretch_width'
                                 )
        return plot_opts_tabs

    @pn.depends('params.plot_second_file_button.clicks')
    def plot_second(self):
        """
        When the "Add secondary plot" button is clicked, run the second_tabs function and append the results to the plot panel.
        """
        if self.params.plot_second_file_button.clicks:
            if self.params.comparison_file == None:
                self.notyf.error(" Please select a file! ")
            else:
                pn.Row(self.make_second_layout)
                self.column.objects = list(self.plot_dict.values())

    @pn.depends('params.clear_button.clicks')
    def clear_second(self):
        """
        When 'Clear secondary plot' is clicked, clear the second_tabs result from the main plot panel. Remove the secondary plot
        widgets, and re-set relevant class variables to None.
        """
        if self.params.clear_button.clicks:
            if self.params.comparison_file:
                self.plot_dict.pop('tabs2', None)
                self.column.objects = list(self.plot_dict.values())
                self.params.param.t2.precedence = -1
                self.params.param.comparison_field.precedence = -1
                self.params.param.z2.precedence = -1
                self.layout2 = None
                self.data_2 = None 
                self.zonal_clim = (None,None)
                self.clim = (None, None)
                self.params.comparison_file = None
                self.params.plot_second_file_button.clicks = 0
            else:
                self.notyf.error(" No secondary file to clear! ")

    @pn.depends('params.difference_button.clicks')
    def plot_difference(self):
        """
        When 'Add difference plots' is clicked, run the difference_plots function and append the results to the main plot panel.
        """
        if self.params.difference_button.clicks:
            if self.params.comparison_file:
                pn.Row(self.make_differences)
                self.column.objects = list(self.plot_dict.values())
            else:
                self.notyf.error(" Please select a secondary file first! ")

    @pn.depends('params.clear_diff_button.clicks')
    def clear_diff(self):
        """
        When 'Clear difference plot' is clicked, clear the difference_plots result from the main plot panel. Re-set relevant 
        class variables to None.
        """
        if self.params.clear_diff_button.clicks:
            if self.layout_diff is not None:
                self.plot_dict.pop('tabs_diff', None)
                self.column.objects = list(self.plot_dict.values())
                self.image_diff = None
                self.params.difference_button.clicks = 0
                self.zonal_ov = None
                self.layout_diff = None
            else:
                self.notyf.error(" No differences to clear! ")
