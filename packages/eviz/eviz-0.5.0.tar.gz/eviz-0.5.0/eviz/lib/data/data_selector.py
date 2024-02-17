"""
Contributions from Deon Kouatchou-Ngongang
"""
from eviz.lib.data.landsat_reader import LandsatReader
from eviz.lib.data.omi_reader import OMIHdfReader
from eviz.lib.data.omi_reader import OMINetcdfReader
from .netcdf_reader import NetcdfReader
from .csv_reader import CsvReader
from eviz.lib.data.airnow_reader import AirNowReader
from .lis_reader import LisReader
from .wrf_reader import WrfReader
import sys
from . import data_utils as du


class DataSelector:
    """
    Purposes:
        - Determine the source and file type of file by reading its filename
        - Construct an XArray data structure of file data by reading its filename

    """

    def __init__(self, filename, model, is_url=False, dtype=None, var=None, stype=None):
        """ Creates a Datasource object which manages file reading

        Parameters:
           filename: a filename String
           var: a data variable String or 'None'
        """
        self.fn = filename
        self.var = var
        self.model = model
        self.is_url = is_url

        if dtype is None:
            self.dtype = self.get_dtype(self.fn)
        else:
            self.dtype = dtype
        self.stype = self.get_stype()
        self.data_reader = self.get_data_reader()

        self.data = self.data_reader.data
        self.model = self.data_reader.model

        # if self.model == 'airnow':
            # self.dataframe = self.data_reader.dataframe

    def __repr__(self):
        """ Returns object data """
        return f'Datasource object: {self.stype} Reader \n{repr(self.stype)}'

    def __str__(self):
        """

        :return:
        """
        return repr(self)

    @staticmethod
    def get_dtype(filename):  # could take in model here as well to determine dtype for wrf, directories
        dtype = None
        if filename.endswith('.he5') or filename.endswith('.hdf'):
            dtype = 'hdf'
        elif filename.endswith('.nc4') or filename.endswith('.nc'):
            dtype = 'netcdf'
        elif filename.endswith('.dat'):
            dtype = 'tabular'
        elif filename.endswith('.csv'):
            dtype = 'tabular'
        return dtype

    def get_data_reader(self):
        """ Creates and returns the data reader object given the source type

        Returns:
             cls data reader
        """
        if (self.stype == 'omi') and (self.dtype == 'hdf'):
            return OMIHdfReader(self.fn, self.model)
        elif self.stype == 'omi':
            return OMINetcdfReader(self.fn, self.model, #self.stype,
                                is_url=self.is_url)
        elif self.stype == 'mopitt':
            return OMINetcdfReader(self.fn, self.model, #self.stype,
                                is_url=self.is_url)
        elif self.stype == 'landsat':
            return LandsatReader(self.fn, self.model)
        elif self.stype == 'netcdf':
            return NetcdfReader(self.fn, self.model, is_url=self.is_url)
        elif self.stype == 'lis':
            return LisReader(self.fn, self.model, self.is_url)
        elif self.stype == 'wrf':
            return WrfReader(self.fn, self.model, self.is_url)
        elif self.stype == 'tabular':
            return CsvReader(self.fn, self.model)
        elif self.stype == 'airnow':
            return AirNowReader(self.fn, self.model)
        else:
            print('Data type and/or source not yet supported')
            sys.exit()

    @staticmethod
    def get_hdf_stype(model,fn):
        if model == 'omi':
            return 'omi'
        elif model == 'landsat': 
            return 'landsat'
        else:
            if du.is_omi(fn) != du.is_landsat(fn):
                result = {True: 'omi', False: 'landsat'}
                result = result[du.is_omi(fn)]
            else:
                result = {True: 'Both', False: None}
                result = result[du.is_omi(fn)]
            return result
            
    @staticmethod
    def get_tabular_stype(model):
        if model == 'airnow':
            return 'airnow'
        else:
            return 'tabular'

    @staticmethod
    def get_netcdf_stype(model):
        if model == 'lis':
            return 'lis'
        elif model == 'wrf':
            return 'wrf'
        elif model == 'omi':
            return 'omi'
        elif model == 'mopitt':
            return 'mopitt'
        else: 
            return 'netcdf'

    def get_stype(self):
        """
        Creates and returns the source type given the data type 
        :return: str : stype
        """
        if self.dtype == 'hdf':
            return self.get_hdf_stype(self.model, self.fn)
        elif self.dtype == 'netcdf':
            return self.get_netcdf_stype(self.model)
        elif self.dtype == 'tabular':
            return self.get_tabular_stype(self.model)
        else:
            print("Data reader class not identified - please provide data type argument (-d or --dtype)")
            sys.exit()
