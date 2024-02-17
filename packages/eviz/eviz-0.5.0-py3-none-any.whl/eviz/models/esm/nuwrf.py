import logging
import warnings
from eviz.lib.eviz.config import Config

warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)


class NuWrf:
    """ Define NUWRF specific model data and functions."""

    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    @staticmethod
    def set_global_attrs(source_name, ds_attrs):
        """Return a tuple of global attributes from WRF or LIS dataset """
        tmp = dict()
        for attr in ds_attrs.keys():
            try:
                tmp[attr] = ds_attrs[attr]
                if source_name == "lis":
                    if attr == "DX" or attr == "DY":
                        # Convert LIS units to MKS
                        tmp[attr] = ds_attrs[attr] * 1000.0
            except KeyError:
                tmp[attr] = None
        return tmp

    def coord_names(self, source_name, source_data, field_name, pid):
        """ Get WRF coord names based on field and plot type

        Parameters:
            source_name (str) : source name
            source_data (dict) : source data
            field_name(str) : Field name associated with this plot
            pid (str) : plot type
        """
        coords = []
        d = source_data['vars'][field_name]
        if source_name == 'wrf':
            stag = d.stagger
            xsuf, ysuf, zsuf = "", "", ""
            if stag == "X":
                xsuf = "_stag"
            elif stag == "Y":
                ysuf = "_stag"
            elif stag == "Z":
                zsuf = "_stag"

            for name in self.get_model_coord_name(source_name, 'xc').split(","):
                if name in d.coords.keys():
                    coords.append((name, self.get_model_dim_name(source_name, 'xc')+xsuf))
                    break

            for name in self.get_model_coord_name(source_name, 'yc').split(","):
                if name in d.coords.keys():
                    coords.append((name, self.get_model_dim_name(source_name, 'yc')+ysuf))
                    break
        else:  # 'lis'
            xc = self.get_model_dim_name(source_name, 'xc')
            if xc:
                coords.append(xc)
            yc = self.get_model_dim_name(source_name, 'yc')
            if yc:
                coords.append(yc)

        if source_name == 'wrf':
            zc = self.get_field_dim_name(source_name, source_data, 'zc', field_name)
            if zc:
                coords.append(zc)
        else:
            for name in self.get_model_dim_name(source_name, 'zc').split(","):
                if name in d.coords.keys():
                    coords.append(name)
                    break

        tc = self.get_field_dim_name(source_name, source_data, 'tc', field_name)
        if tc:
            coords.append(tc)

        dim1, dim2 = None, None
        if source_name == 'wrf':
            if 'yz' in pid:
                dim1 = coords[1]
                dim2 = coords[2]
            elif 'xt' in pid:
                dim1 = 'Time'
            elif 'tx' in pid:
                dim1 = coords[0]
                dim2 = 'Time'
            else:
                dim1 = coords[0]
                dim2 = coords[1]
        else:
            if 'xt' in pid:
                dim1 = coords[3]
            elif 'tx' in pid:
                dim1 = coords[0]
                dim2 = coords[3]
            else:
                dim1 = coords[0]
                dim2 = coords[1]
        return dim1, dim2

    def get_field_dim_name(self, source_name: str, source_data: dict, dim_name: str, field_name: str):
        d = source_data['vars'][field_name]
        field_dims = list(d.dims)   # use dims only!?
        names = self.get_model_dim_name(source_name, dim_name).split(',')
        common = list(set(names).intersection(field_dims))
        dim = list(common)[0] if common else None
        return dim

    def get_model_dim_name(self, source_name: str, dim_name: str):
        try:
            dim = self.config.meta_coords[dim_name][source_name]['dim']
            return dim
        except KeyError:
            return None

    def get_model_coord_name(self, source_name: str, dim_name: str):
        try:
            coord = self.config.meta_coords[dim_name][source_name]['coords']
            return coord
        except KeyError:
            return None

    def get_dd(self, source_name, source_data, dim_name, field_name):
        d = source_data['vars'][field_name]
        field_dims = d.dims
        names = self.get_model_dim_name(source_name, dim_name)
        for d in field_dims:
            if d in names:
                return d
