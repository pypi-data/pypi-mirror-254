import xarray as xr
import numpy as np
from .netcdf_reader import NetcdfReader


class LisReader(NetcdfReader):

    def __init__(self, filename, model, is_url):
        super().__init__(filename, model, is_url=is_url)
        self.fn = filename

        self.data = self._process_data()

    @staticmethod
    def get_lat_lons(data):
        """
        Get the latitude and longitude coordinate values from the data's lat and lon 
        variables. 

                Parameters:
                        data (xr.Dataset): LIS data containing lat and lon variables.

                Returns:
                        xs (array): x coordinate values
                        ys (array): y coordinate values

        """
        xs, ys, extent, central_lon, central_lat = None, None, None, None, None

        lons = data.lon[0,:]
        lats = data.lat[:,0]

        xs = lons
        ys = lats
        xs = np.array(lons)
        ys = np.array(lats)

        dx = (round(float(data.attrs['DX']), 3)) #/ 1000.0
        dy = (round(float(data.attrs['DY']), 3)) #/ 1000.0

        # Some LIS coordinates are NaN. The following workaround fills out those elements
        # with reasonable values:
        idx = np.argwhere(np.isnan(xs))
        for i in idx:
            xs[i] = xs[i-1] + dx/1000.0/100.0
        idx = np.argwhere(np.isnan(ys))
        for i in idx:
            ys[i] = ys[i-1] + dy/1000.0/100.0

        latS = min(ys)
        latN = max(ys)
        lonW = min(xs)
        lonE = max(xs)
        extent = [lonW, lonE, latS, latN]
        central_lon = np.mean(extent[:2])
        central_lat = np.mean(extent[2:])
        return xs, ys

    def _process_data(self)->xr.Dataset:
        """
        Do necessary processing of dataset before plotting, get latitude and longitude
        values, and assign coordinate values to all dimensions of dataset. 

                Returns:
                        data (xr.Dataset): data with proper coordinate and dimension 
                        values. 
        """
        # get attributes from dataset
        try:
            dataset = xr.open_dataset(self.fn)
            #else input is a link to an opendap dataset or path to .nc4 file
        except ValueError:
            try:
                dataset = xr.open_dataset(self.fn)
            except Exception as e:
                print(e)
                print(' Unrecognized input ')
                sys.exit(1)
        
        attrs = dataset.attrs
        
        xs, ys = self.get_lat_lons(dataset)

        # get grid cells in x, y dimensions
        coords = {
            'north_south': ys,
            'east_west': xs
        }
        
        lon_attrs = dataset.lon.attrs
        lat_attrs = dataset.lat.attrs
        
        # rename the original lat and lon variables
        dataset = dataset.rename({'lon':'orig_lon', 'lat':'orig_lat'})
        dataset = dataset.drop(['orig_lon', 'orig_lat'])
        # rename the grid dimensions to lat and lon
        # assign the coords above as coordinates
        dataset = dataset.assign_coords(coords)
        dataset.east_west.attrs = lon_attrs
        dataset.north_south.attrs = lat_attrs

        return dataset
