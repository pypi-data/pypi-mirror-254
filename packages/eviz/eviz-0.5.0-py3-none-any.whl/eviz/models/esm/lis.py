import logging
import warnings
from dataclasses import dataclass

import numpy as np

from eviz.lib.eviz.figure import Figure
from eviz.models.root import Root
from eviz.models.esm.nuwrf import NuWrf
from eviz.lib.eviz.plot_utils import print_map

warnings.filterwarnings("ignore")


@dataclass
class Lis(Root):
    """ Define LIS specific model data and functions.
    """

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        super().__post_init__()
        self.nu = NuWrf(self.config)

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
                    # TODO: Is ds_index really necessary?
                    self.config.ds_index = s
                    self.config.findex = file_index
                    self.config.pindex = field_num
                    self.config.axindex = 0
                    for pt in map_params[i]['to_plot']:
                        self.logger.info(f"Plotting {field_name}, {pt} plot")
                        figure = Figure(self.config, pt)
                        levels = self.config.get_levels(field_name, pt + 'plot')
                        if not levels:
                            self.logger.warning(f' -> No levels specified for {field_name}')
                            field_to_plot = self._get_field_to_plot(field_name, file_index, pt, figure)
                            plotter.single_plots(self.config, field_to_plot=field_to_plot)
                            print_map(self.config, pt, self.config.findex, figure)
                        else:
                            for level in levels:
                                field_to_plot = self._get_field_to_plot(field_name, file_index, pt, figure, level=level)
                                plotter.single_plots(self.config, field_to_plot=field_to_plot, level=level)
                                print_map(self.config, pt, self.config.findex, figure, level=level)

                    field_num += 1

    def _get_field_to_plot(self, field_name, file_index, plot_type, figure, level=None):
        _, ax = figure.get_fig_ax()
        self.config.ax_opts = figure.init_ax_opts(field_name)
        data2d = None
        d = self.source_data['vars'][field_name]
        if 'xt' in plot_type:
            data2d = self._get_xt(d, field_name, time_lev=self.ax_opts['time_lev'])
        elif 'tx' in plot_type:
            data2d = self._get_tx(d, field_name, level=None, time_lev=self.ax_opts['time_lev'])
        elif 'xy' in plot_type:
            data2d = self._get_xy(d, field_name)
        else:
            pass

        xs, ys, extent, central_lon, central_lat = None, None, [], 0.0, 0.0
        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, None, None, field_name, plot_type, file_index, figure, ax
        else:
            lon = self.config.readers['lis'].get_field(self.nu.get_model_coord_name(self.source_name, 'xc'),
                                                       self.config.findex)
            lat = self.config.readers['lis'].get_field(self.nu.get_model_coord_name(self.source_name, 'yc'),
                                                       self.config.findex)
            xs = np.array(lon[0, :])
            ys = np.array(lat[:, 0])
            # Some LIS coordinates are NaN. The following workaround fills out those elements
            # with reasonable values:
            idx = np.argwhere(np.isnan(xs))
            for i in idx:
                xs[i] = xs[i - 1] + self._global_attrs["DX"] / 1000.0 / 100.0
            idx = np.argwhere(np.isnan(ys))
            for i in idx:
                ys[i] = ys[i - 1] + self._global_attrs["DY"] / 1000.0 / 100.0

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
        if 'xt' in plot_type:
            data2d = self._get_xt(d, field_name, time_lev=self.ax_opts['time_lev'])
        elif 'tx' in plot_type:
            data2d = self._get_tx(d, field_name, level=None, time_lev=self.ax_opts['time_lev'])
        elif 'xy' in plot_type:
            data2d = self.__get_xy(d, field_name)
        else:
            pass

        xs, ys = None, None
        if 'xt' in plot_type or 'tx' in plot_type:
            return data2d, xs, ys, field_name, plot_type
        else:
            lon = self.config.readers['lis'].get_field(self.nu.get_model_coord_name(self.source_name, 'xc'),
                                                       self.config.findex)
            lat = self.config.readers['lis'].get_field(self.nu.get_model_coord_name(self.source_name, 'yc'),
                                                       self.config.findex)
            xs = np.array(lon[0, :])
            ys = np.array(lat[:, 0])
            # Some LIS coordinates are NaN. The following workaround fills out those elements
            # with reasonable values:
            idx = np.argwhere(np.isnan(xs))
            for i in idx:
                xs[i] = xs[i - 1] + self._global_attrs["DX"] / 1000.0 / 100.0
            idx = np.argwhere(np.isnan(ys))
            for i in idx:
                ys[i] = ys[i - 1] + self._global_attrs["DY"] / 1000.0 / 100.0

            return data2d, xs, ys, field_name, plot_type

    def _calculate_diff(self, name1, name2, ax_opts):
        """ Helper method for get_diff_data """
        d1 = self._get_data(name1, ax_opts, 0)
        d2 = self._get_data(name2, ax_opts, 1)
        d1 = self._apply_conversion(d1, name1).squeeze()
        d2 = self._apply_conversion(d2, name2).squeeze()
        return d1 - d2

    def _get_data(self, field_name, ax_opts, pid):
        d = self.config.readers[0].get_field(field_name, self.config.findex)
        # Only XY plots and top layer
        return self._get_xy(d, field_name, level=0, time_lev=ax_opts['time_lev'])

    def _get_xy(self, d, name, level=0, time_lev=0):
        """ Extract XY slice from N-dim data field"""
        if d is None:
            return
        data2d = d.squeeze()

        dim = self.nu.get_dd(self.source_name, self.source_data, 'zc', name)
        if dim:
            data2d = eval(f"data2d.isel({dim}=level)")
        if self.nu.get_model_dim_name(self.source_name, 'tc') in d.dims:
            num_times = eval(f"np.size(d.{self.nu.get_model_dim_name(self.source_name, 'tc')})")
            if self.ax_opts['tave'] and num_times > 1:
                self.logger.debug(f"Averaging over {num_times} time levels.")
                data2d = self._apply_mean(data2d, level)
                return self._apply_conversion(data2d, name)
            else:
                data2d = eval(f"d.isel({self.nu.get_model_dim_name(self.source_name, 'tc')}=time_lev)")
        return self._apply_conversion(data2d, name)

    @staticmethod
    def __get_xy(d, name):
        """ Extract XY slice from N-dim data field"""
        if d is None:
            return
        dlength = len(d.shape)
        if dlength == 2:
            return d[:, :]
        if dlength == 3:
            return d[0, :, :]
        if dlength == 4:
            return d[0, 0, :, :]

    # TODO: put in nuwrf_utils.py
    def _get_field(self, name, data):
        try:
            return data[name]
        except Exception as e:
            self.logger.error('key error: %s, not found' % str(e))
            return None

    def get_field_dim_name(self, dim_name, field_name):
        d = self.config.readers[0].get_field(field_name, self.config.findex)
        field_dims = list(d['ptr'][field_name].dims)
        names = self.nu.get_model_dim_name(self.source_name, dim_name).split(',')
        common = list(set(names).intersection(field_dims))
        dim = list(common)[0] if common else None
        return dim

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
                lev_to_plot = int(np.where(d.coords[self.nu.get_model_dim_name(self.source_name, 'zc')].values == level)[0])
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
