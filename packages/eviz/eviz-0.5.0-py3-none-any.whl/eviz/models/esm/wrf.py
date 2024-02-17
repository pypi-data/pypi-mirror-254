import sys
from dataclasses import dataclass
import numpy as np
import logging
import warnings
from matplotlib import pyplot as plt

from eviz.lib.eviz.figure import Figure
from eviz.lib.eviz.plot_utils import print_map
from eviz.models.root import Root
from eviz.models.esm.nuwrf import NuWrf

warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)


@dataclass
class Wrf(Root):
    """ Define NUWRF specific model data and functions.
    """

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        super().__post_init__()
        self.p_top = None
        self.nu = NuWrf(self.config)

    def _init_domain(self):
        """ Approximate unknown fields """
        # Create sigma->pressure dictionary
        # model_top + sigma * (surf_pressure - model_top)
        self.p_top = self.source_data['vars']['P_TOP'][0] / 1e5  # mb
        self.eta_full = np.array(self.source_data['vars']['ZNW'][0])
        self.eta_mid = np.array(self.source_data['vars']['ZNU'][0])
        self.levf = np.empty(len(self.eta_full))
        self.levs = np.empty(len(self.eta_mid))
        i = 0
        for s in self.eta_full:
            if s > 0:
                self.levf[i] = int(self.p_top + s * (1000 - self.p_top))
            else:
                self.levf[i] = self.p_top + s * (1000 - self.p_top)
            i += 1
        i = 0
        for s in self.eta_mid:
            if s > 0:
                self.levs[i] = int(self.p_top + s * (1000 - self.p_top))
            else:
                self.levs[i] = self.p_top + s * (1000 - self.p_top)
            i += 1

    @property
    def global_attrs(self):
        return self._global_attrs

    def _simple_plots(self, plotter):
        map_params = self.config.map_params
        field_num = 0
        self.config.findex = 0
        for i in map_params.keys():
            field_name = map_params[i]['field']
            source_name = map_params[i]['source_name']
            self.source_name = source_name
            filename = map_params[i]['filename']
            file_index = self.config.get_file_index(filename)
            self.source_data = self.config.readers[source_name].read_data(filename)
            self._global_attrs = self.nu.set_global_attrs(source_name, self.source_data['attrs'])
            if not self.p_top:
                self._init_domain()
            self.config.findex = file_index
            self.config.pindex = field_num
            self.config.axindex = 0
            for pt in map_params[i]['to_plot']:
                self.logger.info(f"Plotting {field_name}, {pt} plot")
                field_to_plot = self._get_field_for_simple_plot(field_name, pt)
                plotter.simple_plot(self.config, field_to_plot)
            field_num += 1

    def _single_plots(self, plotter):
        for s in range(len(self.config.source_names)):
            map_params = self.config.map_params
            field_num = 0
            for i in map_params.keys():
                source_name = map_params[i]['source_name']
                if source_name == self.config.source_names[s]:
                    field_name = map_params[i]['field']
                    self.source_name = source_name
                    filename = map_params[i]['filename']
                    file_index = field_num  # self.config.get_file_index(filename)
                    self.source_data = self.config.readers[source_name].read_data(filename)
                    self._global_attrs = self.source_data['attrs']
                    if not self.p_top:
                        self._init_domain()
                    # TODO: Is ds_index really necessary?
                    self.config.ds_index = s
                    self.config.findex = file_index
                    self.config.pindex = field_num
                    self.config.axindex = 0
                    for pt in map_params[i]['to_plot']:
                        self.logger.info(f"Plotting {field_name}, {pt} plot")
                        figure = Figure(self.config, pt)
                        if 'xy' in pt:
                            levels = self.config.get_levels(field_name, pt + 'plot')
                            if not levels:
                                self.logger.warning(f' -> No levels specified for {field_name}')
                                continue
                            for level in levels:
                                field_to_plot = self._get_field_to_plot(field_name, file_index, pt, figure, level=level)
                                plotter.single_plots(self.config, field_to_plot=field_to_plot, level=level)
                                print_map(self.config, pt, self.config.findex, figure, level=level)

                        else:
                            field_to_plot = self._get_field_to_plot(field_name, file_index, pt, figure)
                            plotter.single_plots(self.config, field_to_plot=field_to_plot)
                            print_map(self.config, pt, self.config.findex, figure)

                    field_num += 1

    def _get_field_to_plot(self, field_name, file_index, plot_type, figure, level=None):
        _, ax = figure.get_fig_ax()
        self.config.ax_opts = figure.init_ax_opts(field_name)
        dim1, dim2 = self.nu.coord_names(self.source_name, self.source_data,
                                         field_name, plot_type)
        data2d = None
        d = self.source_data['vars'][field_name]
        if 'yz' in plot_type:
            data2d = self._get_yz(d, field_name, time_lev=self.config.ax_opts['time_lev'])
        elif 'xt' in plot_type:
            data2d = self._get_xt(d, field_name, time_lev=self.ax_opts['time_lev'])
        elif 'tx' in plot_type:
            data2d = self._get_tx(d, field_name, level=None, time_lev=self.ax_opts['time_lev'])
        elif 'xy' in plot_type or 'polar' in plot_type:
            data2d = self._get_xy(d, field_name, level=level, time_lev=self.config.ax_opts['time_lev'])
        else:
            pass

        xs, ys, extent, central_lon, central_lat = None, None, [], 0.0, 0.0
        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, None, None, field_name, plot_type, file_index, figure, ax
        elif 'yz' in plot_type:
            xs = np.array(self._get_field(dim1[0], d)[0, :][:, 0])
            ys = self.levs
            latN = max(xs[:])
            latS = min(xs[:])
            self.config.ax_opts['extent'] = [None, None, latS, latN]
            return data2d, xs, ys, field_name, plot_type, file_index, figure, ax
        else:
            xs = np.array(self._get_field(dim1[0], data2d)[0, :])
            ys = np.array(self._get_field(dim2[0], data2d)[:, 0])
            latN = max(ys[:])
            latS = min(ys[:])
            lonW = min(xs[:])
            lonE = max(xs[:])
            self.config.ax_opts['extent'] = [lonW, lonE, latS, latN]
            self.config.ax_opts['central_lon'] = np.mean(self.config.ax_opts['extent'][:2])
            self.config.ax_opts['central_lat'] = np.mean(self.config.ax_opts['extent'][2:])
            return data2d, xs, ys, field_name, plot_type, file_index, figure, ax

    def _get_field_for_simple_plot(self, field_name, plot_type):
        data2d = None
        d = self.source_data['vars'][field_name]
        dim1, dim2 = self.nu.coord_names(self.source_name, self.source_data,
                                         field_name, plot_type)
        if 'yz' in plot_type:
            data2d = self.__get_yz(d, field_name)
        elif 'xy' in plot_type:
            data2d = self.__get_xy(d, field_name, level=0)
        else:
            pass

        xs, ys, extent, central_lon, central_lat = None, None, [], 0.0, 0.0
        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, None, None, field_name, plot_type
        elif 'yz' in plot_type:
            xs = np.array(self._get_field(dim1, d)[0, :][:, 0])
            ys = self.levs
            return data2d, xs, ys, field_name, plot_type
        else:
            xs = np.array(self._get_field(dim1, data2d)[0, :])
            ys = np.array(self._get_field(dim2, data2d)[:, 0])
            return data2d, xs, ys, field_name, plot_type

    def dim_names(self, field_name, pid):
        """ Get WRF dim names based on field and plot type

        Parameters:
            field_name(str) : Field name associated with this plot
            pid (str) : plot type

        """
        dims = []
        d = self.source_data['vars'][field_name]
        stag = d.stagger
        xsuf, ysuf, zsuf = "", "", ""
        if stag == "X":
            xsuf = "_stag"
        elif stag == "Y":
            ysuf = "_stag"
        elif stag == "Z":
            zsuf = "_stag"

        xc = self.nu.get_dd(self.source_name, self.source_data, 'xc', field_name)
        if xc:
            dims.append(xc + xsuf)

        yc = self.nu.get_dd(self.source_name, self.source_data, 'yc', field_name)
        if yc:
            dims.append(yc + ysuf)

        zc = self.nu.get_dd(self.source_name, self.source_data, 'zc', field_name)
        if zc:
            dims.append(zc + zsuf)

        tc = self.nu.get_dd(self.source_name, self.source_data, 'tc', field_name)
        if tc:
            dims.append(tc)

        # Maps are 2D plots, so we only need - at most - 2 dimensions, depending on plot type
        dim1, dim2 = None, None
        if 'yz' in pid:
            dim1 = dims[1]
            dim2 = dims[2]
        elif 'xt' in pid:
            dim1 = dims[3]
        elif 'tx' in pid:
            dim1 = dims[0]
            dim2 = dims[3]
        else:
            dim1 = dims[0]
            dim2 = dims[1]
        return dim1, dim2

    def _get_xy(self, d, name, level, time_lev=0):
        """ Extract XY slice from N-dim data field"""
        if d is None:
            return
        data2d = d.squeeze()
        level = int(level)
        if self.nu.get_model_dim_name(self.source_name, 'tc') in d.dims:
            num_times = eval(f"np.size(d.{self.nu.get_model_dim_name(self.source_name, 'tc')})")
            if self.config.ax_opts['tave'] and num_times > 1:
                self.logger.debug(f"Averaging over {num_times} time levels.")
                data2d = self._apply_mean(data2d, level)
                return self._apply_conversion(data2d, name)
            else:
                data2d = eval(f"d.isel({self.nu.get_model_dim_name(self.source_name, 'tc')}=time_lev)")

        data2d = data2d.squeeze()
        zname = self.nu.get_field_dim_name(self.source_name, self.source_data, 'zc', name)
        if zname in data2d.dims:
            # TODO: Make soil_layer configurable
            soil_layer = 0
            if 'soil' in zname:
                data2d = eval(f"data2d.isel({zname}=soil_layer)")
            else:
                difference_array = np.absolute(self.levs - level)
                index = difference_array.argmin()
                lev_to_plot = self.levs[index]
                self.logger.debug(f'Level to plot: {lev_to_plot} at index {index}')
                data2d = eval(f"data2d.isel({zname}=index)")
        return self._apply_conversion(data2d, name)

    def _get_yz(self, d, name, time_lev=0):
        """ Create YZ slice from N-dim data field"""
        d = d.squeeze()
        if self.nu.get_model_dim_name(self.source_name, 'tc') in d.dims:
            num_times = eval(f"np.size(d.{self.nu.get_model_dim_name(self.source_name, 'tc')})")
            if self.config.ax_opts['tave'] and num_times > 1:
                self.logger.debug(f"Averaging over {num_times} time levels.")
                data2d = self._apply_mean(d)
            else:
                data2d = eval(f"d.isel({self.nu.get_model_dim_name(self.source_name, 'tc')}=time_lev)")
        else:
            data2d = d
        # WRF specific:
        d = self.source_data['vars'][name]
        stag = d.stagger
        if stag == "X":
            data2d = data2d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'xc') + "_stag")
        else:
            data2d = data2d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'xc'))
        return self._apply_conversion(data2d, name)

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
            lev = self.nu.get_model_dim_name(self.source_name, 'zc')
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

    def basic_plot(self):
        """
        Create a basic plot, i.e. one without specifications.
        """
        for k, field_names in self.config.to_plot.items():
            for field_name in field_names:
                self.fig, self.ax = plt.subplots(nrows=1, ncols=1)
                self._basic_plot(field_name, self.ax)
                self._plot_dest(field_name)

    def _basic_plot(self, field_name, fig, ax, level=0):
        """Helper function for basic_plot() """
        pid = self.config.app_data['inputs'][0]['to_plot'][field_name]
        data2d, dim1, dim2 = self.__get_plot_data(field_name, pid=pid)
        if data2d is None:
            return
        cf = ax.contourf(dim1.values, dim2.values, data2d, cmap=self.config.cmap)
        cbar = self.fig.colorbar(cf, ax=ax,
                                 orientation='vertical',
                                 pad=0.05,
                                 fraction=0.05)
        d = self.config.readers[0].get_field(field_name, self.config.findex)
        dvars = d['vars'][field_name]
        t_label = self.config.meta_attrs['field_name'][self.source_name]
        if self.config.source_names[self.config.findex] in ['lis', 'wrf']:
            dim1_name = self.config.meta_coords['xc'][self.source_name]
            dim2_name = self.config.meta_coords['yc'][self.source_name]
        else:
            dim1_name = dim1.attrs[t_label]
            dim2_name = dim2.attrs[t_label]

        if pid == 'xy':
            ax.set_title(dvars.attrs[t_label])
            ax.set_xlabel(dim1_name)
            ax.set_ylabel(dim2_name)
            if 'units' in dvars.attrs:
                cbar.set_label(dvars.attrs['units'])
        fig.squeeze_fig_aspect(self.fig)

    def __get_plot_data(self, field_name, pid=None):
        dim1 = self.config.meta_coords['xc'][self.source_name]
        dim2 = self.config.meta_coords['yc'][self.source_name]
        data2d = None
        if 'yz' in pid:
            dim1 = self.config.meta_coords['yc'][self.source_name]
            dim2 = self.config.meta_coords['zc'][self.source_name]
        d = self.config.readers[self.source_name].get_field(field_name, self.config.findex)['vars']

        if 'yz' in pid:
            data2d = self.__get_yz(d, field_name)
        elif 'xy' in pid:
            data2d = self.__get_xy(d, field_name, 0)
        else:
            self.logger.error(f'[{pid}] plot: Please create specifications file.')
            sys.exit()

        coords = data2d.coords

        return data2d, coords[dim1], coords[dim2]

    # TODO: put in nuwrf_utils.py
    def _get_field(self, name, data):
        try:
            return data[name]
        except Exception as e:
            self.logger.error('key error: %s, not found' % str(e))
            return None

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
                data2d = d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'tc'))
            else:  # 4D array - we need to select a level
                lev_to_plot = int(
                    np.where(d.coords[self.nu.get_model_dim_name(self.source_name, 'zc')].values == level)[0])
                self.logger.debug("Level to plot:" + str(lev_to_plot))
                # select level
                data2d = eval(f"d.isel({self.nu.get_model_dim_name(self.source_name, 'zc')}=lev_to_plot)")
                data2d = data2d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'tc'))
        else:
            if len(d.dims) == 3:
                data2d = d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'tc'))
            else:
                d = d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'xc'))
                data2d = d.mean(dim=self.nu.get_model_dim_name(self.source_name, 'tc'))
        return data2d
