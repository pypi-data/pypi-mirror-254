""" Contributed by Deon Kouatchou-Ngongang """
import numpy as np
import xarray as xr
import pyhdf.error
from pyhdf.SD import SD, SDC
from .base_reader import BaseReader


class LandsatReader(BaseReader):
    """ Handles reading Landsat data from HDF4 files """
    def __init__(self, filename, model):
        super().__init__(filename, model)
        self.fn = filename
        self.ftype = self.get_ftype()
        self.data = self.read_file()

    def __repr__(self):
        return f'Reader object: {self.ftype}; {type(self.data)} \n{self.fn}'

    # II. Accessor & Helper Methods
    def get_fid(self):
        """ Accesses the file reader object for a file

        Returns:
            a file reader (SD) object
        """
        fid = SD(self.fn, SDC.READ)
        return fid

    # - - - - - A. Data Restoration
    def get_fill(self, ds):
        """ Returns the fill value of a given dataset (SDS) object

        Parameters:
            ds: an SDS object
        Returns:
            float, int, or 'None'
        """
        for key, value in ds.attributes().items():
            if key == '_FillValue':
                return value
        return None

    def get_scale(self, ds):
        """ Returns the scale factor of a given dataset (SDS) object

        Parameters:
            ds: an SDS object
        Returns:
            float, int, or 'None'
        """
        for key, value in ds.attributes().items():
            if key == 'scale_factor':
                return value
        return 1

    def get_offset(self, ds):
        """ Returns the offset value of a given dataset (SDS) object

        Parameters:
            ds: an SDS object
        Returns:
            float, int, or 'None'
        """
        for key, value in ds.attributes().items():
            if key == 'add_offset':
                return value
        return 0

    def restore_data(self, ds):
        """ Restores the data o a given dataset (SDS) object

        Parameters:
            ds: an SDS object
        Returns:
             a NumPy array
        """
        fill = self.get_fill(ds)
        scale = self.get_scale(ds)
        offset = self.get_offset(ds)

        data = ds.get()  # .astype('float')

        data = np.where(data != fill, data, np.nan)  # fill
        data *= scale  # scale
        data += offset  # offset

        data = np.expand_dims(data, axis = 0)

        return data

    # - - - - - B. Dimensions
    def get_dims(self, ds):
        """ Returns the dimension (SDim) objects of a given dataset (SDS) object

        Parameters:
            ds: an SDim object
        Returns:
            a Python list of SDim objects
        """
        dims = []  # Will actually hold dimension objects

        for i in range(len(ds.dimensions())):
            dims.append(ds.dim(i))

        return dims

    def get_dim_attrs(self, dim):
        """ Returns the attributes of a given dimension (SDim) object

        Parameters:
            dim: an SDim object
        Returns:
            a Python dictionary (String keys and values)
        """
        attrs = {'Name': dim.info()[0], 'dtype': dim.info()[2]}  # Will hold dim attrs

        attrs.update(dim.attributes())  # Adds other unknown attributes

        return attrs

    def get_dims_attrs(self, ds):
        """ Returns the dimension attributes for a given dataset (SDS) object

        Parameters:
            ds: an SDS object
        Returns:
            a Python dictionary of String keys and dictionary values
        """
        dims_attrs = {}
        dims = self.get_dims(ds)

        for dim in dims:
            if dim.info()[0] == 'YDim':
                dims_attrs['lat'] = self.get_dim_attrs(dim)
            elif dim.info()[0] == 'XDim':
                dims_attrs['lon'] = self.get_dim_attrs(dim)

        return dims_attrs

    # - - - - - C. Coordinates
    def check_fid_coords(self, fid):
        """ Checks if there are any file-level coordinates

        Parameters:
            fid: a file reader (SD) object
        Returns:
             bool: False if there are no file-level coordinates, True if there are any
        """
        coord_sets = []  # will hold datasets suspected to be coordinates

        for i in range(len(fid.datasets())):
            ds = fid.select(i)
            if bool(ds.iscoordvar()):
                coord_sets.append(ds)

        if len(coord_sets) > 0:
            return True
        else:
            return False

    def get_coord_bounds(self, fid):
        """ Returns the coordinate boundaries for constructing coordinates at the dataset level

        Parameters:
            fid: a file reader (SD) object
        Returns:
            a Python dictionary of String keys and numeric values
        """
        coord_attrs = {}
        # Gets our coordinate-related attributes
        for key, value in fid.attributes().items():
            if 'coordinate' in key.lower():
                coord_attrs[key] = value

        coord_bounds = {}
        # Gets our coordinate bounds
        for key in coord_attrs.keys():
            if 'north' in key.lower():
                coord_bounds['latN'] = coord_attrs[key]
            if 'south' in key.lower():
                coord_bounds['latS'] = coord_attrs[key]
            if 'east' in key.lower():
                coord_bounds['lonE'] = coord_attrs[key]
            if 'west' in key.lower():
                coord_bounds['lonW'] = coord_attrs[key]

        return coord_bounds

    def get_ds_coords(self, fid, ds):
        """ Returns constructed coordinates given the file reader (SD) and a dataset (SDS) object

        Parameters:
            fid: an SD object
            ds: an SDS object
        Returns:
            a Python dictionary of String keys and NumPy array values
        """
        bounds = self.get_coord_bounds(fid)

        latN = bounds['latN']
        latS = bounds['latS']
        lonE = bounds['lonE']
        lonW = bounds['lonW']

        lat_shape = ds.dimensions()['YDim']
        lon_shape = ds.dimensions()['XDim']

        if isinstance(bounds, dict):  # Have to configure dataset coords
            lat_space = (latN - latS) / lat_shape
            lon_space = (lonE - lonW) / lon_shape

            lats = np.linspace(latS, latN + lat_space, lat_shape)
            lons = np.linspace(lonW, lonE + lon_space, lon_shape)
            times = [self.get_time(fid)]

            coords = {'times': times, 'lats': lats, 'lons': lons}
            return coords

        # else:   # Coords already set at file level
        # return sample_bounds

    def get_time(self, fid):
        """ Returns the time(s) at which the data was measured/acquired

        Parameters:
            fid: an SD object
        Returns:
            a DateTime object
        """
        time = fid.attributes()['AcquisitionDate']
        return time

    # III. Top-Level Methods

    def get_array(self, fid):
        """ Returns an XArray DataArray of an HDF4 dataset given the file and Landsat reader objects

        Parameters:
            fid: an SD object
        Returns:
            an XArray DataArray
        """
        try:
            ds = fid.select(self.var)
        except pyhdf.error.HDF4Error:
            xr_arr = None
        else:
            coords_dict = self.get_ds_coords(fid, ds)
            lats = coords_dict['lats']
            lons = coords_dict['lons']
            times = coords_dict['times']

            xr_arr = xr.DataArray(self.restore_data(ds), coords=[times, lats, lons], dims=['time', 'lat', 'lon'])

            xr_arr.attrs = ds.attributes()

            dims_attrs = self.get_dims_attrs(ds)
            xr_arr.lat.attrs = dims_attrs['lat']
            xr_arr.lon.attrs = dims_attrs['lon']

        return xr_arr

    def read_set(self):
        """ Reads a LANDSAT HDF4 Reader object and returns the dataset(s) as an XArray DataArray/Dataset

        Returns:
            an XArray DataArray or Dataset
        """
        fid = self.get_fid()

        if self.check_fid_coords(fid):  # File-level coords exist
            pass
        else:
            fid_coords = False  # File-level coords do not exist

        if isinstance(self.var_input, str):
            xr_arr = self.get_array(fid)

            fid.end()
            return xr_arr
        elif isinstance(self.var_input, tuple) or isinstance(self.var_input, list):
            if len(self.var_input) == 1:
                self.var = self.var_input[0]
                xr_arr = self.get_array(fid)

                fid.end()
                return xr_arr
            else:
                xr_ds = xr.Dataset()

                for var in self.var_input:
                    if var in fid.datasets().keys():
                        self.var = var
                        xr_ds[var] = self.get_array(fid)

                xr_ds.attrs = fid.attributes()

                fid.end()

                if '*empty*' in repr(xr_ds.data_vars):  # If the dataset is empty
                    return None
                else:
                    return xr_ds
        else:
            return None

    def read_file(self):
        """ Reads a LANDSAT HDF4 Reader object and returns its data as an XArray Dataset

        Returns:
            an XArray Dataset
        """
        fid = self.get_fid()

        if self.check_fid_coords(fid):  # File-level coords exist
            pass
        else:
            fid_coords = False  # File-level coords do not exist

        xr_ds = xr.Dataset()

        for var in fid.datasets().keys():
            self.var = var
            xr_ds[var] = self.get_array(fid)

        xr_ds.attrs = fid.attributes()

        fid.end()

        if '*empty*' in repr(xr_ds.data_vars):  # If the dataset is empty
            return None
        else:
            return xr_ds

    # IV. Future OOP Things
    def get_ftype(self):
        """ Determines and returns the file type of the Landsat Reader object

        Returns:
            String of file type or 'None'
        """
        if self.fn.endswith('hdf'):
            return 'HDF4'
        else:
            return None


if __name__ == "__main__":
    f_loc = '/Users/deonkouatchou/eviz/eviz_datasource_dev/Samples/Landsat/'
    f1 = f_loc + 'LT50830152011198GLC00.hdf'
    f2 = f_loc + 'LT50830152011214GLC00.hdf'

    obj1 = LandsatReader(f1)
    print(obj1, '\n')

    obj2 = LandsatReader(f2, 'cfmask')
    print(obj2, '\n')

    obj3 = LandsatReader(f1, ['toa_band6'])
    print(obj3, '\n')
    print(obj3.data)

    obj4 = LandsatReader(f2, ('toa_band6_qa', 'sr_band1', 'sr_band4'))
    print(obj4, '\n')

    obj5 = LandsatReader(f1, '?')
    print(obj5, '\n')

    obj6 = LandsatReader(f1, ['!', '?'])
    print(obj6, '\n')
