import logging
import warnings
from dataclasses import dataclass

import numpy as np
import xarray as xr

from eviz.lib.data.processor import Interp
from eviz.models.esm.generic import Generic

warnings.filterwarnings("ignore")


@dataclass()
class Geos(Generic):
    """ Define GEOS-specific model data and functions.
    The GEOS-specific functionality centers around the HISTORY.rc file which contains
    information about the GEOS data sources. In Eviz, the HISTORY.rc is parsed during
    initialization and the relevant information is stored in the Config object.

    Parameters:
        config (Config) : Config object associated with this model
    """
    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)
    
    def __post_init__(self):
        self.logger.info("Start init")
        self.season = None
        super().__post_init__()

    def _get_field_to_plot(self, source_data, field_name, file_index, plot_type, figure, level=None):
        _, ax = figure.get_fig_ax()
        self.config.ax_opts = figure.init_ax_opts(field_name)
        dim1, dim2 = self.config.get_dim_names(plot_type)
        data2d = None
        if 'yz' in plot_type:
            data2d = self._get_yz(source_data, field_name, time_lev=self.config.ax_opts['time_lev'])
        elif 'xt' in plot_type:
            data2d = self._get_xt(source_data, field_name, time_lev=self.config.ax_opts['time_lev'])
        elif 'tx' in plot_type:
            data2d = self._get_tx(source_data, field_name, level=None, time_lev=self.config.ax_opts['time_lev'])
        elif 'xy' in plot_type or 'polar' in plot_type:
            data2d = self._get_xy(source_data, field_name, level=level, time_lev=self.config.ax_opts['time_lev'])
        else:
            pass

        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, None, None, field_name, plot_type, file_index, figure, ax
        return data2d, data2d[dim1].values, data2d[dim2].values, field_name, plot_type, file_index, figure, ax

    def _get_field_to_plot_compare(self, source_data, field_name, file_index, plot_type, figure, ax=None, level=None):
        if ax is None:
            _, ax = figure.get_fig_ax()
        # field_name, plot_type, level, ds_meta, output_fname = map_params[0]
        dim1, dim2 = self.config.get_dim_names(plot_type)
        data2d = None
        if self.config.ax_opts['is_diff_field']:
            proc = Interp(self.config, source_data)
            data2d, xx, yy = proc.regrid(self.field_names, ax, level, plot_type)
            return data2d, xx, yy, self.field_names[0], plot_type, file_index, figure, ax
        else:
            d = source_data['vars'][field_name]
            if 'yz' in plot_type:
                data2d = self._get_yz(source_data, field_name, time_lev=self.config.ax_opts['time_lev'])
            elif 'xt' in plot_type:
                data2d = self._get_xt(source_data, field_name, time_lev=self.config.ax_opts['time_lev'])
            elif 'tx' in plot_type:
                data2d = self._get_tx(source_data, field_name, level=None, time_lev=self.config.ax_opts['time_lev'])
            elif 'xy' in plot_type or 'polar' in plot_type:
                data2d = self._get_xy(source_data, field_name, level=level, time_lev=self.config.ax_opts['time_lev'])
            else:
                pass

        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, None, None, field_name, plot_type, file_index, figure, ax
        return data2d, data2d[dim1].values, data2d[dim2].values, field_name, plot_type, file_index, figure, ax

    def _get_yz(self, d, name, time_lev=0):
        """ Create YZ slice from N-dim data field"""
        # Check if a singleton dimension exists
        d_temp = d['vars'][name]
        if d_temp is None:
            return
        data2d = d_temp.squeeze()
        if self.config.get_model_dim_name('tc') in d_temp.dims:
            num_times = eval(f"np.size(d_temp.{self.config.get_model_dim_name('tc')})")
            if self.config.ax_opts['tave'] and num_times > 1:
                self.logger.debug(f"Averaging over {num_times} time levels.")
                data2d = self._apply_mean(data2d)
            else:
                data2d = eval(f"d_temp.isel({self.config.get_model_dim_name('tc')}=time_lev)")
        else:
            data2d = d_temp
        data2d = self._select_yrange(data2d, name)
        data2d = data2d.mean(dim=self.config.get_model_dim_name('xc'))
        return self._apply_conversion(data2d, name)

    def _get_xy(self, d, name, level, time_lev=0):
        """ Extract XY slice from N-dim data field"""
        d_temp = d['vars'][name]
        if d_temp is None:
            return
        data2d = d_temp.squeeze()
        if level:
            level = int(level)
        if self.config.get_model_dim_name('tc') in d_temp.dims:
            num_times = eval(f"np.size(d_temp.{self.config.get_model_dim_name('tc')})")
            if self.config.ax_opts['tave'] and num_times > 1:
                self.logger.debug(f"Averaging over {num_times} time levels.")
                data2d = self._apply_mean(data2d, level)
                return self._apply_conversion(data2d, name)
            else:
                data2d = eval(f"d_temp.isel({self.config.get_model_dim_name('tc')}=time_lev)")
        else:
            data2d = d_temp
        data2d = data2d.squeeze()
        if self.config.get_model_dim_name('zc') in data2d.dims:
            if level:
                lev_to_plot = int(np.where(data2d.coords[self.config.get_model_dim_name('zc')].values == level)[0])
                data2d = eval(f"data2d.isel({self.config.get_model_dim_name('zc')}=lev_to_plot)")
        return self._apply_conversion(data2d, name)

    def _get_xt(self, d, name, time_lev=None):
        """ Compute time series from N-dim data field"""
        d_temp = d['vars'][name]
        if d_temp is None:
            return

        if isinstance(time_lev, list):
            data2d = eval(f"d_temp.isel({self.config.get_model_dim_name('tc')}=slice(time_lev))")
        else:
            data2d = d_temp.squeeze()

        if 'mean_type' in self.config.spec_data[name]['xtplot']:
            mean_type = self.config.spec_data[name]['xtplot']['mean_type']
            # annual:
            if mean_type == 'point_sel':
                xc = self.config.spec_data[name]['xtplot']['point_sel'][0]
                yc = self.config.spec_data[name]['xtplot']['point_sel'][1]
                data2d = data2d.sel(lon=xc, lat=yc, method='nearest')
            elif mean_type == 'area_sel':
                x1 = self.config.spec_data[name]['xtplot']['area_sel'][0]
                x2 = self.config.spec_data[name]['xtplot']['area_sel'][1]
                y1 = self.config.spec_data[name]['xtplot']['area_sel'][2]
                y2 = self.config.spec_data[name]['xtplot']['area_sel'][3]
                data2d = data2d.sel(lon=np.arange(x1, x2, 0.5), lat=np.arange(y1, y2, 0.5), method='nearest')
                data2d = data2d.mean(dim=(self.config.get_model_dim_name('xc'), self.config.get_model_dim_name('yc')))
            elif mean_type in ['year', 'season', 'month']:
                data2d = data2d.groupby(self.config.get_model_dim_name('tc') + '.' + mean_type).mean(
                    dim=self.config.get_model_dim_name('tc'))
            else:
                data2d = data2d.groupby(self.config.get_model_dim_name('tc')).mean(dim=xr.ALL_DIMS)
                if 'mean_type' in self.config.spec_data[name]['xtplot']:
                    if self.config.spec_data[name]['xtplot']['mean_type'] == 'rolling':
                        window_size = 5
                        if 'window_size' in self.config.spec_data[name]['xtplot']:
                            window_size = self.config.spec_data[name]['xtplot']['window_size']
                        data2d = eval(f"data2d.rolling({self.config.get_model_dim_name('tc')}=window_size).mean()")

        else:
            data2d = data2d.groupby(self.config.get_model_dim_name('tc')).mean(dim=xr.ALL_DIMS)

        if 'level' in self.config.spec_data[name]['xtplot']:
            level = int(self.config.spec_data[name]['xtplot']['level'])
            lev_to_plot = int(np.where(data2d.coords[self.config.get_model_dim_name('zc')].values == level)[0])
            data2d = data2d[:, lev_to_plot].squeeze()

        return self._apply_conversion(data2d, name)

    def _get_tx(self, d, name, level=None, time_lev=None):
        d_temp = d['vars'][name]
        if d_temp is None:
            return

        data2d = d_temp.squeeze()
        if self.config.get_model_dim_name('zc') in d_temp.dims:
            data2d = eval(f"d_temp.isel({self.config.get_model_dim_name('zc')}=0)")

        if 'trange' in self.config.spec_data[name]['txplot']:
            start_time = self.config.spec_data[name]['txplot']['trange'][0]
            end_time = self.config.spec_data[name]['txplot']['trange'][1]
        if 'yrange' in self.config.spec_data[name]['txplot']:
            lats0 = self.config.spec_data[name]['txplot']['yrange'][0]
            lats1 = self.config.spec_data[name]['txplot']['yrange'][1]
        if 'xrange' in self.config.spec_data[name]['txplot']:
            lons0 = self.config.spec_data[name]['txplot']['xrange'][0]
            lons1 = self.config.spec_data[name]['txplot']['xrange'][1]
        weights = eval(f"np.cos(np.deg2rad(data2d.{self.config.get_model_dim_name('yc')}.values))")

        d1 = data2d * weights[None, :, None]
        d2 = eval(f"d1.sum(dim=self.config.get_model_dim_name('yc'))")
        d3 = d2 / np.sum(weights)
        return self._apply_conversion(d3, name)

    def _apply_conversion(self, data2d, name):
        if 'unitconversion' in self.config.spec_data[name]:
            if "AOA" in name.upper():
                data2d = data2d / np.timedelta64(1, 'ns') / 1000000000 / 86400
            else:
                data2d = data2d * float(self.config.spec_data[name]['unitconversion'])
        return data2d

    def _apply_mean(self, d, level=None):
        # Time average:
        if level:
            if len(d.dims) == 3:
                data2d = d.mean(dim=self.config.get_model_dim_name('tc'))
            else:  # 4D array - we need to select a level
                lev_to_plot = int(np.where(d.coords[self.config.get_model_dim_name('zc')].values == level)[0])
                self.logger.debug("Level to plot:" + str(lev_to_plot))
                # select level
                data2d = eval(f"d.isel({self.config.get_model_dim_name('zc')}=lev_to_plot)")
                data2d = data2d.mean(dim=self.config.get_model_dim_name('tc'))
        else:
            if len(d.dims) == 3:
                data2d = d.mean(dim=self.config.get_model_dim_name('tc'))
            else:
                d = d.mean(dim=self.config.get_model_dim_name('xc'))
                data2d = d.mean(dim=self.config.get_model_dim_name('tc'))
        return data2d

    def _select_yrange(self, data2d, name):
        """ Select a range of vertical levels"""
        if 'zrange' in self.config.spec_data[name]['yzplot']:
            if not self.config.spec_data[name]['yzplot']['zrange']:
                return data2d
            lo_z = self.config.spec_data[name]['yzplot']['zrange'][0]
            hi_z = self.config.spec_data[name]['yzplot']['zrange'][1]
            if hi_z >= lo_z:
                self.logger.error(f"Upper level value ({hi_z}) must be less than low level value ({lo_z})")
                return
            lev = self.config.get_model_dim_name('zc')
            min_index, max_index = 0, len(data2d.coords[lev].values) - 1
            for k, v in enumerate(data2d.coords[lev]):
                if data2d.coords[lev].values[k] == lo_z:
                    min_index = k
            for k, v in enumerate(data2d.coords[lev]):
                if data2d.coords[lev].values[k] == hi_z:
                    max_index = k
            return data2d[min_index:max_index + 1, :, :]
        else:
            return data2d

# TODO: Currently, Geos() is basically Generic(). Need to add HISTORY and Overlays below
#  to make it into a separate Geos()


"""
    def _comparison_plots(self, plotter):
        # TODO: self.logger.info(f"Creating {self.config.model_name.upper()} comparison plots.")
        # Read data from files to be compared
        foo = self.config.compare['exp_list']
        self.config.compare_sources = foo.split(',')
        file_path = self.config.file_list[0]['filename']
        # TODO: need to deal with different readers - current only one
        model_data1 = self.config.readers[0].read_data(file_path)
        file_path = self.config.file_list[1]['filename']
        model_data2 = self.config.readers[0].read_data(file_path)
        self.model_data = (model_data1, model_data2)
        map_params = self.config.map_params
        # self.maps_params = self.config.figure.get_map_params(self.config)  # convenience var
        maps1 = map_params[0]
        maps2 = map_params[1]
        if len(maps1) == 0 or len(maps2) == 0:
            self.logger.error(f"Specification is not defined for the desired plot type!")
            sys.exit()

        for i1, i2 in zip(maps1, maps2):
            field_name1, plot_type, level, ds_meta1, output_fname = i1
            field_name2, plot_type, level, ds_meta2, *_ = i2
            figure = Figure(self.config, plot_type)
            fig, ax = figure.get_fig_ax()

            self.logger.info(f"{field_name1} vs {field_name2}, {plot_type}, level:{level}")

            self.field_names = (field_name1, field_name2)

            # TODO: make a decorator
            # self.preproc1 = Overlays(figure, self.config)
            # self.preproc2 = Overlays(figure, self.config)
            #
            # if 'yz' in plot_type:
            #     self.preproc1.trop_field(ds_meta1, 0)
            #     self.preproc2.trop_field(ds_meta2, 1)
            # self.preproc1.sphum_field(ds_meta1, 0)
            # self.preproc2.sphum_field(ds_meta2, 1)

            # axes_shape = fig.get_axes_shape()
            if ax.shape == (3, ):
                self.config.ax_opts = figure.init_ax_opts(field_name1, did=0)
                figure.set_ax_opts_diff_field(ax[0])
                data_to_plot = self._get_field_to_plot_compare(source_data=model_data1,
                                                               findex=0, map_params=maps1, figure=figure)
                if self.use_mp_pool:
                    p = multiprocessing.Process(target=plotter.comparison_plots,
                                                args=(self.config, data_to_plot))
                    self.logger.info(f"  start " + p.name)
                    self.procs.append(p)
                    p.start()
                else:
                    plotter.comparison_plots(self.config, data_to_plot)

                self.config.ax_opts = figure.init_ax_opts(field_name2, did=1)
                figure.set_ax_opts_diff_field(ax[1])
                data_to_plot = self._get_field_to_plot_compare(source_data=model_data2,
                                                               findex=1, map_params=maps2, figure=figure)
                plotter.comparison_plots(self.config, data_to_plot)

                self.comparison_plot = True
                self.config.ax_opts = figure.init_ax_opts(field_name1, did=1)
                figure.set_ax_opts_diff_field(ax[2])
                data_to_plot = self._get_field_to_plot_compare(source_data=self.model_data,
                                                               findex=1, map_params=maps2, figure=figure)
                plotter.comparison_plots(self.config, data_to_plot)

            elif ax.shape == (2, 2):
                # Plot one axes at a time
                self.config.ax_opts = figure.init_ax_opts(field_name1, did=0)
                # axes (0,0)
                figure.set_ax_opts_diff_field(ax[0, 0])
                data_to_plot = self._get_field_to_plot_compare(source_data=model_data1,
                                                               findex=0, map_params=maps1, figure=figure)
                # send data to plot to plotter function
                plotter.comparison_plots(self.config, data_to_plot)

                self.config.ax_opts = figure.init_ax_opts(field_name2, did=1)
                # axes (0,1)
                figure.set_ax_opts_diff_field(ax[0, 1])
                data_to_plot = self._get_field_to_plot_compare(source_data=model_data2,
                                                               findex=1, map_params=maps2, figure=figure)
                plotter.comparison_plots(self.config, data_to_plot)

                self.comparison_plot = True
                self.config.ax_opts = figure.init_ax_opts(field_name1, did=1)
                # axes (1,0)
                figure.set_ax_opts_diff_field(ax[1, 0])
                data_to_plot = self._get_field_to_plot_compare(source_data=self.model_data,
                                                               findex=1, map_params=maps2, figure=figure)
                plotter.comparison_plots(self.config, data_to_plot)

                self.comparison_plot = True
                self.config.ax_opts = figure.init_ax_opts(field_name1, did=1)
                # axes (1,1)
                figure.set_ax_opts_diff_field(ax[1, 1])
                data_to_plot = self._get_field_to_plot_compare(source_data=self.model_data,
                                                               findex=1, map_params=maps2, figure=figure)
                plotter.comparison_plots(self.config, data_to_plot)

        if self.use_mp_pool:
            for p in self.procs:
                self.logger.info(f"process{p.name} is done")
                p.join()

    def _single_plots_todo(self):
        self.logger.info(f"Creating {self.config.model_name.upper()} plots.")
        if not self.config.have_specs_yaml_file:
            # Generic basic plots
            self.basic_plot()
            return

        for findex in range(len(self.config.file_list)):
            rindex = 0
            self.findex['filename'] = findex
            self.config.findex = findex
            file_path = self.config.file_list[findex]['filename']
            self.model_data = self.config.readers[0].read_data(file_path)

            self.frame_params = self.config.figure.frame(self.config)
            self.maps_params = self.config.figure.get_map_params(self.config)

            for p_index in range(len(self.maps_params[findex])):
                field_name, plot_type, level, ds_meta, output_fname = self.maps_params[findex][p_index]
                self.logger.info(f"{field_name}, {plot_type}, level:{level}")

                self.ax_opts = self.config.figure.init_ax_opts(self.config, field_name, plot_type[0:2], did=findex)
                self.fig, ax = self.config.figure.get_fig_ax(self.config, plot_type, rindex)
                self.config.figure.set_ax_opts_diff_field(self.config, ax)
                self.output_fname = output_fname

                self.preproc = Overlays(self.config.figure, self.config)
                if 'yz' in plot_type:
                    self.preproc.trop_field(ds_meta, findex)
                self.preproc.sphum_field(ds_meta)

                self.map_data = self.get_plot_data(field_name, ax, self.ax_opts, plot_type, level=level)
                if self.use_mp_pool:
                    p = multiprocessing.Process(target=self._plot,
                                                args=(field_name, ax, plot_type, level))
                    self.logger.info(f"  start " + p.name)
                    self.procs.append(p)
                    p.start()
                else:
                    self._plot(field_name, ax, plot_type, level=level)

        if self.use_mp_pool:
            for p in self.procs:
                self.logger.info(f"process{p.name} is done")
                p.join()

    def _yzplot_subplot_todo(self, field_name, ax):
        data2d, x, y = self.map_data
        if data2d is None:
            return
        self.ax_opts = self.config.figure.update_ax_opts(self.config, field_name, ax, 'yz')
        self.config.figure.plot_text(self.config, field_name, ax, 'yz', data=data2d)

        if self.ax_opts['profile_dim']:
            prof_dim = self.ax_opts['profile_dim']
            dep_var = None
            if prof_dim == 'yc':
                dep_var = 'zc'
            if prof_dim == 'zc':
                dep_var = 'yc'
            data2d = data2d.mean(dim=self.get_model_dim_name(prof_dim))
            self._prof_plot(ax, data2d, (self.ax_opts['profile_dim'], dep_var))
        else:
            cfilled = self._filled_contours(field_name, ax, x, y, data2d)

            # This needs to be done before colorbar, else fig.colorbar will change the axes nrows and ncols attributes
            # Investigate if this is a PLT bug or an EVIZ bug
            if self.config.compare:
                if (self.preproc1.trop_ok or self.preproc2.trop_ok) and not self.comparison_plot:
                    self.logger.debug(f"Adding troppopause height layer")
                    tropopause = None
                    if self.did == 0:
                        tropopause = self.preproc1.tropp.mean(dim='lon') * self.preproc1.tropp_conversion
                        self.preproc1.trop_ok = False
                    elif self.did == 1:
                        tropopause = self.preproc2.tropp.mean(dim='lon') * self.preproc2.tropp_conversion
                        self.preproc2.trop_ok = False
                    ax.plot(x, tropopause, linewidth=2, color="k", linestyle="--")

            else:
                if self.preproc.trop_ok and not self.comparison_plot:
                    self.logger.debug(f"Adding troppopause height layer")
                    tropopause = self.preproc.tropp.mean(dim='lon') * self.preproc.tropp_conversion
                    ax.plot(x, tropopause, linewidth=2, color="k", linestyle="--")

            contour_format = pu.contour_format_from_levels(pu.formatted_contours(self.ax_opts['clevs']),
                                                           scale=self.ax_opts['cscale'])

            self._set_colorbar(cfilled, ax, field_name, contour_format)

            ylabels = ax.get_yticklabels()
            for label in ylabels:
                label.set_fontsize(pu.axis_tick_font_size(self.config.figure.subplots))

            xlabels = ax.get_xticklabels()
            for label in xlabels:
                label.set_fontsize(pu.axis_tick_font_size(self.config.figure.subplots))

            self._set_ax_ranges(field_name, ax, y)

            self._line_contours(ax, x, y, data2d)

        if self.config.compare and self.comparison_plot:
            if 'name' in self.config.spec_data[field_name]:
                name = self.config.spec_data[field_name]['name']
            else:
                name = data2d.name
            plt.suptitle(
                name,
                fontstyle='italic',
                fontsize=16)

        if self.config.add_logo:
            pu.add_logo_fig(self.fig, self.config.figure.EVIZ_LOGO)

        # TODO: tweak this
        # pu.squeeze_fig_aspect(self.fig)

        self._print_map(field_name)

    def _set_ax_ranges(self, name, ax, y):
        # A sensible number of vertical levels
        y_ranges = np.array([1000, 700, 500, 300, 200, 100])
        if y.min() <= 10.0:
            y_ranges = np.append(y_ranges, np.array([70, 50, 30, 20, 10]))
        if y.min() <= 0.2:
            y_ranges = np.append(y_ranges, np.array([7, 5, 3, 2, 1, .7, .5, .3, .2, .1]))
        if y_ranges[-1] != y.min():
            y_ranges = np.append(y_ranges, y.min())

        lo_z, hi_z = y_ranges.max(), y_ranges.min()
        if 'zrange' in self.config.spec_data[name]['yzplot']:
            if not self.config.spec_data[name]['yzplot']['zrange']:
                pass  # if nothing specified (it happens)
            else:
                lo_z = self.config.spec_data[name]['yzplot']['zrange'][0]
                hi_z = self.config.spec_data[name]['yzplot']['zrange'][1]
                if hi_z >= lo_z:
                    self.logger.error(f"Upper level value ({hi_z}) must be less than low level value ({lo_z})")
                    return None

        # These can be defined for global or regional models. We let the respective model
        # override the extents. For generic, we assume they are global extents.
        ax.set_xticks([-90, -60, -30, 0, 30, 60, 90])
        ax.set_xticklabels(["90S", "60S", "30S", "EQ", "30N", "60N", "90N"])
        ax.tick_params(width=3, length=6)
        # The vertical coordinate can have different units. For generic, we assume pressure
        # and, again, let specialized models override the definition.
        # Assume surface is the first level
        ax.set_ylim(lo_z, hi_z)
        # scale is by default "log"
        ax.set_yscale(self.ax_opts['zscale'])
        ax.yaxis.set_minor_formatter(NullFormatter())
        if 'linear' in self.ax_opts['zscale']:
           y_ranges = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
        ax.set_yticks(y_ranges)
        ax.yaxis.set_major_formatter(FormatStrFormatter('%3.1f'))
        ax.set_ylabel("Pressure (hPa)", size=pu.axes_label_font_size(self.config.figure.subplots))
        if self.ax_opts['add_grid']:
            ax.grid()
"""