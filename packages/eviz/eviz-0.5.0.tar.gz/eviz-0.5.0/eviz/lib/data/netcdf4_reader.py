from dataclasses import dataclass, field
from typing import Any

import xarray as xr

from eviz.lib.data.reader import DataReader


@dataclass
class NetCDFDataReader(DataReader):
    datasets: list = field(default_factory=list)
    findex: int = 0

    def __post_init__(self):
        super().__post_init__()

    def read_data(self, file_path: str) -> Any:
        """ Helper function to open and define a dataset

        Parameters:
            fid (int) : file id (starts at 0)
            file_path (str) : name of file associated with fid

        Returns:
            unzipped_data (xarray.Dataset) : dict with xarray dataset information
        """
        self.logger.debug(f"Loading NetCDF data from {file_path} , fid: {self.findex}")
        unzipped_data = {}
        if "*" in file_path:
            with xr.open_mfdataset(file_path, decode_cf=True) as ds:
                f = self._rename_dims(ds)
                unzipped_data['id'] = self.findex
                unzipped_data['ptr'] = f
                unzipped_data['regrid'] = False
                unzipped_data['vars'] = f.data_vars
                unzipped_data['attrs'] = f.attrs
                unzipped_data['dims'] = f.dims
                unzipped_data['coords'] = f.coords
                unzipped_data['filename'] = "".join(file_path)
                # TODO: get_season_from_file(file_name)
                unzipped_data['season'] = None
                self.findex += 1
        else:
            with xr.open_dataset(file_path, decode_cf=True) as ds:
                f = self._rename_dims(ds)
                unzipped_data['id'] = self.findex
                unzipped_data['ptr'] = f
                unzipped_data['regrid'] = False
                unzipped_data['vars'] = f.data_vars
                unzipped_data['attrs'] = f.attrs
                unzipped_data['dims'] = f.dims
                unzipped_data['coords'] = f.coords
                unzipped_data['filename'] = "".join(file_path)
                # TODO: get_season_from_file(file_name)
                unzipped_data['season'] = None
                self.findex += 1
        processed_data = self._process_data(unzipped_data)
        self.datasets.append(processed_data)
        return processed_data

    def _rename_dims(self, ds):
        """ Set Eviz recognized dims """
        if self.source_name in ['wrf', 'lis']:
            return ds
        xc = self._get_model_dim_name('xc')
        yc = self._get_model_dim_name('yc')
        zc = self._get_model_dim_name('zc')
        tc = self._get_model_dim_name('tc')
        ds = ds.rename({xc: 'lon', yc: 'lat'})  # TODO: why can't I use, inplace=True?
        try:
            ds = ds.rename({zc: 'lev'})
        except:
            pass
        try:
            ds = ds.rename({tc: 'time'})
        except:
            pass
        return ds

    def _process_data(self, data):
        self.logger.debug(f"Preparing NetCDF data")
        return data

    def get_findex(self, data_to_plot):
        try:
            return data_to_plot[5]
        except IndexError:
            return data_to_plot[3]

    def _get_model_dim_name(self, dim_name):
        return self.meta_coords[dim_name][self.source_name]

