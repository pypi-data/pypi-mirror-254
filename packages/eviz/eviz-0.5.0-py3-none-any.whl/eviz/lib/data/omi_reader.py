"""
Contributed by Deon Kouatchou-Ngongang

"""
import numpy as np
import xarray as xr
from .base_reader import BaseReader
from .netcdf_reader import NetcdfReader
import h5py
import sys


class OMIHdfReader(BaseReader):
    """ Handles reading OMI data from HDF5 files.

    Note: OMI Level 1B data files are written in HE4 format while Level 2
    and Level 3 product are in HE5 format
    """

    xc = 'lon'
    yc = 'lat'
    zc = None
    tc = 'time'

    # # I. Constructor
    def __init__(self, filename, model):
        """
            Note: this data source is a sub level of data product for omi so that it can extract with
            the correct coordinate labels, and then rename all of them to lat/lon/time
            so it'll happen for both if you start with an omi source and if you are doing a comparison and you
            select the comparison source using the drop down menu
        """
        super().__init__(filename, model)
        self.model = 'base'
        self.model = model

        # if isinstance(self.var, type(None)):
        self.fn = filename
        self.get_level()
        self.ftype = self.get_ftype()
        self.data = self.read_file()

    def __repr__(self):
        return f'Reader object: {self.ftype}; {type(self.data)} \n{self.fn}'

    # II. Accessor & Helper Functions
    def get_level(self):
        """ Check that the file is Level 3 OMI product.
        """
        if 'L3' not in self.fn:
            print('OMI MLS data must be of Level 3 data product.')
            sys.exit()

    def get_fid(self):
        """ Access the file reader object for a given HDF5 file

        Returns:
            an h5py file reader object
        """
        fid = h5py.File(self.fn, 'r')
        return fid

    def get_data_group(self, fid):
        """
        Finds and returns the contents of the file data field subgroup in dictionary format

        Parameters:
            fid: a file identifier object
        Returns:
             a Python dictionary of dataset name String keys and dataset object values
        """
        parent_contents = dict(fid['HDFEOS']['GRIDS'])  # contents of our parent group
        sub = list(parent_contents.values())[0]  # our sub-parent group object
        sub_contents = dict(sub)  # contents of our sub-parent group
        data_group = list(sub_contents.values())[0]  # our data group object

        return dict(data_group)

    # - - - - - A. Attributes
    def convert_dict_dtype(self, sample_dict):
        """
        Converts a dictionary of attributes from NumPy data types to general Python data types

        Parameters:
            sample_dict: a Python dictionary of attributes
        Returns:
             a Python dictionary of attributes
        """
        for key, item in sample_dict.items():
            if isinstance(item, np.ndarray):  # Converts np arrays to a list to, if applicable, an int or float
                item = list(item)

                if len(item) == 1:
                    item = item[0]
            elif isinstance(item, np.bytes_):  # Converts np bytes to np string to a Python string
                item = str(item.astype('str'))

                if item[0] == '(' or item[0] == '{':  # Converts to tuple or dict if applicable
                    item = eval(item)
                # **eval() reliability??**

            sample_dict[key] = item  # Updates any changes to the key value

        return sample_dict

    def get_fid_attrs(self, fid):
        """
        Returns the file-level attributes (in Python data types)

        Parameters:
            fid: a file reader object
        Returns:
            a Python dictionary of attributes
        """
        fid_attrs = dict(fid['HDFEOS']['ADDITIONAL']['FILE_ATTRIBUTES'].attrs)
        fid_attrs = self.convert_dict_dtype(fid_attrs)

        fid_attrs.update(self.get_plot_attrs(fid))

        return fid_attrs

    def get_plot_attrs(self, fid):
        """
        Returns the file plotting attributes (in Python data types)

        Parameters:
            fid: a file reader object
        Returns:
            a Python dictionary of attributes
        """
        parent_contents = dict(fid['HDFEOS']['GRIDS'])
        subgroup = list(parent_contents.values())[0]

        plot_attrs = dict(subgroup.attrs)
        plot_attrs = self.convert_dict_dtype(plot_attrs)

        return plot_attrs

    def get_ds_attrs(self, ds):
        """
        Returns the attributes of an HDF5 dataset

        Parameters:
            ds: an HDF5 dataset object
        Returns:
            a Python dictionary of attributes
        """
        ds_attrs = dict(ds.attrs)
        ds_attrs = self.convert_dict_dtype(ds_attrs)

        return ds_attrs

    # - - - - - B. Data Restoration
    def get_fill(self, ds_attrs):
        """
        Returns the fill value of a dataset

        Parameters:
            ds_attrs: a Python dictionary of dataset attributes
        Returns:
            an integer, float, or 'None'
        """
        for key, value in ds_attrs.items():
            if key == '_FillValue':
                return value
        return None

    def get_scale(self, ds_attrs):
        """
        Returns the scale factor of a dataset

        Parameters:
            ds_attrs: a Python dictionary of dataset attributes
        Returns:
            an integer, float, or 'None'
        """
        for key, value in ds_attrs.items():
            if key == 'ScaleFactor':
                return value
        return 1

    def get_offset(self, ds_attrs):
        """
        Returns the offset value of a dataset

        Parameters:
            ds_attrs: a Python dictionary of dataset attributes
        Returns:
            an integer, float, or &/or 0
        """
        for key, value in ds_attrs.items():
            if key == 'Offset':
                return value
        return 0

    def restore_data(self, ds):
        """
        Restores the data of a given dataset object

        Parameters:
            ds: an HDF5 dataset object
        Returns:
            a NumPy array
        """
        ds_attrs = self.get_ds_attrs(ds)

        fill = self.get_fill(ds_attrs)
        scale = self.get_scale(ds_attrs)
        offset = self.get_offset(ds_attrs)

        data = ds[()]  # .astype('float')

        data = np.where(data != fill, data, np.nan)
        data *= scale
        data += offset

        data = np.expand_dims(data, axis = 0)

        return data

    # - - - - - C. Coordinates & Dimensions
    def get_time(self, fid):
        """
        Returns the time at which the data was measured/acquired

        Parameters:
            fid: a file reader object
        Returns:
             a list of a DateTime object
        """
        fid_attrs = self.get_fid_attrs(fid)

        year = month = day = None
        for key, value in fid_attrs.items():
            if 'year' in key.lower():
                year = str(value)
            elif 'month' in key.lower():
                month = str(value)
                if len(month) == 1:
                    month = '0'+month
            elif 'day' in key.lower():
                day = str(value)
                if len(day) == 1:
                    day = '0'+day

        time = year + '-' + month + '-' + day
        times = [time]
        # times = [datetime.strptime(time, '%Y %b %d')]

        return times

    def get_coords(self, fid):
        """
        Returns the coordinates of a file

        Parameters:
            fid: a file reader object
        Returns:
             a Python dictionary of String keys and NumPy array values
        """
        plot_attrs = self.get_plot_attrs(fid)

        lonW = plot_attrs['GridSpan'][0]
        lonE = plot_attrs['GridSpan'][1]
        latS = plot_attrs['GridSpan'][2]
        latN = plot_attrs['GridSpan'][3]

        lon_size = plot_attrs['NumberOfLongitudesInGrid']
        lat_size = plot_attrs['NumberOfLatitudesInGrid']

        lons = np.linspace(lonW, lonE, lon_size)
        lats = np.linspace(latS, latN, lat_size)
        times = self.get_time(fid)

        return {'times': times, 'lons': lons, 'lats': lats}

    def get_ds_dims(self, ds, coords):
        """
        Returns the dimension names of a dataset

        Parameters:
            ds: a dataset object
            coords: a Python dictionary of file coordinates (NumPy arrays)
        Returns:
            a Python dictionary of dimension name String keys and dimension size integer values
        """
        dims = ds.dims
        ds_dims = {'time': 1}

        for i in range(len(dims)):
            if dims[i].label == '':
                if ds.shape[i] == coords['lons'].size:
                    ds_dims['lon'] = ds.shape[i]
                elif ds.shape[i] == coords['lats'].size:
                    ds_dims['lat'] = ds.shape[i]
            else:
                if 'time' in dims[i].label.lower():
                    ds_dims['time'] = ds.shape[i]
                else:
                    ds_dims[dims[i].label] = ds.shape[i]

        return ds_dims

    def check_coords(self, dims, coords):
        """
        Rearranges order of the coordinates list to match the dimension shapes

        Parameters:
            dims: a Python dictionary of dimension name String keys and dimension size integer values
            coords: a Python dictionary of file coordinates (NumPy arrays)
        Returns:
            a Python dictionary of rearranged file coordinates (NumPy arrays)
        """
        if list(dims.values())[1] != list(coords.values())[1].size:
            temp = coords
            coords = {list(coords.keys())[0]: list(coords.values())[0],
                      list(coords.keys())[2]: list(coords.values())[2],
                      list(coords.keys())[1]: list(coords.values())[1]}
        return coords

    # III. Top-Level Functions
    def get_array(self, data_group, fid_coords):
        """
        Returns an XArray DataArray of an HDF5 dataset given the data field subgroup contents and
        file-level coordinates.

        Parameters:
            data_group: a Python dictionary of String keys and HDF5 dataset object values
            fid_coords: a Python dictionary of file coordinates (NumPy arrays)
        Returns:
            an XArray DataArray
        """
        try:
            hdf_ds = data_group[self.var]
        except KeyError:   # If variable doesn't exist
            xr_arr = None
        else:
            data = self.restore_data(hdf_ds)
            ds_attrs = self.get_ds_attrs(hdf_ds)

            ds_dims = self.get_ds_dims(hdf_ds, fid_coords)
            ds_coords = self.check_coords(ds_dims, fid_coords)

            xr_arr = xr.DataArray(data, dims=list(ds_dims.keys()), coords=list(ds_coords.values()))
            xr_arr.attrs = ds_attrs

        return xr_arr

    def read_set(self):
        """
        Reads the OMI HDF5 File Reader object and eturns the dataset(s) as an XArray DataArray/Dataset

        Returns:
            an XArray DataArray or Dataset
        """
        fid = self.get_fid()

        data_group = self.get_data_group(fid)
        fid_coords = self.get_coords(fid)

        if isinstance(self.var_input, str):
            xr_arr = self.get_array(data_group, fid_coords)

            fid.close()
            return xr_arr
        elif isinstance(self.var_input, tuple) or isinstance(self.var_input, list):
            if len(self.var_input) == 1:
                self.var = self.var_input[0]
                xr_arr = self.get_array(data_group, fid_coords)

                fid.close()
                return xr_arr
            else:
                xr_ds = xr.Dataset()

                fid_attrs = self.get_fid_attrs(fid)

                for var in self.var_input:
                    if var in data_group.keys():
                        self.var = var
                        xr_ds[var] = self.get_array(data_group, fid_coords)

                xr_ds.attrs = fid_attrs

                fid.close()

                if '*empty*' in repr(xr_ds.data_vars):  # If the dataset is empty
                    return None
                else:
                    return xr_ds
        else:
            return None

    def read_file(self):
        """
        Reads an OMI HDF5 filename and returns its data as an XArray Dataset

        Returns:
            an XArray Dataset
        """
        xr_ds = xr.Dataset()

        fid = self.get_fid()

        data_group = self.get_data_group(fid)
        fid_attrs = self.get_fid_attrs(fid)
        fid_coords = self.get_coords(fid)

        for var in data_group.keys():
            self.var = var
            xr_ds[var] = self.get_array(data_group, fid_coords)

        xr_ds.attrs = fid_attrs

        fid.close()

        if '*empty*' in repr(xr_ds.data_vars):   # If the dataset is empty
            return None
        else:
            return xr_ds

    # IV. Future OOP Things
    def get_ftype(self):
        """
        Determines and returns the file type of the OMI Reader object

        Returns:
            String of file type or 'None'
        """
        if self.fn.endswith('.he5'):
            return 'HDF5'
        elif self.fn.endswith('.he4'):
            return 'HDF4'
        else:
            return None

class OMINetcdfReader(NetcdfReader):

    xc = 'longitude'
    yc = 'latitude'
    zc = None
    tc = 'time'
    # # I. Constructor
    def __init__(self, filename, model, is_url=None): #dsource is a sub level of data product for omi so that it can extract with
        # the correct coordinate labels, and then rename all of them to lat/lon/time
        # so it'll happen for both if you start with an omi source and if you are doing a comparison and you select the comparison
        # source using the drop down menu
        super().__init__(filename, model, is_url)
        tropo = self.get_omi_product()
        if tropo == True:
            self.data = self.get_tropo_time()
        else:
            self.data = self.get_time()

    def get_omi_product(self):
        tropo = False

        omi_tropo_sources = ['MODIS_AOT',
        'MOP_toco',
        'OMI_toch2o',
        'OMI_toso2',
        'OMI_trno2',
        'OMIMLS_tro3']

        for source in omi_tropo_sources:
            if source in self.fn:
                tropo = True
        return tropo

        # if dsource is None:
            # print("OMI data product not recognized.")
            # sys.exit()

    def get_time(self):
        year = self.fn.split('_')[-2].split('m')[0]
        mo = self.fn.split('_')[-2].split('m')[-1][0:2]
        day = self.fn.split('_')[-2].split('m')[-1][2:4]
        yearmoday = year + '-' + mo + '-' + day
        newtime = np.datetime64(yearmoday, 'D')
        return self.data.expand_dims({'time': [newtime]}) 

    def get_tropo_time(self):
        yearmo = self.fn.split('_')[-1].split('.')[0]
        yearmo = yearmo[0:4] + '-' + yearmo[4:6]
        newtime = np.datetime64(yearmo, 'M')
        return self.data.expand_dims({'time': [newtime]}) 
