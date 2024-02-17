import xarray as xr
import param
import os
import pandas as pd
import numpy as np

from eviz.lib.xarray_utils import compute_mean_over_dim


class TimeAvg:
    """ Create a time averaged file.

    Parameters:
            files (list): all files to average over;
            run (pn.widgets.Butoon): panel button to trigger averaging;
            all_vars (bool): whether to use all variables in provided file;
            var_inp (str): variables to use;
    """

    label = None
    
    def __init__(self, files, run, tc, all_vars, var_inp):
        self.files = files
        self.file = files[0]
        self.run_time_avg_btn = run
        self.tc = tc
        self.all_variables = all_vars
        self.variable_input = var_inp
        self.label = None
        self.output = None
        self.time_series_mean = None

        self.data_mean = None
        self.set_ds()
        self.avg_data = None

        self.average_by_time()
    
        super().__init__()
    
    def set_ds(self):
        """
        Determines the input data and opens with xarray, whether provided a filename
        or a directory path.

        """
        if os.path.isdir(self.files[0]):
            pth = os.path.join(self.files[0] + '/*nc*')
            # self.label = self.files[0]
            try:
                self.label = os.path.split(self.files[0])[-1::][0]
            except:
                self.label = self.files[0]
            self.ds = xr.open_mfdataset(pth)
        else:
            try:
                self.label = os.path.split(self.files[0])[-1::][0]
            except:
                self.label = self.files[0]
            self.ds = xr.open_mfdataset(self.files)

    @param.depends('run_time_avg_btn.clicks')
    def average_by_time(self):
        """
        Calculate the mean over the time dimension. Write the file to disk, and set the class 
        variable output to the result.

        Parameters:
                files (list): all files to average over;
                run (pn.widgets.Butoon): panel button to trigger averaging;
                all_vars (bool): whether to use all variables in provided file;
                var_inp (str): variables to use;

        Sets:
                output (xr): averaged dataset
        """
        if self.run_time_avg_btn.clicks:
            if self.all_variables:
                avg_fields = []
                for field in self.ds.data_vars.keys():
                    avg_fields.append(compute_mean_over_dim(self.ds, mean_dim=self.tc, field_name=field))
            else: 
                try:
                    fields = self.variable_input.value
                    fields = fields.split(", ")
                    avg_fields = []
                    for field in fields:
                        avg_fields.append(compute_mean_over_dim(self.ds, mean_dim=self.tc, field_name=field))
                except:
                    print("please ensure that variables provided are correct")

            # if self.save_time_avg_file:
            ds = xr.Dataset({})
            ds = ds.assign_attrs(self.ds.attrs)
            for field in avg_fields:
                ds[field.name] = field.astype(dtype='float32')
                ds[field.name] = ds[field.name].assign_attrs(self.ds[field.name].attrs)
            
            start_date = str(self.ds[self.tc][0].values).split('T')[0]
            end_date = str(self.ds[self.tc][-1:].values[0]).split('T')[0]
            dates = start_date + "_" + end_date
            t = pd.date_range(start=start_date, end=end_date, freq="M")
            time = np.array(end_date, dtype='datetime64')
            fields = self.variable_input.value
            fiel = fields.split(", ") 

            dir_ = os.path.join(os.path.abspath(''), 'time_average_files/')

            if self.all_variables:
                output = dir_ + str(self.label)
            else:
                output = dir_ + self.label + "." + fields
            
            if os.path.exists(dir_):
                pass
            else: 
                os.makedirs(dir_)

            if self.run_time_avg_btn.clicks > 1:
                self.output = output + "(" + str(self.run_time_avg_btn.clicks) + ")" + ".iViz_tavg.nc4"
            else:
                self.output = output + ".iViz_tavg.nc4"

            ds = eval(f"ds.assign_coords({self.tc}=end_date)")
            ds = ds.expand_dims(self.tc)

            ds.to_netcdf(self.output)








