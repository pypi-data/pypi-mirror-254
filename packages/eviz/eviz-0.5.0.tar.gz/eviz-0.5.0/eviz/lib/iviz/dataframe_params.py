import param
import panel as pn
from .base_params import BaseParams
pn.extension()


class DataframeParams(BaseParams):

    """
    The DataframeParams class configures iviz parameters from an input pandas dataframe
    dimensions and fields.     

    Attributes:
            dataInput (str): input file information, either a param.Selector or a filename;
            file (xr): pandas DataFrame, ingested by data module;
            model (str): earth system model input or determined;
    """

    plot_kind = pn.widgets.MultiChoice(options=['hist', 'bar', 'scatter', 'points', 'polygons', 
                            'box', 'hexbin', 'kde', 'bivariate'], 
                            value=['points'], name='Plot kinds available', margin=10)
    basemap = param.ObjectSelector(objects=['CartoDark', 'CartoLight', 'CartoMidnight', 'ESRI', 
                            'EsriImagery', 'EsriNatGeo', 'EsriOceanBase', 'EsriOceanReference', 
                            'EsriReference', 'EsriTerrain', 'EsriUSATopo', 'OpenTopoMap', 
                            'OpenTopoMap', 'OSM', 'StamenLabels', 'StamenTerrain', 
                            'StamenTerrainRetina', 'StamenToner', 'StamenTonerBackground', 
                            'StamenWatercolor', 'Wikipedia'], default='ESRI', 
                            label='Selected basemap')
    enable_basemap = param.Boolean(False, label='Enable basemap')
    size = param.Integer(bounds=(0,150), default=4, label='Size')
    describe = param.Boolean(False, label='Describe dataset')

    def __init__(self, dataInput, file, model, **params):
        super().__init__(dataInput=dataInput, file=file, model=model, **params)
        self.plot_type.visible = False

        self.param.color_levels.precedence = -1
        self.param.column_slider.precedence = -1
        self.param.z.precedence = -1 
        self.param.t.precedence = -1
        
        self.param.xc.precedence = +1
        self.param.yc.precedence = +1

        self.param.field.label = 'Color by selected column'

    def _set_params(self):
        """
        Run needed functions to set main class parameters. Sets all coordinate labels,
        file name, and plot types available.

        """
        self.xc, self.yc = self.set_dim_params(self.model, self.xc, 
                        self.yc)
        self.set_param_values()
        self.set_input()

    # ======== TODO ======= #
    # Not ready yet. 
    # Need to re initialize 
    # Xarray params class
    # ===================== #
    # @param.depends('multi_file', watch=True)
    # def update_files(self):
    #     """
    #     On file selection change, update coordinate parameters for data, replace variable
    #     and dimension values, re-set parameters. Triggered by 'multi_file' param.
    #     """
    #     if type(self.dataInput) == param.Selector:
    #         ds = DataSelector(self.multi_file, None)
    #         self.file = ds.data
    #         self.model = ds.model
    #         self.keys = params_util.get_keys(self.file)
    #         self.coords = params_util.get_coords(self.file)
    #         self.ndims = params_util.get_ndims(self.file) 
    #         self.dims = params_util.get_dims(self.file)
    #         self.xc, self.yc, self.tc, self.zc = self.set_xarray_dim_params(model=self.model, xc=self.xc, yc=self.yc, 
    #                                                                     tc=self.tc, zc=self.zc)
    #         # self.format_tc()
    #         # self.set_attrs()
    #         self.set_param_values()
    #         plot_types, default_types = self.get_avail_plot_types(self.file[self.field], self.xc, self.yc, self.tc, self.zc)
    #         self.set_avail_plot_types(plot_types, default_types)
    #         self.input = self.set_input()

    def set_dim_params(self, model, xc, yc):
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

        if model == 'airnow': 
            xc = meta_coords['xc']['airnow']
            yc = meta_coords['yc']['airnow']

        elif model == 'timeseries':
            xc = meta_coords['xc']['timeseries']
            yc = meta_coords['yc']['timeseries']

        return xc, yc

    def set_xarray_dim_params(self, model, xc, yc, tc, zc):
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

        elif model == 'cf':
            xc = meta_coords['xc']['cf']
            yc = meta_coords['yc']['cf']
            tc = meta_coords['tc']['cf']
            zc = meta_coords['zc']['cf']

        elif model == 'lis':
            xc = meta_coords['xc']['lis']['dim']
            yc = meta_coords['yc']['lis']['dim']
            # zc = meta_coords['zc']['lis']
            tc = meta_coords['tc']['lis']['dim']
            
        elif model == 'gmi':
            xc = meta_coords['xc']['gmi']
            yc = meta_coords['yc']['gmi']
            zc = meta_coords['zc']['gmi']
            tc = meta_coords['tc']['gmi']

        elif model == 'airnow': 
            xc = meta_coords['xc']['airnow']
            yc = meta_coords['yc']['airnow']
        
        elif model == 'wrf':
            xc = meta_coords['xc']['wrf']['coords'][0]
            yc = meta_coords['yc']['wrf']['coords'][0]
            tc = meta_coords['tc']['wrf']['dim']
            zc = meta_coords['zc']['wrf']['dim']

        elif model is None:
            print(' Please enter in full, case-sensitive, which coordinate to use for x and y axis ')
            print(' Available coords: ')
            print(self.coords)
            x_user_input = input(" X coordinate: ")
            y_user_input = input(" Y coordinate: ")
            if len(self.coords) > 2:
                time_user_input = input(" Time coorinate: ")
                tc = time_user_input
            # else:
                # tc = None
            if len(self.coords) > 3: 
                z_user_input = input(" Z Coordinate (enter 'None' if None): ")
                zc = z_user_input
                z_user_input = z_user_input.lower() 
                # if z_user_input == 'none':
                    # zc = None
            # else:
                # zc = None

            xc = x_user_input
            yc = y_user_input

        return xc, yc, tc, zc 

    def set_param_values(self):
        """
        Set all parameters for file. Includes configuring fields to the data's 
        columns, and seraching for longitude or latitude columns. If not found, 
        sets x and y parameters to first and second column in dataframe. 

        """
        plotting_fields = list(self.file.columns)
        plotting_fields.insert(0, None)
        self.param['field'].objects = plotting_fields

        self.param['xc'].objects = plotting_fields
        self.param['yc'].objects = plotting_fields

        lon_strs = ['longitude', 'Longitude', 
                    'lon', 'Lon', 'lons',
                    'x', 'X']

        lat_strs = ['latitude', 'Latitude', 
                    'lat', 'Lat', 'lats',
                    'y', 'Y']

        if self.xc is None:
            for c in plotting_fields:
                if c in lon_strs:
                    self.xc = c
                elif c in lat_strs:
                    self.yc = c

        if self.xc is None:
            self.xc = plotting_fields[0]
        if self.yc is None:
            self.yc = plotting_fields[1]

    def get_avail_plot_types(self):
        pass

    def set_input(self):
        self.param.multi_file.precedence = -1
        return self.multi_file
