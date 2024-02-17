import xarray as xr
import param
import sys
from getpass import getpass
from pydap.cas.urs import setup_session
from pydap.client import open_url
from eviz.lib.iviz import params_util

from .base_reader import BaseReader


class NetcdfReader(BaseReader):

    def __init__(self, filename, model, is_url):
        super().__init__(filename, model)
        self.fn = filename
        self.stype = model
        self.model = model
        self.is_url = is_url

        if self.is_url:
            pydap_client = self.get_pydap_client(filename)
            # self.fn = self.open_file()
            self.fn = pydap_client

        # self.data = self.open_file()
        self.data = self.read_file()

        if model is None:
            self.model = self.get_model()
        else:
            self.model = model

    def get_pydap_client(self, filename):
        username = input(" Opendap Username Required: ")
        password = getpass(" Opendap Password Required: ")
        session = setup_session(username, password, check_url=self.fn)
        dataset = open_url(self.fn, session=session)
        store = xr.backends.PydapDataStore.open(self.fn, session=session)
        return store

    def get_model(self):
        """
        If provided a file or a directory as input, determine what model type
        the data is using the coordinates of the data.

                Returns:
                        model (str): determined model type
        """
        self.coords = params_util.get_coords(self.data)
        self.dims = params_util.get_dims(self.data)
        self.meta_coords = params_util.load_model_coords()
        model = params_util.get_model_type(self.coords)
        if model is None:
            model = 'netcdf'
        return model

    def open_file(self):
        """
        Open the current file after determining input to tool.

                Sets:
                        self.file : an Xarray dataset
        """
        try:
            data = xr.open_dataset(self.fn if type(self.fn) != param.Selector else
                                   self.files)
            # else input is a link to an opendap dataset or path to .nc4 file
        except ValueError:
            try:
                data = xr.open_dataset(self.fn if type(self.fn) != param.Selector else
                                       self.files, decode_times=False)
            except Exception as e:
                print(e)
                print(' Unrecognized input ')
                sys.exit(1)
        return data

    def get_fields(self, data):
        keys = list(data.keys())
        fields = []
        for k in keys:
            if (k not in list(data.coords)) and \
                    (k not in list(data.dims)):
                # k != 'Times':
                fields.append(k)
        return fields

    def read_file(self):
        """
        Reads an OMI HDF5 filename and returns its data as an XArray Dataset

        Returns:
            an XArray Dataset
        """
        xr_ds = xr.Dataset()

        dataset = self.open_file()

        ds_attrs = dataset.attrs

        for var in self.get_fields(dataset):
            self.var = var
            xr_ds[var] = self.get_array(dataset)

        xr_ds.attrs = ds_attrs
        return xr_ds

    def get_renamed_coords(self, data_array, squeeze=False):
        renamed_coords = {}
        if self.xc in list(data_array.coords):
            renamed_coords[self.xc] = 'lon'
        if self.yc in list(data_array.coords):
            renamed_coords[self.yc] = 'lat'
        if self.zc in list(data_array.coords):
            renamed_coords[self.zc] = 'lev'
        if self.tc in list(data_array.coords):
            renamed_coords[self.tc] = 'time'

        if squeeze:
            data_array = data_array.squeeze()

        return renamed_coords

    def get_array(self, ds):
        try:
            da = ds[self.var]
            renamed_coords = self.get_renamed_coords(da)

            newda = da.rename(renamed_coords)
            return newda
        except KeyError:
            sys.exit('Variable not found in dataset')

    def get_coords(self, fid):
        """
        Returns the coordinates of a file

        Parameters:
            fid: a file reader object
        Returns:
             a Python dictionary of String keys and NumPy array values
        """
        return fid.coords
