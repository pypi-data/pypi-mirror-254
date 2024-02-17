from abc import ABC, abstractmethod
from eviz.lib.iviz import params_util


class BaseReader(ABC):

    xc = None
    yc = None
    tc = None
    zc = None

    def __init__(self, filename, model):
        self.fn = filename
        self.stype = model
        self.model = model

        self.meta_coords = params_util.load_model_coords()
        self.xc, self.yc, self.tc, self.zc = self.set_dim_params(self.model, 
            self.xc, self.yc, self.tc, self.zc)

    # @abstractmethod
    def open_file(self, fn, variable):
        pass

    def set_dim_params(self, model, xc, yc, zc, tc):
        """
        Set all xc, yc, tc, and zc parameter objects according to the determined models
        xc, yc, tc, and zc labels found in the meta_coords.yml file.

                Parameters:
                        xc (param): dimension
                        yc (param): dimension
                        tc (param): dimension
                        zc (param): dimension

                Returns:
                        xc (param): dimension
                        yc (param): dimension
                        tc (param): dimension
                        zc (param): dimension
        """
        meta_coords = self.meta_coords

        if model == 'base':
            xc = 'lon'
            yc = 'lat'
            tc = 'time'

        if model == 'ccm':
            xc = meta_coords['xc']['ccm']
            yc = meta_coords['yc']['ccm']
            zc = meta_coords['zc']['ccm']
            tc = meta_coords['tc']['ccm']

        elif model in ['cf', 'merra-2']:
            xc = meta_coords['xc']['cf']
            yc = meta_coords['yc']['cf']
            tc = meta_coords['tc']['cf']
            zc = meta_coords['zc']['cf']

        elif model == 'lis':
            xc = meta_coords['xc']['lis']['dim']
            yc = meta_coords['yc']['lis']['dim']
            tc = meta_coords['tc']['lis']['dim']
            
        elif model == 'gmi':
            xc = meta_coords['xc']['gmi']
            yc = meta_coords['yc']['gmi']
            zc = meta_coords['zc']['gmi']
            tc = meta_coords['tc']['gmi']

        elif model == 'omi':
            xc = meta_coords['xc']['omi']
            yc = meta_coords['yc']['omi']
            tc = meta_coords['tc']['omi']

        elif model == 'omi-tco3':
            xc = meta_coords['xc']['omi']
            yc = meta_coords['yc']['omi']
            tc = meta_coords['tc']['omi']

        elif model == 'omi':
            xc = meta_coords['xc']['omi']
            yc = meta_coords['yc']['omi']
            tc = meta_coords['tc']['omi']

        elif model == 'airnow': 
            xc = meta_coords['xc']['airnow']
            yc = meta_coords['yc']['airnow']
        
        elif model == 'wrf':
            xc = meta_coords['xc']['wrf']['coords'].split(",")[0]
            yc = meta_coords['yc']['wrf']['coords'].split(",")[0]
            tc = meta_coords['tc']['wrf']['dim']
            zc = meta_coords['zc']['wrf']['dim'].split(",")[0]

        elif model == 'spacetime':
            xc = meta_coords['xc']['spacetime']
            yc = meta_coords['yc']['spacetime']
            tc = meta_coords['tc']['spacetime']
            zc = meta_coords['zc']['spacetime']
            self.model = 'base'

        elif model == 'timeseries':
            xc = meta_coords['xc']['timeseries']
            yc = meta_coords['yc']['timeseries']
            self.model = 'base'

        elif model == 'test':
            xc = meta_coords['xc']['test']['coords'].split(",")[0]
            yc = meta_coords['yc']['test']['coords'].split(",")[0]
            self.model = 'base'

        elif model is None:
            pass
        return xc, yc, tc, zc 
