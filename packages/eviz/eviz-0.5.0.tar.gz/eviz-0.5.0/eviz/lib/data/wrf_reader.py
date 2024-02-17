import sys

import xarray as xr
from .netcdf_reader import NetcdfReader


class WrfReader(NetcdfReader):

    def __init__(self, filename, model, is_url):
        super().__init__(filename, model, is_url=is_url)
        self.fn = filename
        self.data = self._process_data()

    def open_file(self):
        try:
            data = xr.open_dataset(self.fn)
            #else input is a link to an opendap dataset or path to .nc4 file
        except ValueError:
            try:
                data = xr.open_dataset(self.fn, decode_times=False)
            except Exception as e:
                print(e)
                print(' Unrecognized input ')
                sys.exit(1)
        return data
    
    def get_lat_lons(self, data):
        """
        Get longitude and latitude values from provided dataset. 

        Parameters:
                data (xr.Dataset): wrf dataset with XLONG, XLAT and staggered
                coordinates.

        Returns:
                lons      (array): longitude values
                lats      (array): latitude values
                levs      (array): bottom_top values
                lons_v    (array): longitude v stagger values
                lats_v    (array): latitude v stagger values
                lons_u    (array): longitude u stagger values
                lats_u    (array): latitude u stagger values
                levs_stag (array): bottom_top_stag values
        """
        lons = data.XLONG[-1,-1,:].drop(['XLAT', 'XTIME'])
        # lons = data.XLONG[-1,-1,:].drop(['XLAT', 'XTIME']).rename({'west_east': 'lon'})
        # lats = data.XLAT[-1,:,-1].drop(['XLONG', 'XTIME']).rename({'south_north': 'lat'})
        # lons = data[self.xc][-1,-1,:].drop([self.yc, 'XTIME'])
        lats = data.XLAT[-1,:,-1].drop(['XLONG', 'XTIME'])

        levs = data.bottom_top

        lons_v = data.XLONG_V[-1,-1,:].drop(['XLAT_V', 'XTIME'])
        lats_v = data.XLAT_V[-1,:,-1].drop(['XLONG_V', 'XTIME'])
        lons_u = data.XLONG_U[-1,-1,:].drop(['XLAT_U', 'XTIME'])
        lats_u = data.XLAT_U[-1,:,-1].drop(['XLONG_U', 'XTIME'])

        lons_v = data.XLONG_V[-1,-1,:].drop(['XLAT_V', 'XTIME'])
        lats_v = data.XLAT_V[-1,:,-1].drop(['XLONG_V', 'XTIME'])
        lons_u = data.XLONG_U[-1,-1,:].drop(['XLAT_U', 'XTIME'])
        lats_u = data.XLAT_U[-1,:,-1].drop(['XLONG_U', 'XTIME'])


        levs_stag = data.bottom_top_stag
        return lons, lats, levs, lons_v, lats_v, lons_u, lats_u, levs_stag

    # @param.depends('params.file')
    def _process_data(self)->xr.Dataset:
        """
        Do necessary processing of dataset before plotting, get latitude and longitude
        values, and assign coordinate values to all dimensions of dataset. 

        Returns:
                data (xr.Dataset): data with proper coordinate and dimension
                values.
        """
        dataset = self.open_file()

        lons, lats, levs, lons_v, lats_v, lons_u, lats_u, levs_stag = self.get_lat_lons(dataset)

        coords = {
            'XLAT': lats,
            'XLONG': lons,
            'XLAT_U': lats_u,
            'XLONG_U': lons_u,
            'XLAT_V': lats_v,
            'XLONG_V': lons_v,
            'bottom_top_stag': levs_stag,
            'bottom_top': levs            
        }

        dataset = dataset.assign_coords(coords)

        dataset = dataset.rename({
            'XLAT': 'south_north',
            'XLONG': 'west_east',
            'XTIME': 'Time',
            'XLONG_U': 'west_east_stag',
            'XLAT_V': 'south_north_stag',
        })

        # dataset = dataset.rename({
        #     'XLAT': 'lat',
        #     'XLONG': 'lon',
        #     'XTIME': 'Time',
        #     'XLONG_U': 'west_east_stag',
        #     'XLAT_V': 'south_north_stag',
        # })

        # dataset = dataset.rename_dims({'south_north': 'lat', 'west_east': 'lon'})

        dataset = dataset.drop(['XLONG_V', 'XLAT_U'])

        return dataset
