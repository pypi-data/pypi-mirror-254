import panel as pn
import holoviews as hv
import cartopy.crs as ccrs
import numpy as np
from eviz.lib.iviz import params_util


def frange(start, stop=None, step=None):
    """
    Produce a range given a start, and optionally a stop and step. 

    Parameters:
            start (int): number to start range;
            stop (int): number to stop range, optinal;
            step (int): increment between each number in range, optional;
    """
    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

def get_regridded_ds(d1_size, d1, d2_size, d2):
    """
    Compare sizes of dataset 1 and dataset 2 and regrid large dataset to 
    smaller dataset size. 

    Parameters:
            d1_size (tuple): tuple of dataset size
            d1 (xr.Dataset): Xarray dataset 1
            d2_size (tuple): tuple of dataset 2 size
            d2 (xr.Dataset): Xarray dataset 2

    Returns:
            new_arr (array): 2 dimensional array of regridded dataset.
            regridded_dataset_number (int): regridded ds #
    """
    if d1_size < d2_size:
        new_arr = params_util.regrid_xr(d2, d1, regrid_dims=(1, 0))
        new_arr = params_util.regrid_xr(new_arr, d1, regrid_dims=(0, 1))
        regridded_dataset_number = 2
    elif d1_size > d2_size:
        new_arr = params_util.regrid_xr(d1, d2, regrid_dims=(1, 0))
        new_arr = params_util.regrid_xr(new_arr, d2, regrid_dims=(0, 1))
        regridded_dataset_number = 1
    else:
        new_arr = d2
        regridded_dataset_number = 0
    return new_arr, regridded_dataset_number

def get_ylim(d1, d2):
    """
    Return the y min and max between two datasets.

    Parameters:
            d1: Xarray dataset
            d2: Xarray dataset
            ymin: parameter to set clim min
            ymax: parameter to set clim max

    Returns:
            clim_min (float): Value of colorbar minimum for cbar limit
            clim_max (float): Value of colorbar maximum for cbar limit
    """
    if d1.min() < d2.min():
        ymin = float(d1.min())
    else:
        ymin = float(d2.min())

    if d1.max() > d2.max():
        ymax = float(d1.max())
    else:
        ymax = float(d2.max())

    return ymin, ymax

def cache_projection(proj_str):
    """
    Add the current Cartopy CRS projection method to the Panel cache.

    Parameters:
            proj_str (str): input projection string.

    Cached:
            projection (method): Cartopy CRS projection method.
    """
    if ('projection',) in pn.state.cache:
        if proj_str in str(pn.state.cache[('projection',)]):
            pass
        else:
            proj_method = getattr(ccrs, proj_str)
            pn.state.cache.pop(('projection',))
            pn.state.as_cached('projection', proj_method)
    else:
        proj_method = getattr(ccrs, proj_str)
        pn.state.as_cached('projection', proj_method)


def cmap_examples(cms, provider, cols=4):
    """
    Returns a hv.Layout of hv.Images of colormaps. For each colormap available, create an image depicting color range
    available. Label each colormap above the image.

    Parameters:
            cms (list): list of strings of name of colormaps.
            provider (str): Colormap provider.
            cols (int): number of columns for Layout.

    Returns:
            hv.Layout (hv): Layout out of filtered colormap Images.
    """
    from math import ceil
    n = len(cms) * 1.0
    c = ceil(n / cols) if n > cols else cols
    opt_kwargs = dict(xaxis=None, yaxis=None, width=215, height=70,
                      margin=0, fontsize=6, toolbar=None)
    bars = [hv.Image(np.linspace(0, 1, 64)[np.newaxis],
                     ydensity=1) \
                .opts(cmap=hv.plotting.util.process_cmap(r, provider=provider), title=r,
                **opt_kwargs)
            for r in cms]
    return hv.Layout(bars).opts(width=500,toolbar=None).cols(c)


def set_clim(d1, d2):
    """
    Return the colorbar min and max between two datasets.

    Parameters:
            d1: Xarray dataset
            d2: Xarray dataset
            clim_min: parameter to set clim min
            clim_max: parameter to set clim max

    Returns:
            clim_min (float): Value of colorbar minimum for cbar limit
            clim_max (float): Value of colorbar maximum for cbar limit
    """
    if d1.min() < d2.min():
        clim_min = float(d1.min())
    else:
        clim_min = float(d2.min())

    if d1.max() > d2.max():
        clim_max = float(d1.max())
    else:
        clim_max = float(d2.max())

    return clim_min, clim_max

