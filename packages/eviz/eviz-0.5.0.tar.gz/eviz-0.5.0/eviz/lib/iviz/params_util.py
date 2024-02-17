import xarray as xr
import holoviews as hv
import panel as pn
import yaml

from scipy.interpolate import interp1d

import os 

pn.extension()
hv.extension('bokeh', logo=False)


def set_long_name_in_attrs(file,keys):
    """
    For all keys in xarray Dataset, set the 'long_name' attribute if not provided. 

    """
    for k in keys:
        if 'long_name' not in file[k].attrs:
            file[k].attrs['long_name'] = file[k].name
    return file

def set_units_in_attrs(file,keys):
    """
    For all keys in xarray Dataset, set the 'units' attribute if not provided. 

    """
    for k in keys:
        if 'units' not in file[k].attrs:
            file[k].attrs['units'] = ''
    return file

def get_ndims(file, field=None):
    """
    Get number of dimensions of input file, if provided a field, get dimensions
    of that fields array. 

    Parameters:
            file (xr): data
            field (str): variable, optional;

    Returns:
            ndims (int): number of dimensions found
    """
    if field is None:
        ndims = len(list(file.dims))
    else:
        ndims = len(list(file[field].dims))
    return ndims


def get_coords(file):
    """
    Get coordinates of input file. 

    Parameters:
            file (xr): data;

    Returns:
            list : list of coords found
    """
    return list(file.coords)


def get_dims(file):
    """
    Get coordinates of input file. 

    Parameters:
            file (xr): data;

    Returns:
            list : list of coords found
    """
    return list(file.dims)


def get_keys(file):
    """
    Get coordinates of input file.

    Parameters:
            file (xr): data;

    Returns:
            list : list of coords found
    """
    return list(file.keys())


def load_model_coords():
    """
    Load the coordinates of all known models types using the config/meta_coordinates.yaml
    file. 

    Returns:
            meta_coordinates (dict): coordinates of all known models;
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    meta_coords = '../../../config/meta_coordinates.yaml'
    meta_coord_path = os.path.join(root_path, meta_coords)
    with open(meta_coord_path) as f:
        meta_coordinates = yaml.load(f, Loader=yaml.FullLoader)
    return meta_coordinates 


def get_model_type(coords):
    """
    Match the provided coordinates with the coordinates of known models 
    in case model type is not provided by user. If coordinates match a known 
    model type, return the model. If not, return None. 

    Parameters:
            coords (list): all data coordinates;

    Returns:
            model (str): model type if known
    """
    model = None
    meta_coords = load_model_coords()
    cf = [meta_coords['xc']['cf'], meta_coords['yc']['cf'], meta_coords['tc']['cf'], meta_coords['zc']['cf']]
    ccm = [meta_coords['xc']['ccm'], meta_coords['yc']['ccm'], meta_coords['tc']['ccm'], meta_coords['zc']['ccm']]
    gmi = [meta_coords['xc']['gmi'], meta_coords['yc']['gmi'], meta_coords['tc']['gmi'], meta_coords['zc']['gmi']]
    wrf = [meta_coords['xc']['wrf']['coords'][0], meta_coords['yc']['wrf']['coords'][0], meta_coords['tc']['wrf']['coords'], 
                meta_coords['zc']['wrf']['coords']]
    lis = [meta_coords['xc']['lis']['dim'], meta_coords['yc']['lis']['dim'], meta_coords['tc']['lis']['dim']]
    base = ['lon', 'lat', 'time']

    dic = {
        'cf': cf,
        'ccm': ccm,
        'gmi': gmi,
        'lis': lis,
        'wrf': wrf,
        'base': base,
    }

    for key, value in dic.items():
        coords.sort()
        dic[key].sort()
        if coords == dic[key]:
            model = key

    return model


# Interpolation (AKA regrid) methods
def _interp(y_src, x_src, x_dest, **kwargs):
    """
    Return the scipy interpolate single dimension funcition with args. 

    """
    return interp1d(x_src, y_src, **kwargs)(x_dest)


def regrid_xr(ref_arr, in_arr, regrid_dims=(0,0)):
    """
    Regrids input 2D array with respect to the reference ref_arr using scipy 
    interp1d function.

    Parameters:
            ref_arr (array): 2d array to map to;
            in_arr (array): 2d array to regrid;
            regrid_dims (tuple): dimension of array being regridded;

    Returns:
            new_array (array) : Regridded 2d array
    """
    new_arr = ref_arr
    if regrid_dims[0]:
        new_arr = xr.apply_ufunc(_interp, new_arr,
                                 input_core_dims=[['lat']],
                                 output_core_dims=[['lat']],
                                 exclude_dims={'lat'},
                                 kwargs={'x_src': new_arr['lat'], 'x_dest': in_arr.coords['lat'].values, 
                                 'fill_value': "extrapolate"}, 
                                #  'fill_value': 1.0}, 
                                 )
        new_arr.coords['lat'] = in_arr.coords['lat']
    elif regrid_dims[1]:
        new_arr = xr.apply_ufunc(_interp, new_arr,
                                 input_core_dims=[['lon']],
                                 output_core_dims=[['lon']],
                                 exclude_dims={'lon'},
                                 kwargs={'x_src': new_arr['lon'], 'x_dest': in_arr.coords['lon'].values, 
                                 'fill_value': "extrapolate"}, 
                                #  'fill_value': 1.0}, 
                                 )
        new_arr.coords['lon'] = in_arr.coords['lon']
    else:
        return new_arr
    return new_arr


def regrid_xr_yz(ref_arr, in_arr, regrid_dims=(0, 0)):
    """
    Regrids input 2D array with respect to the reference ref_arr using scipy 
    interp1d function for the yz data. c

    Parameters:
            ref_arr (array): 2d array to map to;
            in_arr (array): 2d array to regrid;
            regrid_dims (tuple): dimension of array being regridded;

    Returns:
            new_array (array) : Regridded 2d array
    """
    new_arr = ref_arr
    if regrid_dims[0]:
        new_arr = xr.apply_ufunc(_interp, new_arr,
                                 input_core_dims=[['lev']],
                                 output_core_dims=[['lev']],
                                 exclude_dims={'lev'},
                                 kwargs={'x_src': new_arr['lev'], 'x_dest': in_arr.coords['lev'].values})
        new_arr.coords['lev'] = in_arr.coords['lev']
    elif regrid_dims[1]:
        new_arr = xr.apply_ufunc(_interp, new_arr,
                                 input_core_dims=[['lat']],
                                 output_core_dims=[['lat']],
                                 exclude_dims={'lat'},
                                 kwargs={'x_src': new_arr['lat'], 'x_dest': in_arr.coords['lat'].values})
        new_arr.coords['lat'] = in_arr.coords['lat']
    else:
        return new_arr
    return new_arr


def coastlines360(resolution='110m',lon_360=False):
    """
    Using cartopy natural earth features, return a Holoviews overlay of 0-360 latitude
    coastlines. 
    """
    try:
        import cartopy.io.shapereader as shapereader
        from cartopy.io.shapereader import natural_earth
        import shapefile
        filename = natural_earth(resolution=resolution,category='physical',name='coastline')

        sf = shapefile.Reader(filename)
        fields = [x[0] for x in sf.fields][1:]
        records = sf.records()
        shps = [s.points for s in sf.shapes()]
        pls=[]
        for shp in shps:
            lons=[lo+180.0 for lo,_ in shp]
            lats=[la for _,la in shp]
            if lon_360:
                lats_patch1=[lat for lon,lat in zip(lons,lats) if lon<0]
                lons_patch1=[lon+360.0 for lon in lons if lon<0]
                if any(lons_patch1):
                    pls.append(hv.Path((lons_patch1,lats_patch1)).opts(color='black'))
                lats_patch2=[lat if lon>=0 else None for lon,lat in zip(lons,lats)]
                lons_patch2=[lon if lon>=0 else None for lon in lons]
                if any(lons_patch2):
                    pls.append(hv.Path((lons_patch2,lats_patch2)).opts(color='black'))
            else:
                pls.append(hv.Path((lons,lats)).opts(color='black'))
        return hv.Overlay(pls)
    except Exception as err:
        print('Overlaying Coastlines not available from holoviews because: {0}'.format(err))
