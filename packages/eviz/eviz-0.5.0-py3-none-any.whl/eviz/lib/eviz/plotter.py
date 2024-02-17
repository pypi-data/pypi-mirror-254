from dataclasses import dataclass
import cftime
import logging
import warnings

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import math
import pandas as pd
from matplotlib import colors
from matplotlib import ticker
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mticker
import matplotlib.gridspec as gridspec
import matplotlib.path as mpath
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import eviz.lib.const as constants
import eviz.lib.eviz.plot_utils as pu
import eviz.lib.utils as u
from eviz.lib.eviz.config import Config
from eviz.lib.data.reader import get_data_coords

warnings.filterwarnings("ignore")

logger = logging.getLogger('plotter')


def _simple_xy_plot_regional(config: Config, data_to_plot: tuple, level=0):
    """Helper function for basic_plot() """
    data2d, dim1, dim2, field_name, plot_type = data_to_plot
    pid = config.app_data['inputs'][0]['to_plot'][field_name]
    if data2d is None:
        return
    fig, ax = plt.subplots(nrows=1, ncols=1)
    if isinstance(dim1, np.ndarray) and isinstance(dim2, np.ndarray):
        cf = ax.contourf(dim1, dim2, data2d, cmap=config.cmap)
    elif isinstance(dim1, xr.DataArray) and isinstance(dim2, xr.DataArray):
        cf = ax.contourf(dim1.values, dim2.values, data2d, cmap=config.cmap)
    else:
        raise TypeError('dim1 and dim2 must be either numpy.ndarrays or xarray.DataArrays.')

    cbar = fig.colorbar(cf, ax=ax,
                        orientation='vertical',
                        pad=0.05,
                        fraction=0.05)
    source_name = config.source_names[config.ds_index]
    dvars = config.readers[source_name].datasets[config.findex]['vars'][field_name]
    dim1_name, dim2_name = config.get_dim_names(plot_type)

    if pid == 'xy':
        ax.set_title(config.meta_attrs['field_name'][source_name])
        ax.set_xlabel(dim1_name)
        ax.set_ylabel(dim2_name)
        if 'units' in dvars.attrs:
            cbar.set_label(dvars.attrs['units'])
    u.squeeze_fig_aspect(fig)
    plt.show()


def _simple_yz_plot_regional(config: Config, data_to_plot: tuple):
    """Helper function for basic_plot() """

    def _prof_plot(ax, data2d, ax_dims):
        if ax_dims[0] == 'zc':
            y0 = data2d.coords[config.meta_coords['yc'][config.model_name](ax_dims[1])][0].values
            y1 = data2d.coords[config.meta_coords['zc'][config.model_name](ax_dims[1])][-1].values
            ax.plot(data2d, data2d.coords[config.meta_coords['yc'][config.model_name]])
            ax.set_ylim(y0, y1)
        elif ax_dims[0] == 'yc':
            dim_names = config.meta_coords['yc'][config.model_name](ax_dims[1]).split(',')
            for i in dim_names:
                if i in data2d.dims:
                    gooddim = i
            ax.plot(data2d, data2d.coords[gooddim].values)


def _simple_xy_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a simple xy (lat-lon) plot """
    source_name = config.source_names[config.ds_index]
    if source_name in ['lis', 'wrf']:
        _simple_xy_plot_regional(config, data_to_plot)
        return

    def shift_columns(arr):
        m, n = arr.shape
        mid = math.ceil(n / 2)
        shifted_arr = np.zeros((m, n), dtype=arr.dtype)
        shifted_arr[:, :mid] = arr[:, mid:]
        shifted_arr[:, mid:] = arr[:, :mid]
        return shifted_arr

    data2d, dim1, dim2, field_name, plot_type = data_to_plot
    dmin = data2d.min(skipna=True).values
    dmax = data2d.max(skipna=True).values
    if dmin < 1:  # TODO: This is hackish, please fix
        levels = np.linspace(dmin, dmax, 10)
    else:
        levels = np.around(np.linspace(dmin, dmax, 10), decimals=1)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    if data2d is None:
        return
    cf = ax.contourf(dim1.values, dim2.values, shift_columns(data2d), cmap=config.cmap)
    co = ax.contour(dim1.values, dim2.values, shift_columns(data2d), levels, linewidths=(1,), origin='lower')
    ax.clabel(co, fmt='%2.1f', colors='w', fontsize=8)
    cbar = fig.colorbar(cf, ax=ax, orientation='vertical', pad=0.05, fraction=0.05)

    if 'field_name' in config.meta_attrs['field_name']:
        t_label = config.meta_attrs['field_name'][config.source_names[config.findex]]
    else:
        t_label = 'name'

    if config.source_names[config.ds_index] in ['lis', 'wrf']:
        dim1_name = config.meta_coords['xc'][config.source_names[config.ds_index]]
        dim2_name = config.meta_coords['yc'][config.source_names[config.ds_index]]
    else:
        try:
            dim1_name = dim1.attrs[t_label]
            dim2_name = dim2.attrs[t_label]
            ax.set_title(data2d.attrs[t_label])
        except KeyError:
            dim1_name = dim1.name
            dim2_name = dim2.name
            ax.set_title(field_name)

    ax.set_xlabel(dim1_name)
    ax.set_ylabel(dim2_name)
    if 'units' in data2d.attrs:
        cbar.set_label(data2d.attrs['units'])


def _simple_sc_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a simple scatter plot """
    data2d, dim1, dim2, field_name, plot_type = data_to_plot
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10), subplot_kw=dict(projection=ccrs.PlateCarree()))
    scat = ax.scatter(dim1, dim2, c=data2d[field_name], cmap='coolwarm', s=50,
                      transform=ccrs.PlateCarree())
    cbar = fig.colorbar(scat, ax=ax, shrink=0.5)
    cbar.set_label("ppb")
    ax.coastlines()
    ax.set_title(f'{field_name}')


def _simple_yz_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a simple yz (zonal-mean) plot """
    source_name = config.source_names[0]
    if source_name in ['lis', 'wrf']:
        _simple_yz_plot_regional(config, data_to_plot)
        return

    data2d, dim1, dim2, field_name, plot_type = data_to_plot
    dmin = data2d.min(skipna=True).values
    dmax = data2d.max(skipna=True).values
    if dmin < 1:  # TODO: This is hackish, please fix
        levels = np.linspace(dmin, dmax, 10)
    else:
        levels = np.around(np.linspace(dmin, dmax, 10), decimals=1)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    if data2d is None:
        return
    cf = ax.contourf(dim1.values, dim2.values, data2d, cmap=config.cmap)
    co = ax.contour(dim1.values, dim2.values, data2d, levels, linewidths=(1,), origin='lower')
    ax.clabel(co, fmt='%2.1f', colors='w', fontsize=8)
    cbar = fig.colorbar(cf, ax=ax, orientation='vertical', pad=0.05, fraction=0.05)
    if 'field_name' in config.meta_attrs['field_name']:
        t_label = config.meta_attrs['field_name'][config.source_names[config.ds_index]]
    else:
        t_label = 'name'
    if config.source_names[config.ds_index] in ['lis', 'wrf']:
        dim1_name = config.meta_coords['xc'][config.source_names[config.ds_index]]
        dim2_name = config.meta_coords['yc'][config.source_names[config.ds_index]]
    else:
        try:
            dim1_name = dim1.attrs[t_label]
            dim2_name = dim2.attrs[t_label]
            ax.set_title(data2d.attrs[t_label])
        except KeyError:
            dim1_name = dim1.name
            dim2_name = dim2.name
            ax.set_title(field_name)

    ax.set_xlabel(dim1_name)
    ax.set_ylabel(dim2_name)
    if 'units' in data2d.attrs:
        cbar.set_label(data2d.attrs['units'])


def _single_xy_plot(config: Config, data_to_plot: tuple, level: int) -> None:
    """ Create a single xy (lat-lon) plot using SPECS data

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
        level (int) : vertical level
    """
    data2d, x, y, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    axes_shape = fig.get_gs_geometry()
    axindex = config.axindex
    if axes_shape == (3, 1):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
        else:
            ax = ax_temp[axindex]
    elif axes_shape == (2, 2):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
            if config.ax_opts['add_extra_field_type']:
                ax = ax_temp[3]
        else:
            ax = ax_temp[axindex]

    logger.debug(f'Plotting {field_name}')
    if data2d is None:
        return

    ax_opts = fig.update_ax_opts(field_name, ax, 'xy', level=level)
    fig.plot_text(field_name, ax, 'xy', level=level, data=data2d)

    if ax_opts['extent']:
        if ax_opts['extent'] == 'conus':
            extent = [-140, -40, 15, 65]  # [lonW, lonE, latS, latN]
        else:
            extent = ax_opts['extent']
    else:
        extent = [-180, 180, -90, 90]

    if ax_opts['use_cartopy']:
        # TODO: Fix this:
        # ax = fig.set_cartopy_latlon_opts(ax, extent)
        ax.set_extent(extent, crs=ccrs.PlateCarree())
        ax = fig.set_cartopy_features(ax)
        cfilled = _filled_contours(config, field_name, ax, x, y, data2d, transform=ccrs.PlateCarree())
    else:
        cfilled = _filled_contours(config, field_name, ax, x, y, data2d)

    if ax_opts['clevs'] is not None:
        if ax_opts['cscale'] is not None:
            contour_format = pu.contour_format_from_levels(pu.formatted_contours(ax_opts['clevs']),
                                                           scale=ax_opts['cscale'])
        else:
            contour_format = pu.contour_format_from_levels(pu.formatted_contours(ax_opts['clevs']))
        _set_colorbar(config, cfilled, fig, ax, ax_opts, findex, field_name, contour_format, data2d)
        _line_contours(fig, ax, ax_opts, x, y, data2d)

    if config.compare and config.ax_opts['is_diff_field']:
        if 'name' in config.spec_data[field_name]:
            name = config.spec_data[field_name]['name']
        else:
            name = data2d.name

        level_text = None
        if config.ax_opts['zave']:
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
        if level_text:
            name = name + level_text
        plt.suptitle(
            name,
            fontstyle='italic',
            fontsize=pu.image_font_size(fig.subplots))

    if config.add_logo:
        ax0 = fig.get_axes()[0]
        pu.add_logo_fig(fig, fig.EVIZ_LOGO)

    # This works well in xy (i.e. lat-lon) plots
    fig.squeeze_fig_aspect(fig.fig)


def _single_scat_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single scatter using SPECS data
        config (Config) : configuration used to specify data sources
        data_to_plot (dict) : dict with plotted data and specs

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
    """
    data2d, x, y, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    logger.debug(f'Plotting {field_name}')
    rc = {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
    with mpl.rc_context(rc=rc):
        if ax_opts['extent']:
            if ax_opts['extent'] == 'conus':
                extent = [-140, -40, 15, 65]  # [lonW, lonE, latS, latN]
            else:
                extent = ax_opts['extent']
        else:
            extent = [-180, 180, -90, 90]

        if ax_opts['use_cartopy']:
            ax = fig.set_cartopy_latlon_opts(ax, extent)
            ax.set_extent(extent, crs=ccrs.PlateCarree())
            ax = fig.set_cartopy_features(ax)
            scat = ax.scatter(x, y, c=data2d[field_name], cmap='coolwarm', s=50, transform=ccrs.PlateCarree())
        else:
            scat = ax.scatter(x, y, c=data2d[field_name], cmap='coolwarm', s=50)

        cbar = fig.fig.colorbar(scat, ax=ax,
                                orientation='horizontal',
                                pad=pu.cbar_pad(fig.subplots),
                                fraction=pu.cbar_fraction(fig.subplots),
                                extendfrac='auto',
                                shrink=0.5)

        if ax_opts['clabel'] is None:
            if 'units' in config.spec_data[field_name]:
                cbar_label = config.spec_data[field_name]['units']
            else:
                try:
                    cbar_label = data_to_plot['vars'][field_name].units
                except:
                    logger.error(f"Please specify {field_name} units in specs file")
                    cbar_label = "n.a."
        else:
            cbar_label = ax_opts['clabel']
        cbar.set_label(cbar_label, size=pu.bar_font_size(fig.subplots))
        for t in cbar.ax.get_xticklabels():
            t.set_fontsize(pu.contour_tick_font_size(fig.subplots))

        ax.set_title(f'{field_name}')


def _single_yz_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single yz (zonal-mean) plot using SPECS data
        Note:
            YZ fields are treated like XY fields where Y->X and Z->Y

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
    """
    data2d, x, y, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    axes_shape = fig.get_gs_geometry()
    axindex = config.axindex
    if axes_shape == (3, 1):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
        else:
            ax = ax_temp[axindex]
    elif axes_shape == (2, 2):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
            if config.ax_opts['add_extra_field_type']:
                ax = ax_temp[3]
        else:
            ax = ax_temp[axindex]

    logger.debug(f'Plotting {field_name}')
    if data2d is None:
        return
    ax_opts = fig.update_ax_opts(field_name, ax, 'yz', level=0)
    # TODO: pass fig.fig
    fig.plot_text(field_name, ax, 'yz', level=None, data=data2d)

    if ax_opts['profile_dim']:
        prof_dim = ax_opts['profile_dim']
        dep_var = None
        if prof_dim == 'yc':
            dep_var = 'zc'
        if prof_dim == 'zc':
            dep_var = 'yc'
        prof_dim = ax_opts['profile_dim']
        data2d = data2d.mean(dim=config.get_model_dim_name(prof_dim))
        _single_prof_plot(config, data2d, fig, ax, ax_opts, (prof_dim, dep_var))
    else:
        cfilled = _filled_contours(config, field_name, ax, x, y, data2d)

        contour_format = pu.contour_format_from_levels(pu.formatted_contours(ax_opts['clevs']),
                                                       scale=ax_opts['cscale'])

        ylabels = ax.get_yticklabels()
        for label in ylabels:
            label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

        xlabels = ax.get_xticklabels()
        for label in xlabels:
            label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

        _set_ax_ranges(config, field_name, fig, ax, ax_opts, y, findex)

        _line_contours(fig, ax, ax_opts, x, y, data2d)

        _set_colorbar(config, cfilled, fig, ax, ax_opts, findex, field_name, contour_format, data2d)

    if config.compare and config.ax_opts['is_diff_field']:
        if 'name' in config.spec_data[field_name]:
            name = config.spec_data[field_name]['name']
        else:
            name = data2d.name
        plt.suptitle(
            name,
            fontstyle='italic',
            fontsize=pu.image_font_size(fig.subplots))

    if config.add_logo:
        pu.add_logo(fig, fig.EVIZ_LOGO)
        # pu.watermark(ax, fig.EVIZ_LOGO)


def _set_ax_ranges(config, field_name, fig, ax, ax_opts, y, findex):
    """ Create a sensible number of vertical levels """
    source_name = config.source_names[config.ds_index]
    dvars = config.readers[source_name].datasets[findex]['vars'][field_name]
    if 'units' in config.spec_data[field_name]:
        units = config.spec_data[field_name]['units']
    else:
        try:
            units = dvars.units
        except Exception as e:
            logger.error(f"{e}: Please specify {field_name} units in specs file")
            units = "n.a."

    # units = config.readers[0].datasets[config.ds_index]['coords']['lev'].units
    y_ranges = np.array([1000, 700, 500, 300, 200, 100])
    if units == "Pa":
        y_ranges = y_ranges * 100
        if y.min() <= 1000.0:
            y_ranges = np.append(y_ranges, np.array([70, 50, 30, 20, 10]) * 100)
        if y.min() <= 20.:
            y_ranges = np.append(y_ranges, np.array([7, 5, 3, 2, 1, .7, .5, .3, .2, .1]) * 100)
        if y_ranges[-1] != y.min():
            y_ranges = np.append(y_ranges, y.min())
    else:
        if y.min() <= 10.0:
            y_ranges = np.append(y_ranges, np.array([70, 50, 30, 20, 10]))
        if y.min() <= 0.2:
            y_ranges = np.append(y_ranges, np.array([7, 5, 3, 2, 1, .7, .5, .3, .2, .1]))
        if y_ranges[-1] != y.min():
            y_ranges = np.append(y_ranges, y.min())

    lo_z, hi_z = y_ranges.max(), y_ranges.min()
    if 'zrange' in config.spec_data[field_name]['yzplot']:
        if not config.spec_data[field_name]['yzplot']['zrange']:
            pass  # if nothing specified (it happens)
        else:
            lo_z = config.spec_data[field_name]['yzplot']['zrange'][0]
            hi_z = config.spec_data[field_name]['yzplot']['zrange'][1]
            if hi_z >= lo_z:
                logger.error(f"Upper level value ({hi_z}) must be less than low level value ({lo_z})")
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
    ax.set_yscale(ax_opts['zscale'])
    ax.yaxis.set_minor_formatter(NullFormatter())
    if 'linear' in ax_opts['zscale']:
        y_ranges = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
        if 'Pa' in config.readers[source_name].datasets[findex]['coords']['lev'].units:
            y_ranges = y_ranges * 100
    ax.set_yticks(y_ranges)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%3.1f'))
    ax.set_ylabel("Pressure (" + units + ")", size=pu.axes_label_font_size(fig.subplots))
    if ax_opts['add_grid']:
        ax.grid()


def _single_polar_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single xt (time-series) plot using SPECS data

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
    """
    source_name = config.source_names[config.ds_index]
    data2d, x, y, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    if np.shape(ax_temp) == (3,):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
        else:
            ax = ax_temp[findex]
    elif np.shape(ax_temp) == (2, 2):
        if ax_opts['is_diff_field']:
            ax = ax_temp[1, 0]
            if config.ax_opts['add_extra_field_type']:
                ax = ax_temp[1, 1]
        else:
            ax = ax_temp[0, findex]

    logger.debug(f'Plotting {field_name}')
    if data2d is None:
        return

    ax_opts = fig.update_ax_opts(field_name, ax, 'polar')
    fig.plot_text(field_name, ax, 'polar', data=data2d)

    if ax_opts['use_pole'] == 'south':
        plotcrs = ccrs.SouthPolarStereo(central_longitude=0.0)
    else:
        plotcrs = ccrs.NorthPolarStereo(central_longitude=-100.0)

    fig.gs = gridspec.GridSpec(2, 1, height_ratios=[1, .02],
                               bottom=.07, top=.99, hspace=0.01, wspace=0.01)

    ax = plt.subplot(fig.gs[0], projection=plotcrs)
    fig.plot_text(field_name, ax, 'polar', data=data2d)

    dmin = data2d.min(skipna=True).values
    dmax = data2d.max(skipna=True).values

    logger.debug(f"Field: {field_name}; Min:{dmin:.2f}; Max:{dmax:.2f}")

    _create_clevs(field_name, ax_opts, data2d)
    clevs = pu.formatted_contours(ax_opts['clevs'])
    contour_format = pu.contour_format_from_levels(clevs)

    extend_value = "both"
    if ax_opts['clevs'][0] == 0:
        extend_value = "max"
    norm = colors.BoundaryNorm(ax_opts['clevs'], ncolors=256, clip=False)

    if ax_opts['use_pole'] == 'south':
        ax.set_extent([-180, 180, -90, -60], ccrs.PlateCarree())
    else:
        ax.set_extent([-180, 180, 60, 90], ccrs.PlateCarree())

    ax = fig.set_cartopy_features(ax)
    if ax_opts['boundary']:
        theta = np.linspace(0, 2 * np.pi, 100)
        center, radius = [0.5, 0.5], 0.5
        verts = np.vstack([np.sin(theta), np.cos(theta)]).T
        circle = mpath.Path(verts * radius + center)
        ax.set_boundary(circle, transform=ax.transAxes)

    data_transform = ccrs.PlateCarree()
    cfilled = ax.contourf(x, y, data2d,
                          cmap=ax_opts['use_cmap'],
                          levels=ax_opts['clevs'],
                          transform=data_transform,
                          extend=extend_value,
                          norm=norm)

    cax = plt.subplot(fig.gs[1])
    cbar = plt.colorbar(cfilled, cax=cax, orientation='horizontal', extend='max', extendrect=True)
    dvars = config.readers[source_name].datasets[findex]['vars'][field_name]
    if 'units' in config.spec_data[field_name]:
        units = config.spec_data[field_name]['units']
    else:
        try:
            units = dvars.units
        except Exception as e:
            logger.error(f"{e}: Please specify {field_name} units in specs file")
            units = "n.a."
    if ax_opts['clabel'] is None:
        cbar_label = units
    else:
        cbar_label = ax_opts['clabel']
    cbar.set_label(cbar_label, size=pu.bar_font_size(fig.subplots))

    if ax_opts['add_grid']:
        ax.gridlines()

    # better line contours
    if ax_opts['line_contours']:
        clines = ax.contour(x, y, data2d, levels=ax_opts['clevs'], colors="black",
                            linewidths=0.5, alpha=0.5, linestyles='solid', transform=data_transform)
        ax.clabel(clines, inline=1, fontsize=pu.contour_label_size(fig.subplots),
                  inline_spacing=10, colors="black", fmt=contour_format, rightside_up=True, use_clabeltext=True)
    else:
        _ = ax.contour(x, y, data2d, linewidths=0.0)

    if config.add_logo:
        # _line_contours(ax, x, y, data2d)
        pu.add_logo_fig(fig, fig.EVIZ_LOGO)
        # pu.watermark(ax, fig.EVIZ_LOGO)

    if config.compare:
        suf = " @" + str(level) + "mb"
        d = config.readers[source_name].read_data()
        fig.suptitle(
            d['vars'][field_name].long_name + suf,
            fontsize=pu.image_font_size(fig.subplots))
    else:
        if 'name' in config.spec_data[field_name]:
            fig.fig.suptitle(config.spec_data[field_name]['name'])

    # This works well in xy (i.e. lat-lon) plots
    if fig.subplots != (1, 1):
        fig.squeeze_fig_aspect(fig)


def _single_xt_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single xt (time-series) plot using SPECS data

    Note:
        XT plots are 2D plots where the variable, X, is averaged over all space,
        is plotted against time, T.

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
    """

    data2d, _, _, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    if np.shape(ax_temp) == (3,):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
        else:
            ax = ax_temp[findex]
    elif np.shape(ax_temp) == (2, 2):
        if ax_opts['is_diff_field']:
            ax = ax_temp[1, 0]
            if config.ax_opts['add_extra_field_type']:
                ax = ax_temp[1, 1]
        else:
            ax = ax_temp[0, findex]

    logger.debug(f'Plotting {field_name}')
    if data2d is None:
        return
    ax_opts = fig.update_ax_opts(field_name, ax, 'xt')
    fig.plot_text(field_name, ax, 'xt', data=data2d)

    _time_series_plot(config, ax, ax_opts, fig, data2d, field_name)

    dvars = config.readers[config.source_names[config.ds_index]].datasets[findex]['vars'][field_name]
    if 'units' in config.spec_data[field_name]:
        units = config.spec_data[field_name]['units']
    else:
        try:
            units = dvars.units
        except Exception as e:
            logger.error(f"{e}: Please specify {field_name} units in specs file")
            units = "n.a."
    ax.set_ylabel(units)

    if fig.subplots != (1, 1):
        fig.squeeze_fig_aspect(fig)


def _time_series_plot(config, ax, ax_opts, fig, data2d, field_name):
    with mpl.rc_context(ax_opts['plot_linestyle']):
        dmin = data2d.min(skipna=True).values
        dmax = data2d.max(skipna=True).values
        logger.debug(f"dmin: {dmin}, dmax: {dmax}")

        # t0 = data2d.coords[config.get_model_dim_name('tc')][0].values   # need datetime64
        # t1 = data2d.coords[config.get_model_dim_name('tc')][-1].values

        # Just in case, for non-standard datetimes:
        time_coords = data2d.coords[config.get_model_dim_name('tc')].values
        if isinstance(time_coords[0], cftime._cftime.DatetimeNoLeap):
            time_coords = pd.to_datetime(data2d.coords[config.get_model_dim_name('tc')].dt.strftime("%Y%m%d"))

        t0 = time_coords[0]
        t1 = time_coords[-1]

        if 'mean_type' in config.spec_data[field_name]['xtplot']:
            if 'season' in config.spec_data[field_name]['xtplot']['mean_type']:
                ax.contourf(data2d.coords[config.get_model_dim_name('tc')], data2d, col='season', col_wrap=2)
            else:
                ax.plot(data2d.coords[config.get_model_dim_name('tc')], data2d)
        else:
            ax.plot(time_coords, data2d)

        ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))
        fig.fig.autofmt_xdate()
        ax.set_xlim(t0, t1)
        davg = 0.5 * (abs(dmin - dmax))
        ax.set_ylim([dmin - davg, dmax + davg])
        # TODO: fix this
        # ax.set_ylabel(config.readers[0].datasets[config.ds_index]['vars'][field_name].units)
        ax.set_ylabel('units')

        ylabels = ax.get_yticklabels()
        for label in ylabels:
            label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

        xlabels = ax.get_xticklabels()
        for label in xlabels:
            label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

        if ax_opts['add_grid']:
            ax.grid()


def _single_prof_plot(config, data2d, fig, ax, ax_opts, ax_dims) -> None:
    """ Create a single prof (vertical profile) plot using SPECS data"""
    if ax_dims[0] == 'zc':
        y0 = data2d.coords[config.get_model_dim_name(ax_dims[1])][0].values
        y1 = data2d.coords[config.get_model_dim_name(ax_dims[1])][-1].values
        ax.plot(data2d, data2d.coords[config.get_model_dim_name('yc')])
        ax.set_ylim(y0, y1)
    elif ax_dims[0] == 'yc':
        y0 = data2d.coords[config.get_model_dim_name(ax_dims[1])][0].values
        y1 = data2d.coords[config.get_model_dim_name(ax_dims[1])][-1].values
        ax.plot(data2d, data2d.coords[config.get_model_dim_name('zc')])
        ax.set_ylim(y0, y1)

    ax.set_yscale(ax_opts['zscale'])
    ax.yaxis.set_minor_formatter(NullFormatter())
    if 'linear' in ax_opts['zscale']:
        y_ranges = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
        ax.set_yticks(y_ranges)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%3.1f'))
    if ax_opts['add_grid']:
        ax.grid()

    ylabels = ax.get_yticklabels()
    for label in ylabels:
        label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

    xlabels = ax.get_xticklabels()
    for label in xlabels:
        label.set_fontsize(pu.axis_tick_font_size(fig.subplots))

    if ax_opts['add_grid']:
        ax.grid()


def _single_tx_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single tx (Hovmoller) plot using SPECS data

    Note:
        A Hovmoller plot shows zonal and meridional shifts in a given field
        Can also be used to plot time evolution of atmospheric profiles
        that vary spatially.

    Parameters:
        config (Config) : configuration used to specify data sources
        data_to_plot (tuple) : dict with plotted data and specs
    """
    source_name = config.source_names[config.ds_index]
    data2d, _, _, field_name, plot_type, findex, fig, ax_temp = data_to_plot
    ax_opts = config.ax_opts
    ax = ax_temp
    if np.shape(ax_temp) == (3,):
        if ax_opts['is_diff_field']:
            ax = ax_temp[2]
        else:
            ax = ax_temp[findex]
    elif np.shape(ax_temp) == (2, 2):
        if ax_opts['is_diff_field']:
            ax = ax_temp[1, 0]
            if config.ax_opts['add_extra_field_type']:
                ax = ax_temp[1, 1]
        else:
            ax = ax_temp[0, findex]

    logger.debug(f'Plotting {field_name}')
    if data2d is None:
        return
    ax_opts = fig.update_ax_opts(field_name, ax, 'tx')

    dmin = data2d.min(skipna=True).values
    dmax = data2d.max(skipna=True).values

    logger.debug(f"Field: {field_name}; Min:{dmin}; Max:{dmax}")

    if ax_opts['create_clevs']:
        if dmin < 1:  # TODO: This is hackish, please fix
            ax_opts['clevs'] = np.linspace(dmin, dmax, ax_opts['num_clevs'])
        else:
            ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=1)
        logger.debug(ax_opts['clevs'])

    clevs = pu.formatted_contours(ax_opts['clevs'])

    extend_value = "both"
    if ax_opts['clevs'][0] == 0:
        extend_value = "max"
    norm = colors.BoundaryNorm(ax_opts['clevs'], ncolors=256, clip=False)

    # Get times and make array of datetime objects
    vtimes = data2d.time.values.astype('datetime64[ms]').astype('O')
    # Specify longitude values
    lons = get_data_coords(config.source_names[config.ds_index], data2d, 'xc')

    # Start figure
    x_tick_labels = [u'0\N{DEGREE SIGN}E', u'90\N{DEGREE SIGN}E',
                     u'180\N{DEGREE SIGN}E', u'90\N{DEGREE SIGN}W',
                     u'0\N{DEGREE SIGN}E']

    ax[0].set_extent([0, 357.5, 35, 65], ccrs.PlateCarree(central_longitude=180))
    ax[0].set_yticks([40, 60])
    ax[0].set_yticklabels([u'40\N{DEGREE SIGN}N', u'60\N{DEGREE SIGN}N'])
    ax[0].set_xticks([-180, -90, 0, 90, 180])
    ax[0].set_xticklabels(x_tick_labels)
    ax[0].grid(linestyle='dotted', linewidth=2)
    #
    ax[0].add_feature(cfeature.COASTLINE.with_scale('50m'))
    ax[0].add_feature(cfeature.LAKES.with_scale('50m'), color='black', linewidths=0.5)
    plt.title(config.get_file_description(config.file_list[0]), loc='right')

    if ax_opts['torder']:
        ax[1].invert_yaxis()  # Reverse the time order

    cfilled = ax[1].contourf(lons, vtimes, data2d, clevs, norm=norm,
                             cmap=ax_opts['use_cmap'], extend=extend_value)
    clines = ax[1].contour(lons, vtimes, data2d, clevs,
                           levels=ax_opts['clevs'], colors="black",
                           linewidths=0.5, alpha=0.5)

    contour_format = pu.contour_format_from_levels(pu.formatted_contours(ax_opts['clevs']),
                                                   scale=ax_opts['cscale'])
    cbar = plt.colorbar(cfilled, orientation='horizontal', pad=0.1,
                        aspect=50, ticks=ax_opts['clevs'], format=contour_format)
    cbar.ax.tick_params(labelsize=10)

    if ax_opts['clabel'] is None:
        if 'units' in config.spec_data[field_name]:
            cbar_label = config.spec_data[field_name]['units']
        else:
            try:
                cbar_label = config.readers[source_name].datasets[findex]['vars'][field_name].units
            except:
                logger.error(f"Please specify {field_name} units in specs file")
                cbar_label = "n.a."
    else:
        cbar_label = ax_opts['clabel']
    cbar.set_label(cbar_label, size=pu.bar_font_size(fig.subplots))

    # Axes labels
    # labels = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    # ax.set_yticks(np.arange(1, 13))
    ax[1].set_xticks([-180, -90, 0, 90, 180])
    ax[1].set_xticklabels(x_tick_labels)

    if ax_opts['add_grid']:
        kwargs = {'linestyle': '-', 'linewidth': 2}
        ax[1].grid(**kwargs)

    # pu.watermark(ax, fig.EVIZ_LOGO)

    #  TODO: Need SUPTITLE here
    if fig.subplots != (1, 1):
        fig.squeeze_fig_aspect(fig)

    # if config.add_logo:
    #     pu.add_logo_fig(fig, fig.EVIZ_LOGO)


def _single_box_plot(config: Config, data_to_plot: tuple) -> None:
    """ Create a single box plot using SPECS data"""


def _line_contours(fig, ax, ax_opts, x, y, data2d):
    with mpl.rc_context(ax_opts['contour_linestyle']):
        contour_format = pu.contour_format_from_levels(pu.formatted_contours(ax_opts['clevs']),
                                                       scale=ax_opts['cscale'])
        # line contours
        if ax_opts['line_contours']:
            clines = ax.contour(x, y, data2d, levels=ax_opts['clevs'], colors="black", alpha=0.5)
            ax.clabel(clines, inline=1, fontsize=pu.contour_label_size(fig.subplots),
                      colors="black", fmt=contour_format)
        else:
            _ = ax.contour(x, y, data2d, linewidths=0.0)


def _create_clevs(field_name, ax_opts, data2d):
    # If needed, create contour levels
    if ax_opts['create_clevs']:
        dmin = data2d.min(skipna=True).values
        dmax = data2d.max(skipna=True).values
        logger.debug(f"dmin: {dmin}, dmax: {dmax}")
        ax_opts['clevs'] = np.linspace(dmin, dmax, ax_opts['num_clevs'])
        # if abs(dmin - dmax) < 1e-6:  # TODO: This is hackish, please fix
        #     ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=6)
        # elif abs(dmin - dmax) < 1e-3:  # TODO: This is hackish, please fix
        #     ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=4)
        # elif abs(dmin - dmax) < 1e-2:  # TODO: This is hackish, please fix
        #     ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=3)
        # elif abs(dmin - dmax) < 1e-1:  # TODO: This is hackish, please fix
        #     ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=2)
        # else:
        #     ax_opts['clevs'] = np.around(np.linspace(dmin, dmax, ax_opts['num_clevs']), decimals=1)
        logger.debug(f'Created contour levels for {field_name}:')
        logger.debug(ax_opts['clevs'])
    if ax_opts['clevs'][0] == 0.0:
        ax_opts['extend_value'] = "max"


def _filled_contours(config, field_name, ax, x, y, data2d, transform=None):
    """ Plot filled contours"""
    _create_clevs(field_name, config.ax_opts, data2d)

    norm = colors.BoundaryNorm(config.ax_opts['clevs'], ncolors=256, clip=False)

    # filled contours
    if config.compare:  # and config.comparison_plot:
        cmap_str = config.ax_opts['use_diff_cmap']
    else:
        cmap_str = config.ax_opts['use_cmap']

    try:
        cfilled = ax.contourf(x, y, data2d,
                              robust=True,
                              levels=config.ax_opts['clevs'],
                              cmap=cmap_str,
                              extend=config.ax_opts['extend_value'],
                              norm=norm,
                              transform=transform)
    except TypeError:
        cfilled = ax.contourf(x, y, data2d.transpose(),
                              robust=True,
                              levels=config.ax_opts['clevs'],
                              cmap=cmap_str,
                              extend=config.ax_opts['extend_value'],
                              norm=norm,
                              transform=transform)

    cfilled.cmap.set_under('fuchsia')
    cfilled.cmap.set_over('darkred')
    return cfilled


def _set_colorbar(config, cfilled, fig, ax, ax_opts, findex, field_name, contour_format, data2d):
    source_name = config.source_names[config.ds_index]
    dmin = data2d.min(skipna=True).values
    dmax = data2d.max(skipna=True).values
    min_exp = int(math.log10(abs(dmin)))
    # max_exp = int(math.log10(abs(dmax)))
    fmt = pu.OOMFormatter(min_exp, math_text=True)
    if config.compare:
        if not config.use_cartopy:
            cbar = pu.colorbar(cfilled)
        else:
            if ax_opts['clevs'] is not None:
                cbar = fig.fig.colorbar(cfilled, ax=ax,
                                        orientation='vertical',
                                        pad=pu.cbar_pad(fig.subplots),
                                        fraction=pu.cbar_fraction(fig.subplots),
                                        ticks=ax_opts['clevs'],
                                        format=fmt,
                                        shrink=pu.cbar_shrink(fig.subplots))
            else:
                cbar = fig.fig.colorbar(cfilled, ax=ax,
                                        orientation='vertical',
                                        pad=pu.cbar_pad(fig.subplots),
                                        fraction=pu.cbar_fraction(fig.subplots),
                                        format=fmt,
                                        shrink=pu.cbar_shrink(fig.subplots))
        for t in cbar.ax.get_yticklabels():
            t.set_fontsize(pu.contour_tick_font_size(fig.subplots))

    else:
        if not config.use_cartopy:
            cbar = pu.colorbar(cfilled)
        else:
            if ax_opts['clevs'] is not None:
                cbar = fig.fig.colorbar(cfilled, ax=ax,
                                        orientation='horizontal',
                                        pad=pu.cbar_pad(fig.subplots),
                                        fraction=pu.cbar_fraction(fig.subplots),
                                        ticks=ax_opts['clevs'],
                                        extendfrac='auto',
                                        format=fmt,
                                        shrink=pu.cbar_shrink(fig.subplots))
            else:
                cbar = fig.fig.colorbar(cfilled, ax=ax,
                                        orientation='horizontal',
                                        pad=pu.cbar_pad(fig.subplots),
                                        fraction=pu.cbar_fraction(fig.subplots),
                                        extendfrac='auto',
                                        format=fmt,
                                        shrink=pu.cbar_shrink(fig.subplots))

    dvars = config.readers[source_name].datasets[findex]['vars'][field_name]
    if 'units' in config.spec_data[field_name]:
        units = config.spec_data[field_name]['units']
    else:
        try:
            units = dvars.units
        except Exception as e:
            logger.error(f"{e}: Please specify {field_name} units in specs file")
            units = "n.a."

    if ax_opts['clabel'] is None:
        cbar_label = units
    else:
        cbar_label = ax_opts['clabel']
    cbar.set_label(cbar_label, size=pu.bar_font_size(fig.subplots))
    for t in cbar.ax.get_xticklabels():
        t.set_fontsize(pu.contour_tick_font_size(fig.subplots))


@dataclass()
class Plotter:
    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    @staticmethod
    def simple_plot(config, data_to_plot):
        """
        Create a basic plot, i.e. one without specifications.
        """
        no_specs_plotter = SimplePlotter()
        no_specs_plotter.plot(config, data_to_plot)
        pu.output_basic(config, data_to_plot[3])


@dataclass()
class SimplePlotter:

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")

    def simple_plot(self, config, field_to_plot):
        self.plot(config, field_to_plot)
        pu.output_basic(config, field_to_plot[3])

    @staticmethod
    def plot(config, field_to_plot):
        """ Create a basic plot (ala ncview)
        Parameters:
            config: Config
            field_to_plot: tuple (data2d, dim1, dim2, field_name, plot_type, findex, map_params)
        """
        plot_type = field_to_plot[4]
        if plot_type == 'xy':
            _simple_xy_plot(config, field_to_plot)
        elif plot_type == 'yz':
            _simple_yz_plot(config, field_to_plot)
        elif plot_type == 'sc':
            _simple_sc_plot(config, field_to_plot)


@dataclass()
class SinglePlotter(Plotter):

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")

    def single_plots(self, config: Config, field_to_plot: tuple, level: int = None):
        self.plot(config, field_to_plot, level)

    @staticmethod
    def plot(config, field_to_plot, level):
        """ Create a single plot using specs data
        Parameters:
            config: Config
            field_to_plot: tuple (data2d, dim1, dim2, field_name, plot_type, findex, map_params)
            level: int (optional)
        """
        # data2d, dim1, dim2, field_name, plot_type, findex, map_params = field_to_plot
        plot_type = field_to_plot[4] + 'plot'

        if plot_type == constants.yzplot:
            _single_yz_plot(config, field_to_plot)
        if plot_type == constants.xtplot:
            _single_xt_plot(config, field_to_plot)
        if plot_type == constants.txplot:
            _single_tx_plot(config, field_to_plot)
        if plot_type == constants.xyplot:
            _single_xy_plot(config, field_to_plot, level)
        if plot_type == constants.polarplot:
            _single_polar_plot(config, field_to_plot)
        if plot_type == constants.scplot:
            _single_scat_plot(config, field_to_plot)
        # TODO: for user defined functions you need to do the following:
        # elif plot_type == constants.myplot:
        #     self._myplot_subplot(config, field_to_plot)


@dataclass()
class ComparisonPlotter:
    to_compare: list

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")

    def comparison_plots(self, config: Config, field_to_plot: tuple, level: int = None):
        self.plot(config, field_to_plot, level)

    @staticmethod
    def plot(config, field_to_plot, level):
        """ Create a single plot using specs data
        Parameters:
            config: Config
            field_to_plot: tuple (data2d, dim1, dim2, field_name, plot_type, findex, map_params)
            level: int (optional)
        """
        # data2d, dim1, dim2, field_name, plot_type, findex, map_params = field_to_plot
        plot_type = field_to_plot[4] + 'plot'
        if plot_type not in ['xyplot', 'yzplot', 'polarplot', 'scplot']:
            plot_type = field_to_plot[2]

        if plot_type == constants.yzplot:
            _single_yz_plot(config, field_to_plot)
        elif plot_type == constants.xtplot:
            _single_xt_plot(config, field_to_plot)
        elif plot_type == constants.txplot:
            _single_tx_plot(config, field_to_plot)
        elif plot_type == constants.xyplot:
            _single_xy_plot(config, field_to_plot, level)
        elif plot_type == constants.polarplot:
            _single_polar_plot(config, field_to_plot)
        elif plot_type == constants.scplot:
            _single_scat_plot(config, field_to_plot)
        else:
            logger.error(f'{plot_type} is not implemented')
        # TODO: for user defined functions you need to do the following:
        # elif plot_type == constants.myplot:
        #     self._myplot_subplot(config, field_to_plot)
