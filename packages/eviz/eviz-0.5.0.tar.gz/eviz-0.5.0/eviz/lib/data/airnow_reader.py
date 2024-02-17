import pandas as pd
import os

from .base_reader import BaseReader


class AirNowReader(BaseReader):

    def __init__(self, filename, model):
        super().__init__(filename, model)
        self.data = self.open_file(filename)

    def open_file(self, filepath):
        """
        Function to read measurements from EPA data file

        Inputs:
            path (str):       path to EPA daily data (v2) file
        
        Output:
            pandas dataframe with the following fields:
                Date, Latitude, Longitude, SiteName, var value (units: ppb)
        """
        from glob import glob

        # Check if file exists
        if not os.path.exists(filepath):
            raise OSError("File not found: " + filepath)

        # files to be read
        is_dir = False
        if os.path.isdir(filepath):
            files = glob(filepath + '/HourlyAQObs_*.dat')
            is_dir = True
        elif os.path.isfile(filepath):
            files = filepath

        alldata = pd.DataFrame()

        if type(files) == list:
            for f in files:
                thisdata = pd.read_csv(f)
                alldata = pd.concat([alldata, thisdata], ignore_index=True)
                outdata = alldata
        else:
            thisdata = pd.read_csv(files)

            alldata = pd.concat([alldata, thisdata], ignore_index=True)
            outdata = alldata

        # create time column
        alldata['time'] = pd.to_datetime(
                                (alldata.ValidDate+ ' ' +alldata.ValidTime),
                                format='%m/%d/%y %H:%M')
        seldata = alldata

        # set index
        seldata=seldata.sort_values(by=['AQSID','time'])
        seldata=seldata.set_index(['time','AQSID'])
        
        # convert to xarry dataset to calculate averages
        chem_fields = ['PM25_Unit', 'OZONE_Unit','NO2_Unit',  'CO_Unit', 'SO2_Unit', 'PM10_Unit']
        selds=seldata.to_xarray()
        selds = selds.drop(chem_fields)
        outdata   = selds.to_dataframe().reset_index()

        return outdata

    @staticmethod
    def format_xr(data_xr):

        data_xr = data_xr.assign_coords({"Longitude": data_xr.Longitude, "Latitude": data_xr.Latitude})
        return data_xr
