import os
import logging
from typing import Any

import matplotlib.figure
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib import gridspec
from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1 import make_axes_locatable
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.gridspec as mgridspec
import numpy as np
from matplotlib.transforms import BboxBase as bbase
from matplotlib.ticker import MultipleLocator

import eviz.lib.xarray_utils as xu
import eviz.lib.eviz.plot_utils as pu

from dataclasses import dataclass, field

from eviz.lib.eviz.config import Config


@dataclass
class Figure:
    """ This class acts like Matplotlib's Figure but customized for the eViz framework.
        Parameters:

        config (Config) :
            Representation of the model configuration used to specify data sources and
            user choices for the map generation. The config instance is created at the
            application level.

    Note:
        Frame defines an internal state with figure and axes option.
    """
    config: Config
    plot_type: str
    mfig: matplotlib.figure.Figure = None
    axes: Any = None
    _gs: gridspec.GridSpec = None
    _rindex: int = 0
    _ax_opts: dict = field(default_factory=dict)
    _frame_params: dict = field(default_factory=dict)
    _subplots: tuple = (1, 1)
    _use_cartopy: bool = False

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.debug("Create figure, axes")
        if self.config.add_logo:
            self.EVIZ_LOGO = plt.imread('eviz/lib/_static/ASTG_logo.png')  # 240x225x4

        self._init_frame()
        self.fig, self.axes = self._get_fig_ax()

    def create_subplot_grid(self):
        fig = plt.figure(figsize=(self._frame_params[self._rindex][2], self._frame_params[self._rindex][3]))
        gs = gridspec.GridSpec(*self._subplots)
        return fig, gs

    def create_subplots(self, gs):
        if self._use_cartopy:
            return self.create_subplots_crs(gs)
        else:
            axes = []
            for i in range(self._subplots[0]):
                for j in range(self._subplots[1]):
                    ax = plt.subplot(gs[i, j])
                    axes.append(ax)
            return axes

    def create_subplots_crs(self, gs):
        axes = []
        for i in range(self._subplots[0]):
            for j in range(self._subplots[1]):
                ax = plt.subplot(gs[i, j], projection=ccrs.PlateCarree())
                axes.append(ax)
                # Add gridlines
                gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
                gl.xlabels_top = False
                gl.ylabels_right = False
                gl.xformatter = LONGITUDE_FORMATTER
                gl.yformatter = LATITUDE_FORMATTER
                ax.coastlines()
                ax.add_feature(cfeature.BORDERS, linestyle=':')
                ax.add_feature(cfeature.LAND, edgecolor='black')
                ax.add_feature(cfeature.LAKES, edgecolor='black')
        return axes

    def get_gs_geometry(self):
        if self.gs:
            return self.gs.get_geometry()
        else:
            return None

    def have_multiple_axes(self):
        return self.axes is not None and (self.axes.numRows > 1 or self.axes.numCols > 1)

    def have_nontrivial_grid(self):
        return self.gs.nrows > 1 or self.gs.ncols > 1

    @staticmethod
    def show():
        plt.show()

    def _init_frame(self):
        """ Get shape and geometry for each figure frame """
        self._init_subplots()
        # TODO: clean up
        _frame_params = {}
        rindex = 0
        _frame_params[rindex] = list()
        if self.config.compare:
            if self._subplots == (3, 1):
                _frame_params[rindex] = [3, 1, 8, 12]  # nrows, ncols, width, height
            elif self._subplots == (2, 2):
                _frame_params[rindex] = [2, 2, 12, 8]
        else:
            if self._subplots == (1, 1):
                _frame_params[rindex] = [1, 1, 8, 8]
            elif self._subplots == (2, 1):
                _frame_params[rindex] = [2, 1, 8, 10]
            elif self._subplots == (3, 1):
                _frame_params[rindex] = [3, 1, 8, 12]
            elif self._subplots == (2, 2):
                _frame_params[rindex] = [2, 2, 14, 10]
            elif self._subplots == (3, 4):
                _frame_params[rindex] = [3, 4, 12, 16]
        self._frame_params = _frame_params

    def _init_subplots(self):
        """ Get subplots for each frame """
        _subplots = (1, 1)
        try:
            extra_diff_plot = self.config.extra_diff_plot
            if not self.config.compare:
                extra_diff_plot = False
            if self.config.spec_data and extra_diff_plot:
                _subplots = (2, 2)
            else:
                _subplots = (1, 1)
        except Exception as e:
            self.logger.warning(f"key error: {str(e)}, returning default")
        finally:
            if self.config.compare and not self.config.extra_diff_plot:
                _subplots = (3, 1)
        self._subplots = _subplots

    @staticmethod
    def add_grid(ax, lines=True, locations=None):
        """Add a grid to the current plot.

        Parameters:
            ax (Axis): axis object in which to draw the grid.
            lines (bool, optional): add lines to the grid. Defaults to True.
            locations (tuple, optional):
                (xminor, xmajor, yminor, ymajor). Defaults to None.
        """
        if lines:
            ax.grid(lines, alpha=0.5, which="minor", ls=":")
            ax.grid(lines, alpha=0.7, which="major")

        if locations is not None:
            assert (
                    len(locations) == 4
            ), "Invalid entry for the locations of the markers"

            xmin, xmaj, ymin, ymaj = locations

            ax.xaxis.set_minor_locator(MultipleLocator(xmin))
            ax.xaxis.set_major_locator(MultipleLocator(xmaj))
            ax.yaxis.set_minor_locator(MultipleLocator(ymin))
            ax.yaxis.set_major_locator(MultipleLocator(ymaj))

    def _get_fig_ax(self):
        """ Initialize figure and axes objects for all plots based on plot type

        Returns:
            fig (Figure) : figure object for the given plot type
            ax (Axes) : Axes object for the given plot type
        """
        use_cartopy_opt = False
        if 'yz' in self.plot_type:
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        elif 'xt' in self.plot_type:
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        elif 'tx' in self.plot_type:
            use_cartopy_opt = True
            self._use_cartopy = True
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        elif 'po' in self.plot_type:
            use_cartopy_opt = True
            self._use_cartopy = True
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        elif 'sc' in self.plot_type:
            use_cartopy_opt = True
            self._use_cartopy = True
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        else:  # 'xy' only
            use_cartopy_opt = True
            self._use_cartopy = True
            fig, axtemp = self._set_fig_axes_global(use_cartopy_opt=use_cartopy_opt)
        if isinstance(axtemp, list) and len(axtemp) == 1:
            ax = axtemp[0]
        else:
            ax = axtemp
        return fig, ax

    def get_fig_ax(self):
        return self.mfig, self.axes

    def _set_fig_axes_regional(self, use_cartopy_opt):
        pass

    def _set_fig_axes_global(self, use_cartopy_opt):
        """ Helper function to instantiate figure and axes objects """
        map_projection = ccrs.PlateCarree()
        if 'projection' in self._ax_opts:
            map_projection = self.get_projection(self._ax_opts['projection'])

        # Default
        fig, gs = self.create_subplot_grid()
        axes = self.create_subplots(gs)

        if "tx" in self.plot_type:
            fig = plt.figure(figsize=(self._frame_params[self._rindex][2], self._frame_params[self._rindex][3]))
            gs = mgridspec.GridSpec(nrows=2, ncols=1, height_ratios=[1, 6], hspace=0.05)
            axes = list()
            axes.append(fig.add_subplot(gs[0, 0], projection=map_projection))
            axes.append((fig.add_subplot(gs[1, 0])))
        elif "xt" in self.plot_type:
            axes = plt.subplot(gs[0, 0])
        # elif "sc" in self.plot_type:
        #     axes = plt.subplot(gs[0, 0])
        else:
            if self.config.add_logo:
                fig = plt.figure()
                fig.set_figwidth(self._frame_params[self._rindex][2])
                fig.set_figheight(self._frame_params[self._rindex][3])
                gs = gridspec.GridSpec(2, 2, width_ratios=[1, 10], height_ratios=[10, 1], wspace=0.05, hspace=0.05)
                axes = gs.figure.axes[0]
                return fig, axes
        self.gs = gs
        return fig, axes

    def init_ax_opts(self, field_name):
        """ Initialize map options for a given field, using specs data or some sensible defaults.

        Parameters:
            field_name (str) : File name whose axes options need to be initialized

        Returns:
            Updated axes internal state
        """
        single_ax_opts = dict()
        plot_type = self.plot_type[0:2]

        # # Process single-axes options
        if plot_type == "po":
            plot_type = "polar"  # TODO: recheck this?!

        single_ax_opts['boundary'] = None
        if 'pole' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['boundary'] = self.config.spec_data[field_name][plot_type + 'plot']['boundary']

        single_ax_opts['use_pole'] = 'north'
        if 'pole' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['use_pole'] = self.config.spec_data[field_name][plot_type + 'plot']['pole']

        single_ax_opts['profile_dim'] = None
        if 'profile_dim' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['profile_dim'] = self.config.spec_data[field_name][plot_type + 'plot']['profile_dim']

        single_ax_opts['zave'] = None
        if 'zave' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['zave'] = self.config.spec_data[field_name][plot_type + 'plot']['zave']

        single_ax_opts['tave'] = None
        if 'tave' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['tave'] = self.config.spec_data[field_name][plot_type + 'plot']['tave']

        single_ax_opts['taverange'] = 'all'
        if 'taverange' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['taverange'] = self.config.spec_data[field_name][plot_type + 'plot']['taverange']

        single_ax_opts['use_cmap'] = self.config.cmap
        if 'cmap' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['use_cmap'] = self.config.spec_data[field_name][plot_type + 'plot']['cmap']

        single_ax_opts['use_diff_cmap'] = self.config.cmap
        if 'diff_cmap' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['use_diff_cmap'] = self.config.spec_data[field_name][plot_type + 'plot']['diff_cmap']

        single_ax_opts['cscale'] = None
        if 'cscale' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['cscale'] = self.config.spec_data[field_name][plot_type + 'plot']['cscale']

        single_ax_opts['zscale'] = 'log'
        if 'zscale' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['zscale'] = self.config.spec_data[field_name][plot_type + 'plot']['zscale']

        single_ax_opts['add_grid'] = False
        if 'grid' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['add_grid'] = self.config.spec_data[field_name][plot_type + 'plot']['grid']

        single_ax_opts['line_contours'] = True
        if 'line_contours' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['line_contours'] = self.config.spec_data[field_name][plot_type + 'plot']['line_contours']

        single_ax_opts['add_tropp_height'] = False
        if 'add_tropp_height' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['add_tropp_height'] = self.config.spec_data[field_name][plot_type + 'plot'][
                'add_tropp_height']

        single_ax_opts['torder'] = None
        if 'torder' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['torder'] = self.config.spec_data[field_name][plot_type + 'plot']['torder']

        # Reset spec value if no file was provided
        # if not self.config.get_use_trop_field():
        #     single_ax_opts['add_tropp_height'] = False

        single_ax_opts['use_cartopy'] = False
        if 'use_cartopy' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['use_cartopy'] = self.config.spec_data[field_name][plot_type + 'plot']['use_cartopy']

        single_ax_opts['projection'] = None
        if 'projection' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['projection'] = self.config.spec_data[field_name][plot_type + 'plot']['projection']

        single_ax_opts['extent'] = []
        if 'extent' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['extent'] = self.config.spec_data[field_name][plot_type + 'plot']['extent']
        else:
            single_ax_opts['extent'] = [-180, 180, -90, 90]

        # Used in regional models:
        single_ax_opts['central_lon'] = 0.0
        single_ax_opts['central_lat'] = 0.0

        single_ax_opts['num_clevs'] = 10
        if 'num_clevs' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['num_clevs'] = self.config.spec_data[field_name][plot_type + 'plot']['num_clevs']

        single_ax_opts['time_lev'] = 0
        if 'time_lev' in self.config.spec_data[field_name][plot_type + 'plot']:
            single_ax_opts['time_lev'] = self.config.spec_data[field_name][plot_type + 'plot']['time_lev']

        # Initialize single-axes defaults
        single_ax_opts['is_diff_field'] = False
        single_ax_opts['add_extra_field_type'] = False
        single_ax_opts['clabel'] = None
        single_ax_opts['create_clevs'] = False
        single_ax_opts['clevs'] = None
        single_ax_opts['plot_title'] = None
        single_ax_opts['extend_value'] = 'both'
        single_ax_opts['norm'] = 'both'

        # Customize line styles
        single_ax_opts['contour_linestyle'] = {'lines.linewidth': 0.5, 'lines.linestyle': 'solid'}
        single_ax_opts['plot_linestyle'] = {'lines.linewidth': 1, 'lines.linestyle': 'dashed'}

        # Customize rcParams
        # See https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=rcparams#matplotlib.rcParams
        single_ax_opts['colorbar_fontsize'] = {'colorbar.fontsize': 8}
        single_ax_opts['axes_fontsize'] = {'axes.fontsize': 10}
        single_ax_opts['title_fontsize'] = {'title.fontsize': 10}
        single_ax_opts['subplot_title_fontsize'] = {'subplot_title.fontsize': 12}

        self._ax_opts = single_ax_opts
        return single_ax_opts

    def set_ax_opts_diff_field(self, ax):
        """ Modify axes internal state based on user-defined options

        Note:
            Only relevant for comparison plots.
        """
        geom = pu.get_subplot_geometry(ax)
        if geom[0] == (3, 1) and geom[1:] == (0, 1, 1, 1):
            self._ax_opts['is_diff_field'] = True
        if geom[0] == (2, 2):
            if geom[1:] == (0, 1, 1, 0):
                self._ax_opts['is_diff_field'] = True
            if geom[1:] == (0, 0, 1, 1):
                self._ax_opts['is_diff_field'] = True
                self._ax_opts['add_extra_field_type'] = True

    def _set_clevs(self, field_name, ptype, ctype):
        """ Helper function for update_ax_opts(): sets contour levels """
        if isinstance(ctype, int):
            if ctype in self.config.spec_data[field_name][ptype]['levels']:
                self._ax_opts['clevs'] = self.config.spec_data[field_name][ptype]['levels'][ctype]
                if not self._ax_opts['clevs']:
                    self._ax_opts['create_clevs'] = True
            else:
                self._ax_opts['create_clevs'] = True

        else:
            if ctype in self.config.spec_data[field_name][ptype]:
                self._ax_opts['clevs'] = self.config.spec_data[field_name][ptype][ctype]
                if not self._ax_opts['clevs']:
                    self._ax_opts['create_clevs'] = True
            else:
                self._ax_opts['create_clevs'] = True
        # self._ax_opts['clevs'] = [float(numeric_string) for numeric_string in self._ax_opts['clevs']]

    def update_ax_opts(self, field_name, ax, pid, level=None):
        """ Set (or reset) some map options

        Parameters:
            field_name (str) : Name of field that needs axes options updated
            ax (Axes) : Axes object
            pid (str) : Plot type identifier
            level (int) : Vertical level (optional, default=None)

        Returns:
            Updated axes internal state
        """
        if self.config.compare:
            geom = pu.get_subplot_geometry(ax)
            if self._subplots == (3, 1):
                # Bottom plot
                if geom[1:] == (0, 1, 1, 1):
                    self._ax_opts['line_contours'] = False  # Is this the default we want?
                    if 'yz' in pid:
                        self._set_clevs(field_name, 'yzplot', 'diffcontours')
                    elif 'xy' in pid:
                        self._set_clevs(field_name, 'xyplot', 'diff_' + str(level))
                # top and middle plots
                else:  # use setting appropriate for diff-plot
                    if 'yz' in pid:
                        self._set_clevs(field_name, 'yzplot', 'contours')
                    elif 'xy' in pid:
                        self._set_clevs(field_name, 'xyplot', int(level))
            elif self._subplots == (2, 2):
                if geom[1:] == (0, 1, 1, 0):
                    if 'yz' in pid:
                        self._set_clevs(field_name, 'yzplot', 'diffcontours')
                    elif 'xy' in pid:
                        self._set_clevs(field_name, 'xyplot', 'diff_' + str(level))
                elif geom[1:] == (0, 0, 1, 1):
                    self._ax_opts['line_contours'] = False  # Is this the default we want?
                    diff_opt = 'diff_' + self.config.extra_diff_plot
                    if diff_opt in self.config.spec_data[field_name]:
                        self._ax_opts['clevs'] = self.config.spec_data[field_name][diff_opt]
                else:
                    if pid == 'yz':
                        self._set_clevs(field_name, 'yzplot', 'contours')
                    elif pid == 'yzave':
                        self._set_clevs(field_name, 'yzaveplot', 'contours')
                    elif pid == 'xy':
                        self._set_clevs(field_name, 'xyplot', int(level))
                    elif pid == 'xyave':
                        self._set_clevs(field_name, 'xyaveplot', int(level))
                    elif pid == 'tx':
                        self._set_clevs(field_name, 'txplot', 'contours')
                    elif pid == 'polar':
                        self._set_clevs(field_name, 'polarplot', int(level))
        else:  # _subplots == (1, 1)
            if pid == 'yz':
                self._set_clevs(field_name, 'yzplot', 'contours')
            elif pid == 'yzave':
                self._set_clevs(field_name, 'yzaveplot', 'contours')
            elif pid == 'xy':
                if level:
                    self._set_clevs(field_name, 'xyplot', int(level))
                else:
                    self._set_clevs(field_name, 'xyplot', None)
            elif pid == 'xyave':
                if level:
                    self._set_clevs(field_name, 'xyaveplot', int(level))
                else:
                    self._set_clevs(field_name, 'xyaveplot', None)
            elif pid == 'tx':
                self._set_clevs(field_name, 'txplot', 'contours')
            elif pid == 'polar':
                if level:
                    self._set_clevs(field_name, 'polarplot', int(level))
                else:
                    self._set_clevs(field_name, 'polarplot', None)
        return self._ax_opts

    def _add_comp_plot_title(self, ax, fontsize, did=None):
        """ Helper function for plot_text() """
        if self.config.get_file_exp_name(did):
            self._ax_opts['plot_title'] = self.config.get_file_exp_name(did)
            ax.set_title(self._ax_opts['plot_title'], fontsize=fontsize, loc='left')
        else:
            self._ax_opts['plot_title'] = os.path.basename(self.config.file_list[self.config.findex]['filename'])
            ax.set_title(self._ax_opts['plot_title'], fontsize=fontsize, loc='left')
        return ax

    def plot_text(self, field_name, ax, pid, level=None, data=None):
        """ Add text to a map .

        Parameters:
            field_name (str) : Name of the field
            ax (Axes) : Axes object
            pid (str) : Plot type identifier
            level (int) : Vertical level (optional, default=None)

        Returns:
            Updated axes internal state
        """
        fontsize = pu.subplot_title_font_size(self._subplots)
        findex = self.config.findex
        sname = self.config.map_params[findex]['source_name']
        ds_index = self.config.map_params[findex]['source_index']
        if self.config.compare:
            geom = pu.get_subplot_geometry(ax)
            if geom[0] == (3, 1):
                # Bottom plot
                if geom[1:] == (0, 1, 1, 1):
                    self._ax_opts['plot_title'] = "Difference (top - middle)"
                    ax.set_title(self._ax_opts['plot_title'], fontsize=fontsize)
                # top and middle plots
                else:  # use setting appropriate for diff-plot
                    if geom[1:] == (1, 1, 0, 1):
                        self._add_comp_plot_title(ax, fontsize, did=0)
                    if geom[1:] == (0, 1, 0, 1):
                        self._add_comp_plot_title(ax, fontsize, did=1)
            elif self._subplots == (2, 2):
                if geom[1:] == (0, 1, 1, 0):
                    self._ax_opts['plot_title'] = "Difference (left - right)"
                    ax.set_title(self._ax_opts['plot_title'], fontsize=fontsize)

                elif geom[1:] == (0, 0, 1, 1):
                    if "percd" in self.config.extra_diff_plot:
                        self._ax_opts['plot_title'] = "% Diff"
                        self._ax_opts['clabel'] = "%"
                    elif "percc" in self.config.extra_diff_plot:
                        self._ax_opts['plot_title'] = "% Change"
                        self._ax_opts['clabel'] = "%"
                    elif "ratio" in self.config.extra_diff_plot:
                        self._ax_opts['plot_title'] = "Ratio Diff"
                        self._ax_opts['clabel'] = "ratio"
                    else:
                        self._ax_opts['plot_title'] = "Difference (left - right)"
                    self._ax_opts['line_contours'] = False
                    ax.set_title(self._ax_opts['plot_title'], fontsize=fontsize)
                else:
                    if ax.get_subplotspec().colspan.start == 0 and ax.get_subplotspec().rowspan.start == 0:
                        self._add_comp_plot_title(ax, fontsize, did=0)
                    if ax.get_subplotspec().colspan.start == 1 and ax.get_subplotspec().rowspan.start == 0:
                        self._add_comp_plot_title(ax, fontsize, did=1)
            else:
                plot_title = os.path.basename(
                    self.config.readers[sname].datasets[ax.get_subplotspec().colspan.start]['filename'])
                ax.set_title(plot_title, fontsize=fontsize)

        else:
            # https://matplotlib.org/stable/tutorials/text/text_props.html
            fmt = ""
            loc = 'center'
            left, width = 0, 1.0
            bottom, height = 0, 1.0
            right = left + width
            top = bottom + height
            level_text = None
            if self.config.ax_opts['zave']:
                level_text = ' (Total Column)'
            else:
                if str(level) == '0':
                    level_text = ''
                else:
                    if level is not None:
                        if level > 10000:
                            level_text = '@ ' + str(level) + ' Pa'
                        else:
                            level_text = '@ ' + str(level) + ' mb'

            # Get model-specific field name attribute
            try:
                attr_field_name = self.config.meta_attrs['field_name'][self.config.source_names[ds_index]]
            except KeyError:
                attr_field_name = "NA"
            if 'yz' in pid:
                if self.config.print_basic_stats:
                    # plt.rc('text', usetex=True)
                    fmt = self._basic_stats(data)
                    # fmt = self._basic_stats(field_name, ds_index, "xc", "tc")
                    loc = 'left'
                if self.config.use_history:
                    ax.set_title(self.config.history_expid + " (" + self.config.history_expdsc + ")")
                else:
                    if self.config.get_file_exp_name(findex):
                        ax.set_title(self.config.get_file_exp_name(findex))
                    else:
                        ax.set_title(os.path.basename(self.config.readers[sname].datasets[findex]['filename']))
                    if self.config.get_file_description(findex):
                        text_content = self.config.get_file_description(findex)
                        # Set the text position in axes coordinates
                        text_position = (0.95, 0.05)  # (x, y)
                        # Add text to the axes
                        ax.text(*text_position, text_content, transform=ax.transAxes,
                                horizontalalignment='right', verticalalignment='bottom')
                        # To write in figure area - we need fig object and ...
                        # Set the text position outside the axes
                        # text_position = (1.05, -0.1)  # (x, y)
                        # Add text to the figure (outside the axes)
                        # fig.text(*text_position, text_content, ha='right', va='bottom')

                ax.text(right, top, fmt,
                        transform=ax.transAxes)
                try:
                    ax.text(0.5 * (left + right), bottom + top + 0.1,
                            field_name,
                            transform=ax.transAxes)
                except:
                    ax.text(0.5 * (left + right), bottom + top + 0.1, '',
                            transform=ax.transAxes)

            elif 'xy' in pid:
                if self.config.print_basic_stats:
                    # plt.rc('text', usetex=True)
                    fmt = self._basic_stats(data)
                    # fmt = self._basic_stats(field_name, ds_index, "zc", "tc")
                    loc = 'left'
                if self.config.use_history:
                    ax.set_title(self.config.history_expid + " (" + self.config.history_expdsc + ")", fontsize=10,
                                 loc=loc)
                else:
                    if self.config.get_file_exp_name(findex):
                        ax.set_title(self.config.get_file_exp_name(findex), loc=loc)
                    else:
                        ax.set_title(os.path.basename(self.config.readers[sname].datasets[findex]['filename']),
                                     loc=loc)

                ax.text(right, top, fmt,
                        horizontalalignment='right',
                        verticalalignment='bottom',
                        transform=ax.transAxes)
                try:
                    ax.text(0.5 * (left + right), bottom + top + 0.1,
                            field_name + level_text,
                            horizontalalignment='center',
                            verticalalignment='center',
                            transform=ax.transAxes)
                except:
                    ax.text(0.5 * (left + right), bottom + top + 0.1, '',
                            horizontalalignment='center',
                            verticalalignment='center',
                            transform=ax.transAxes)

            elif 'xt' in pid:
                if self.config.use_history:
                    ax.set_title(self.config.history_expid + " (" + self.config.history_expdsc + ")", fontsize=10,
                                 loc=loc)
                else:
                    if self.config.get_file_exp_name(
                            self.config.get_file_index(self.config.map_params[findex]['filename'])):
                        ax.set_title(os.path.basename(self.config.get_file_exp_name(self.config.file_list[findex])),
                                     fontsize=10, loc=loc)
                    else:
                        ax.set_title(os.path.basename(self.config.readers[sname].datasets[findex]['filename']),
                                     fontsize=10, loc=loc)

                ax.text(right, top, fmt,
                        horizontalalignment='right',
                        verticalalignment='bottom',
                        transform=ax.transAxes)
                ax.text(0.5 * (left + right), bottom + top + 0.1,
                        field_name,
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontsize=fontsize,
                        transform=ax.transAxes)
            elif 'po' in pid:
                pass
            else:
                if self.config.use_history:
                    ax.set_title(self.config.history_expid + " (" + self.config.history_expdsc + ")", fontsize=10,
                                 loc=loc)
                else:
                    if self.config.get_file_exp_name(self.config.file_list[findex]):
                        ax.set_title(os.path.basename(self.config.get_file_exp_name(self.config.file_list[findex])),
                                     fontsize=10, loc=loc)
                    else:
                        ax.set_title(os.path.basename(self.config.readers[sname].datasets[findex]['filename']),
                                     fontsize=10, loc=loc)

                ax.text(right, top, fmt,
                        horizontalalignment='right',
                        verticalalignment='bottom',
                        transform=ax.transAxes)
                try:
                    ax.text(0.5 * (left + right), bottom + top + 0.1,
                            field_name,
                            horizontalalignment='center',
                            verticalalignment='center',
                            fontsize=fontsize,
                            transform=ax.transAxes)
                except:
                    name = self.config.spec_data[field_name]['name']
                    ax.text(0.5 * (left + right), bottom + top + 0.1,
                            name,
                            horizontalalignment='center',
                            verticalalignment='center',
                            fontsize=fontsize,
                            transform=ax.transAxes)

    def _basic_stats2(self, field_name, *args):
        """ Really basic stats for a given field """
        # datamin = data.min().values
        # datamax = data.max().values
        L = list()
        for arg in args:
            L.append(self.get_model_dim_name(arg))
        m = xu.compute_mean_over_dim(self.config.readers[self.config.ds_index].datasets[self.config.findex]['vars'],
                                     tuple(L), field_name=field_name)
        s = xu.compute_std_over_dim(self.config.readers[self.config.ds_index].datasets[self.config.findex]['vars'],
                                    tuple(L), field_name=field_name)
        datamean = self._apply_conversion(np.nanmean(m), field_name)
        datastd = self._apply_conversion(np.nanstd(s), field_name)
        return f"\nMean:{datamean:.2e}\nStd:{datastd:.2e}"

    @staticmethod
    def _basic_stats(data):
        """ Really basic stats for a given field """
        # datamin = data.min().values
        # datamax = data.max().values
        datamean = data.mean().values
        datastd = data.std().values
        return f"\nMean:{datamean:.2e}\nStd:{datastd:.2e}"

    def set_cartopy_features(self, axes):
        """ These are 'typical' map features used in Cartopy-dependent maps

        Parameters:
            axes (Axes) : Figure axes.

        Returns:
            Update axes.
        """
        if self._ax_opts['extent']:
            axes.coastlines(resolution='110m', color='black')
            if self._ax_opts['extent'] == 'conus':
                axes.add_feature(cfeature.STATES, linewidth=0.3, edgecolor='brown')
                states_provinces = cfeature.NaturalEarthFeature(category='cultural',
                                                                name='admin_1_states_provinces_lines',
                                                                scale='50m', facecolor='none')
                axes.add_feature(states_provinces, edgecolor='grey', zorder=10)
            axes.add_feature(cfeature.BORDERS, linestyle='--')
        else:
            axes.coastlines(alpha=0.1)
            axes.add_feature(cfeature.LAND, facecolor='0.9')
            axes.add_feature(cfeature.LAKES, alpha=0.9)
            axes.add_feature(cfeature.BORDERS, zorder=10, linewidth=0.5, edgecolor='grey')
            axes.add_feature(cfeature.COASTLINE, zorder=10)
        return axes

    @staticmethod
    def set_cartopy_latlon_opts(ax, extent):
        """ These appear to be pretty good settings for latlon maps

        Parameters:
            ax (Axes) : Figure axes.
            extent (list) : Domain extent for cartopy coordinates.

        Returns:
            Update axes.
        """
        # TODO: Fix this
        # gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
        gl = ax.grid(color='gray', linestyle='--', alpha=0.5, linewidth=0.5)

        # gl.xlabels_top = None
        # gl.ylabels_right = None
        if extent[0] < -179.0:
            xgrid = np.array([-180, -120, -60, 0, 60, 120, 180])
            ygrid = np.array([-90, -60, -30, 0, 30, 60])
        else:
            xgrid = np.linspace(extent[0], extent[1], 8)
            ygrid = np.linspace(extent[2], extent[3], 8)
        # gl.xlocator = FixedLocator(xgrid.tolist())
        # gl.ylocator = FixedLocator(ygrid.tolist())
        # gl.xformatter = LONGITUDE_FORMATTER
        # gl.yformatter = LATITUDE_FORMATTER
        # gl.xlabel_style = {'size': 10, 'color': 'black'}
        # gl.ylabel_style = {'size': 10, 'color': 'black'}
        return ax

    @staticmethod
    def colorbar(mappable):
        """ Create a colorbar.

        Note:
            Reference: https://joseph-long.com/writing/colorbars/
        """
        last_axes = plt.gca()
        ax = mappable.axes
        fig = ax.figure
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        cbar = fig.colorbar(mappable, cax=cax)
        plt.sca(last_axes)
        return cbar

    def get_projection(self, projection=None):
        """ Get projection parameter"""
        # TODO: Fix for the case when projection is not None!!!
        if not projection:
            return ccrs.PlateCarree()
        if 'extent' not in self._ax_opts:
            self._ax_opts['extent'] = [-140, -40, 15, 65]  # conus
            central_lon, central_lat = -96, 37.5  # conus
        else:
            if self._ax_opts['extent'] == 'conus':
                extent = [-140, -40, 15, 65]  # [-120, -70, 24, 50.5]
                # Make sure...
                projection = 'lambert'
            else:
                extent = [-180, 180, -90, 90]
            central_lon = np.mean(extent[:2])
            central_lat = np.mean(extent[2:])
        options = {'lambert': ccrs.LambertConformal(central_latitude=central_lat,
                                                    central_longitude=central_lon),
                   'albers': ccrs.AlbersEqualArea(central_latitude=central_lat,
                                                  central_longitude=central_lon),
                   'stereo': ccrs.Stereographic(central_latitude=central_lat,
                                                central_longitude=central_lon),
                   'ortho': ccrs.Orthographic(central_latitude=central_lat,
                                              central_longitude=central_lon),
                   'polar': ccrs.NorthPolarStereo(central_longitude=-100),
                   'mercator': ccrs.Mercator()}
        return options[projection]

    @staticmethod
    def squeeze_fig_aspect(fig, preserve='h'):
        # https://github.com/matplotlib/matplotlib/issues/5463
        preserve = preserve.lower()
        bb = bbase.union([ax.bbox for ax in fig.axes])

        w, h = fig.get_size_inches()
        if preserve == 'h':
            new_size = (h * bb.width / bb.height, h)
        elif preserve == 'w':
            new_size = (w, w * bb.height / bb.width)
        else:
            raise ValueError(
                'preserve must be "h" or "w", not {}'.format(preserve))
        fig.set_size_inches(new_size, forward=True)

    # TODO: Move to utils
    def _apply_conversion(self, data2d, name):
        if 'unitconversion' in self.config.spec_data[name]:
            if "AOA" in name.upper():
                data2d = data2d / np.timedelta64(1, 'ns') / 1000000000 / 86400
            else:
                data2d = data2d * float(self.config.spec_data[name]['unitconversion'])
        return data2d

    @property
    def frame_params(self):
        return self._frame_params

    @property
    def subplots(self):
        return self._subplots
