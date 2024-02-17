import holoviews as hv
import param
import panel as pn
import logging
import hvplot.xarray
import hvplot.pandas

import geoviews as gv

from eviz.models.iviz.base_dashboard import BaseDash

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


class TabularDash(BaseDash):
    """ The TabularDash class represents an interactive visualization dashboard for tabular data (rows,columns) 
    in the form of a pandas Dataframe. 

    Attributes:
            config (dict): Config class with file and data information.
            params (dict): Input class with Parameters, configured with yaml and/or input data attributes;
                            contains input data.
    """
    logger = logging.getLogger(__name__)

    def __init__(self, config, params):
        super().__init__(config=config, params=params)

    @param.depends()
    def set_selected_data(self):
        pass

    @param.depends()
    def select_comparison_file(self):
        pass

    def create_time_av(self):
        pass    
    
    def title_function(self, field):
        title = self.params.title_input.value if self.params.custom_title else field
        return title

    def _process_data(self):
        pass

    def cache_data(self):
        pass

    def set_plot_types_on_var_change(self):
        pass

    def filename(self):
        """
        Create a filename to write a gif or layout to file.

        Returns:
                filename (str): filename of saved object
        """
        return str(self.params.field)

    def set_input(self):
        """
        Create a filename to write a gif or layout to file.

        Returns:
                filename (str): filename of saved object
        """
        return self.params.dataInput

    @param.depends('params.show_data', 'params.file', watch=True)
    def data_show(self):
        """
        Returns an interactive Panel pane of current Xarray Dataset.

        Returns:
                pane (panel): Panel pane of an interactive Xarray dataset.
        """
        if self.params.show_data:
            self.plot_dict['data'] = pn.pane.HTML(self.params.file)
            self.column.objects = list(self.plot_dict.values())
        else:
            self.plot_dict.pop('data', None)
            self.column.objects = list(self.plot_dict.values())

    @param.depends('params.describe', watch=True)
    def describe_data(self):
        if self.params.describe:
            self.plot_dict['describe_data'] = pn.pane.HTML(self.params.file.describe())
            self.column.objects = list(self.plot_dict.values())
        else:
            self.plot_dict.pop('describe_data', None)
            self.column.objects = list(self.plot_dict.values())

    @param.depends('params.t', 'params.field', 'params.show_statistics', 'params.z', 'params.file',
                   'params.apply_operation_button.clicks', watch=True)
    def statistics_box(self):
        """
        Calculates basic statistics (median, mean, min, max, std), formats and creates a panel Markdown
        object, which is appended to the side of the main column.

        Returns:
                column (list): A formatted box of basic statistics.
        """
        if self.params.show_statistics:

            if self.params.field is not None:
                data = self.data2d[self.params.field]
            else:
                self.notyf.error( " Please select a field! ")

            # Get rounded statistics
            mean = data.mean().round(3)
            max_ = data.max().round(3)
            min_ = data.min().round(3)
            std = data.std().round(3)
            med = data.median().round(3)

            # Sci notation formatting
            if mean == 0.0:
                mean = '{:0.3e}'.format(data.mean())
            if max_ == 0.0:
                max_ = '{:0.3e}'.format(data.max())
            if min_ == 0.0:
                min_ = '{:0.3e}'.format(data.min())
            if std == 0.0:
                std = '{:0.3e}'.format(data.std())
            if med == 0.0:
                med = '{:0.3e}'.format(data.median())
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

    def create_overlay(self, plot):
        features = [self.params.show_coastlines, self.params.show_states, self.params.show_lakes, 
                    self.params.show_grid, self.params.enable_basemap]
        if plot is not None:
            if any(features):
                coast = gv.feature.coastline(scale=self.params.cartopy_feature_scale).apply.opts(
                            )
                border = gv.feature.borders(scale=self.params.cartopy_feature_scale).apply.opts(
                            )
                borders = coast * border
                lakes = gv.feature.lakes(scale=self.params.cartopy_feature_scale).apply.opts(
                            )
                rivers = gv.feature.rivers(scale=self.params.cartopy_feature_scale).apply.opts(
                            )
                states = gv.feature.states(scale=self.params.cartopy_feature_scale).apply.opts(
                            fill_alpha=0, line_color='gray', line_width=0.6)
                grid = gv.feature.grid().apply.opts(
                            line_color='black')
                basemap = eval(f"gv.tile_sources.{self.params.basemap}()")

                plot_features = [plot]

                if self.params.show_coastlines:
                    plot_features.append(borders)
                if self.params.show_states:
                    plot_features.append(states)
                if self.params.show_rivers:
                    plot_features.append(rivers)
                if self.params.show_lakes:
                    plot_features.append(lakes)
                if self.params.show_grid:
                    plot_features.append(grid)
                if self.params.enable_basemap:
                    plot_features.append(basemap)

                overlay = hv.Overlay([f for f in plot_features]).collate() 
            else:
                overlay = plot
        else:
            overlay = None
        
        return overlay

    @param.depends('params.show_grid', 'params.field', 'params.column_slider', 
                    'params.show_coastlines', 'params.tabs_switch', 
                   'params.enable_basemap', 'params.basemap', 'params.xc', 'params.yc',
                   'params.colorbar_position', 'params.show_states', 'params.show_lakes', 
                   'params.enable_projection.clicks', 'params.show_rivers', 'params.add_histo', 
                   'params.cartopy_feature_scale', 'params.size',
                   'params.apply_operation_button.clicks', 'params.plot_type.value',
                   'params.custom_title', 'params.plot_kind.value',
                   'params.title_input.value', 'params.profile_invert_yaxis')
    def make_layout(self):
        """
        Makes a hv.Layout with xy image, xy contours, and yz contours plot. Embeds in self.tabs pn.Tabs object defined
        in __init__. Returns new self.tabs.

        Returns:
                self.tabs (pn.Tabs): returns pn.Tabs object with embedded Layout.
        """
        self.tabs.loading = True

        opts = {
                'width': 700, 
                'height': 500, 
                'alpha': self.params.alpha,
                'invert_yaxis': self.params.invert_yaxis, 
                'invert_xaxis': self.params.invert_xaxis,
                'cmap': self.params.cmap,
                'show_grid': self.params.show_grid
                }

        if self.params.enable_basemap:
            converter = hvplot.HoloViewsConverter(self.params.file, self.params.xc, self.params.yc, c=self.params.field,
                                            geo=True, size=self.params.size,
                                            colorbar=True, title=self.title_function(self.params.field),
                                            legend=self.params.colorbar_position, 
                                            **opts
                                            )
        else:
            converter = hvplot.HoloViewsConverter(self.params.file, self.params.xc, self.params.yc, c=self.params.field,
                                            colorbar=True, size=self.params.size, 
                                            title=self.title_function(self.params.field),
                                            legend=self.params.colorbar_position,
                                            **opts
                                            )



        xy = []
        for plot_kind in self.params.plot_kind.value:
            plot = self._plot(converter, plot_kind, opts)
            if self.params.cnorm == 'log':
                plot = plot.opts(clim=(float(self.params.file[self.params.field].min().values), self.clim[1]))
            plot = plot.hist() if self.params.add_histo else plot
            plot = self.create_overlay(plot)
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

    def plot_opts(self):
        """
        Returns a panel Tabs object with all the available plot options and parameters controlling visualizations.

        Returns:
                plot_opts_tabs : A panel with plot options widgets.
        """
        # plot_type = pn.Param(self.params.param, parameters=['plot_type'], widgets={
            # 'plot_type': {'type': pn.widgets.MultiChoice}})
        plot_opts_tabs = pn.Tabs(('Plot type + Settings', pn.Column(self.params.plot_type, self.params.plot_kind, 
                                                                    self.params.param.alpha, self.params.param.size,
                                                                    self.params.param.show_grid,
                                                                    self.params.param.describe,
                                                                    self.params.param.custom_title, self.params.title_input,
                                                                    self.params.param.column_slider,
                                                                    pn.Row(self.params.param.basemap, self.params.param.enable_basemap, 
                                                                            width=475),
                                                                    self.params.param.show_coastlines,
                                                                    self.params.param.show_states,
                                                                    self.params.param.show_lakes,
                                                                    self.params.param.show_rivers,
                                                                    self.params.param.cartopy_feature_scale)),
                                 # self.params.explore_files_button, self.params.save_session_button, self.params.save_plot_opts_button)),
                                 ('Axes + Colorbar',
                                  pn.Column(self.params.param.colorbar_position, self.params.param.share_colorbar,
                                            self.params.param.zero_clim,
                                            pn.Tabs(('XY', pn.Column(self.params.param.invert_yaxis, 
                                                                     self.params.param.invert_xaxis,
                                                                     )),
                                                    ('Zonal', pn.Column(self.params.param.invert_yaxis_z,
                                                                        self.params.param.invert_xaxis_z,
                                                                        ))),
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
