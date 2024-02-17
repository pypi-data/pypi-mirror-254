from dataclasses import dataclass
import logging
import warnings
import sys
import numpy as np
import xarray as xr

from eviz.lib.data.processor import Interp
from eviz.models.root import Root

warnings.filterwarnings("ignore")


@dataclass
class Generic(Root):
    """ The generic class contains definitions for handling generic ESM data, that is 2D, 3D, and 4D
     field data. This is typically not the case for observational data which may be unstructured and very
     non-standard in its internal arrangement.
     Specific model functionality should be overridden in subclasses.
    """
    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        super().__post_init__()

    def _get_field_to_plot(self, source_data, field_name, file_index, plot_type, figure, level=None) -> tuple:
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

    def _get_field_to_plot_compare(self, source_data,
                                   field_name, file_index, plot_type, figure, ax=None, level=None) -> tuple:
        if ax is None:
            _, ax = figure.get_fig_ax()
        dim1, dim2 = self.config.get_dim_names(plot_type)
        data2d = None
        if self.config.ax_opts['is_diff_field']:
            proc = Interp(self.config, source_data)
            data2d, xx, yy = proc.regrid(self.field_names, ax, level, plot_type)
            return data2d, xx, yy, self.field_names[0], plot_type, file_index, figure, ax
        else:
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
        # translate global domain

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
        # calculate total column
        if self.config.ax_opts['zave']:
            self.logger.debug(f"Averaging over vertical levels.")
            data2d = self._apply_mean(data2d, level='all')
            return self._apply_conversion(data2d, name)
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
            if level == 'all':
                data2d = d.mean(dim=self.config.get_model_dim_name('zc'))
            else:
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

    def _get_field_for_simple_plot(self, model_data, field_name, plot_type):
        name = self.config.source_names[self.config.ds_index]
        dim1, dim2 = self.config.get_dim_names(plot_type)
        # dim1 = self.config.meta_coords['xc'][name]
        # dim2 = self.config.meta_coords['yc'][name]
        if 'yz' in plot_type:
            dim1 = self.config.meta_coords['yc'][name]
            dim2 = self.config.meta_coords['zc'][name]
        d = model_data['vars']

        if 'yz' in plot_type:
            data2d = self._get_yz_simple(d, field_name)
        elif 'xy' in plot_type:
            data2d = self._get_xy_simple(d, field_name, 0)
        else:
            self.logger.error(f'[{plot_type}] plot: Please create specifications file.')
            sys.exit()

        coords = data2d.coords
        return data2d, coords[dim1], coords[dim2], field_name, plot_type

    def _get_xy_simple(self, d, name, level):
        """ Extract XY slice from N-dim data field"""
        if d is None:
            return
        data2d = d[name].squeeze()
        # Hackish
        if len(data2d.shape) == 4:
            data2d = eval(f"data2d.isel({self.config.get_model_dim_name('tc')}=0)")
        if len(data2d.shape) == 3:
            if self.config.get_model_dim_name('tc') in data2d.dims:
                data2d = eval(f"data2d.isel({self.config.get_model_dim_name('tc')}=0)")
            else:
                data2d = eval(f"data2d.isel({self.config.get_model_dim_name('zc')}=0)")
        return data2d

    def _get_yz_simple(self, d, name, time_lev=0):
        """ Create YZ slice from N-dim data field"""
        if d is None:
            return
        data2d = d[name].squeeze()
        if len(data2d.shape) == 4:
            data2d = eval(f"data2d.isel({self.config.get_model_dim_name('tc')}=0)")
        data2d = data2d.mean(dim=self.config.get_model_dim_name('xc'))
        return data2d
