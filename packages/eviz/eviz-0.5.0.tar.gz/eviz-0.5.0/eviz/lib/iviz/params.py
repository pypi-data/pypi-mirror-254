import holoviews as hv
import param
import panel as pn
import pandas as pd

from .base_params import BaseParams
from ..data.data_selector import DataSelector
from eviz.lib.iviz import params_util

pn.extension()
hv.extension('bokeh', logo=False)

default_plots_types = {
    'XY (Lat/lon)': 'xy', 
    'Boxplot (field/time)': 'box',
    'Histogram (field/time)': 'hist',
    'Field avg': '1d',
}

        # avail_plot_types = {
        #     'XY (Lat/lon)': 'xy', 
        #     'YZ (Lat/lev)': 'yz',
        #     'Profile (field/lev) Plot': 'zt', 
        #     'Polar region plot': 'polar',
        #     'Field avg': '1d',
        #     'Total column': 'tc'
        # }


class DatasetParams(BaseParams):
    """
    The DatasetParams class configures iviz parameters from an input Xarray Dataset or 
    DataArray's dimensions and fields. 

    Attributes:
            dataInput (str): input file information, either a param.Selector or a filename;
            file (xr): xarray DatArray or Dataset, ingested by data module;
            model (str): earth system model input or determined;
    """

    def __init__(self, dataInput, file, model, **params):
        super().__init__(dataInput=dataInput, file=file, model=model, **params)

    def _set_params(self):
        """
        Run needed functions to set main class parameters. Sets all coordinate labels,
        file name, and plot types available.

        """
        self.keys = params_util.get_keys(self.file)
        self.coords = params_util.get_coords(self.file)
        self.xc, self.yc, self.tc, self.zc = self.set_dim_params(model=self.model, xc=self.xc, yc=self.yc, 
                                                                    tc=self.tc, zc=self.zc)
        # self.format_tc()
        self.set_proj_from_attrs()
        self.set_attrs()
        self.set_param_values()
        plot_types, default_types = self.get_avail_plot_types(self.file[self.field], 
                                                # self.file[self.field], #meant for data2d but not defined yet 
                                                self.xc, self.yc, self.tc, self.zc)
        self.set_avail_plot_types(plot_types, default_types)
        self.input = self.set_input()

    # @param.depends('multi_file', watch=True)
    def format_tc(self):
        """
        Try and except bloc to format the time coordinate of the data.

        Sets:
                file (xr): opened xarray file time dimension
        """
        try: 
            self.file[self.tc] = pd.DatetimeIndex(self.file[self.tc].values)
            self.file[self.tc] = self.file[self.tc].dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            print(' Could not format time string ')

    # @param.depends('field', watch=True)
    def set_attrs(self):
        """
        Check that all attributes that are needed by tool are provided in the Dataset.attrs 

        """
        self.file = params_util.set_units_in_attrs(self.file, self.keys)
        self.file = params_util.set_long_name_in_attrs(self.file, self.keys)

    def get_3d_fields(self, data):
        """
        Given input data, filter out any fields that have more than 3 dimensions. Only
        use 3d fields for plotting.

        Parameters:
                data (xarray): xarray dataset
        Returns:
                plotting_fields (list): list of strings of each field with >= 3d
        """
        plotting_fields = []
        for f in list(data.keys()):
            if len(list(data[f].dims)) >= 2:
                if len(list(data[f].dims)) < 5:
                    if str(f) != 'lat' and str(f) != 'lon':
                        plotting_fields.append(f)
        return plotting_fields

    def check_for2d_file2(self, ndims):
        """
        For second file, check for 4 dimensions.

                Parameters:
                        ndims (int): number of dimensions
        """
        if ndims < 4:
            self.param.z2.precedence = -1

    def set_proj_from_attrs(self):
        """
        Get the projection attribute from the data if it is provided, and set proj parameter.

                Parameters:
                        proj (str): cartopy projection parameter
        """
        if 'projection' in self.file.attrs:
            proj = str(self.file.attrs['projection']).title().strip().replace(" ","")
            self.proj = proj
        elif 'MAP_PROJ_CHAR' in self.file.attrs:
            proj = str(self.file.attrs['MAP_PROJ_CHAR']).title().strip().replace(" ","")
            self.proj = proj
        elif 'MAP_PROJECTION' in self.file.attrs:
            proj = str(self.file.attrs['MAP_PROJECTION']).title().strip().replace(" ","")
            self.proj = proj

    def set_tc_bounds(self, tc, data, coords):
        """
        Set time coordinate slider values and bounds according to data tc limits.

        Parameters:
                tc (str): time coordinate
                data (xarray): data
                coords (list): list of coords from data
        """
        ### If tc in data coords, re-set to 0, get bounds, check precedence, 
        ### and set bounds. If not in data coords, set to None and set precedence. 
        if tc is not None:
            self.t = 0
            t_length = len(data[tc].values)

            if t_length != 1:
                end_t = t_length - 1
                t_bounds = (0, end_t)
                self.param['t'].bounds = t_bounds
                self.param['t'].precedence = +1
                self.gif_dim_opts.append(tc)
            else:
                self.param['t'].precedence  = -1

        else:
            self.param['t'].precedence = -1

    def set_zc_bounds(self, yc, zc, data, coords):
        """
        Set z coordinate slider values and bounds according to data zc limits.

        Parameters:
                zc (str): vertical coordinate
                data (xarray): data
                coords (list): list of coords from data
        """
        ### If zc is in data coords, get the bounds, make sure the parameter precedence 
        ### is positive, and re-set the bounds. 
        if zc is not None:
            if zc in coords or zc in list(data.dims):
                self.z = 0 
                length = len(data[zc].values)
                if length != 1:
                    end_bound = length - 1
                    bounds = (0, end_bound)
                    self.param['z'].bounds = bounds
                    self.set_zc_yzplot_limits_sliders(data, zc)
                    ### Also set y and z sliders to min and maxes of data
                    ## yz_ylim and yz_xlim is zonal x and y, so y and z
                    if len(data[yc].values) > 1:
                        self.set_yc_yzplot_limits_sliders(data, yc)
                else:
                    self.param['z'].precedence = -1
                    self.param.yz_ylim.precedence = -1
                    self.param.yz_xlim.precedence = -1
            else:
                self.param['z'].precedence = -1
                self.param.yz_ylim.precedence = -1
                self.param.yz_xlim.precedence = -1
        else: ## if zc is not in data coords
            ##turn off parameter precedence, set class var to None
            self.param['z'].precedence = -1
            self.param.yz_ylim.precedence = -1
            self.param.yz_xlim.precedence = -1

    def set_yc_yzplot_limits_sliders(self, data, yc):
        """
        Set x-coordinate(xc) for yzplot sliders bounds according to data x and y values.

        Parameters:
                xc (str): x coordinate
                data (xarray): data
        """
        yvals = (data[yc].values.min(), data[yc].values.max())
        self.param.yz_xlim.bounds = yvals
        self.yz_xlim = yvals
        self.param.yz_xlim.step = 1.0
        self.param.yz_ylim.step = 1.0
        self.gif_dim_opts.append(self.zc)

    def set_zc_yzplot_limits_sliders(self, data, zc):
        """
        Set x-coordinate(xc) for yzplot sliders bounds according to data x and y values.

        Parameters:
                xc (str): x coordinate
                data (xarray): data
        """
        zvals = (data[zc].values.min(), data[zc].values.max())
        self.param.yz_ylim.bounds = zvals
        self.yz_ylim = zvals

    def set_xc_xyplot_limits_sliders(self, data, xc):
        """
        Set x-coordinate(xc) xyplot sliders bounds according to data x and y values.

        Parameters:
                xc (str): x coordinate
                data (xarray): data
        """
        xvals = (data[xc].values.min(), data[xc].values.max())
        self.param.xy_xlim.bounds = xvals
        self.xy_xlim = xvals
        self.globallons = xvals

    def set_yc_xyplot_limits_sliders(self, data, yc):
        """
        Set y-coordinate(yc) xyplot sliders bounds according to data x and y values.

        Parameters:
                yz (str): y coordinate
                data (xarray): data
        """
        yvals = (data[yc].values.min(), data[yc].values.max())
        self.param.xy_ylim.bounds = yvals
        self.xy_ylim = yvals
        self.globallats = yvals

    def set_param_values(self):
        """
        Set all parameters for file. Includes configuring fields to the data's 
        variables, the x and y extents, and defining dimensions that can 
        iterated over for a gif. 

        """
        self.gif_dim_opts = []
        self.set_tc_bounds(self.tc, self.file, self.coords)
        self.set_zc_bounds(self.yc, self.zc, self.file, self.coords)

        plotting_fields = self.get_3d_fields(self.file)
        self.param['field'].objects = plotting_fields

        self.field = self.param['field'].objects[0]

        if len(self.file[self.field][self.xc].values) != 1:
            xvals = (self.file[self.field][self.xc].values.min(), 
                     self.file[self.field][self.xc].values.max())
            self.set_xc_xyplot_limits_sliders(self.file, self.xc)

        else:
            xvals = (self.file[self.field][self.xc].values.min(), 
                     self.file[self.field][self.xc].values.max())
            self.xy_xlim.precedence = -1
            self.xy_xlim = xvals
        
        if len(self.file[self.field][self.yc].values) != 1:
            yvals = (self.file[self.field][self.yc].values.min(), 
                     self.file[self.field][self.yc].values.max())
            self.set_yc_xyplot_limits_sliders(self.file, self.yc)

        else:
            yvals = (self.file[self.field][self.yc].values.min(), 
                     self.file[self.field][self.yc].values.max())

            self.param.xy_ylim.precedence = -1
            self.param.yz_ylim.precedence = -1
            self.xy_ylim = yvals

        self.gif_dim.options = self.gif_dim_opts

    def set_f2_field(self, f1keys, f2keys):
        """
        Set the variable value for the secondary file.

        Parameters:
                f1keys (list): file 1 keys
                f2keys (list): file 2 keys

        Returns:
                plotval (str): default variable for file 2. 
        """
        self.param['comparison_field'].objects = f2keys
        if (self.comparison_field is None) or (self.comparison_field not in f2keys):
            self.param.set_param(comparison_field=f2keys[0])

        if f2keys != f1keys:
            self.param.comparison_field.precedence = 1
            # plotval = self.comparison_field
                # plotval = self.comparison_field
        # else:
            # pass
            # plotval = self.field
        # return plotval

    @param.depends('multi_file', watch=True)
    def update_files(self):
        """
        On file selection change, update coordinate parameters for data, replace variable
        and dimension values, re-set parameters. Triggered by 'multi_file' param.
        """
        if type(self.dataInput) == param.Selector:
            self.file = DataSelector(self.multi_file, self.model).data
            # self.file = DataSelector(self.multi_file, None).data
            self.keys = params_util.get_keys(self.file)
            self.coords = params_util.get_coords(self.file)
            self.ndims = params_util.get_ndims(self.file) 
            self.dims = params_util.get_dims(self.file)
            self.xc, self.yc, self.tc, self.zc = self.set_dim_params(model=self.model, xc=self.xc,
                                            yc=self.yc, tc=self.tc, zc=self.zc)
            # self.format_tc()
            self.set_attrs()
            self.set_param_values()
            plot_types, default_types = self.get_avail_plot_types(self.file[self.field], #self.file[self.field],
                                            self.xc, self.yc, self.tc, self.zc)
            self.set_avail_plot_types(plot_types, default_types, self.plot_type.values)
            self.input = self.set_input()

    def get_avail_plot_types(self, data, xc, yc, tc, zc):
        """
        Evaluate data x, y, t, and z values to determine what plot types are available.

        Parameters:
                data (xarray): data
                xc (str): x coordinate
                yc (str): y coordinate
                tc (str): t coordinate
                zc (str): z coordinate
        """

        avail_plot_types = {
            'XY (Lat/lon)': 'xy', 
            'YZ (Lat/lev)': 'yz',
            'Profile (field/lev) Plot': 'zt', 
            'Polar region plot': 'polar',
            'Field avg': '1d',
            'Total column': 'tc'
        }
        plot_types = avail_plot_types
        default_plots = default_plots_types

        if len(list(data[yc].values)) == 1 or len(list(data[xc].values)) == 1: #check for xy
            plot_types.pop('XY (Lat/lon)', None)
            default_plots.pop('XY (Lat/lon)', None)

        if zc is not None:
            if zc in list(data.coords) or zc in list(data.dims):
                #Make sure that the file and variable actually has multiple lev values 
                if len(list(data[zc].values)) == 1 or len(list(data[yc].values)) == 1:
                    plot_types.pop('YZ (Lat/lev)', None)
                    plot_types.pop('YZ (Lat/lev)', None)
                    plot_types.pop('Total column', None)
                    plot_types.pop('Z avg. boxplot', None)
                    plot_types.pop('Z avg. histogram (field/time)', None)
                    plot_types.pop('Profile (field/lev) Plot', None)
                    default_plots.pop('YZ (Lat/lev)', None)
                else:
                    plot_types.update({'YZ (Lat/lev)': 'yz'})
                    plot_types.update({'Total column': 'tc'})
                    default_plots.update({'YZ (Lat/lev)': 'yz'})
            else:
                plot_types.pop('YZ (Lat/lev)', None)
                plot_types.pop('YZ (Lat/lev)', None)
                plot_types.pop('Total column', None)
                plot_types.pop('Z avg. boxplot', None)
                plot_types.pop('Z avg. histogram (field/time)', None)
                plot_types.pop('Profile (field/lev) Plot', None)
                default_plots.pop('YZ (Lat/lev)', None)
        else:
            plot_types.pop('YZ (Lat/lev)', None)
            plot_types.pop('YZ (Lat/lev)', None)
            plot_types.pop('Total column', None)
            plot_types.pop('Z avg. boxplot', None)
            plot_types.pop('Z avg. histogram (field/time)', None)            
            plot_types.pop('Profile (field/lev) Plot', None)
            default_plots.pop('YZ (Lat/lev)', None)

        if tc in list(data.coords) or tc in list(data.dims):
            if len(list(data[tc].values)) > 1:
                plot_types.update({'TS (field/time)': 'ts'})
            if len(list(data[tc].values)) > 1 and len(list(data[xc].values)) > 1:
                plot_types.update({'XT (Lon/time)': 'xt'})
            if len(list(data[tc].values)) > 1 and len(list(data[yc].values)) > 1:
                plot_types.update({'YT (Lon/time)': 'yt'})

        if self.model == 'lis' or self.model == 'wrf':
            plot_types.pop('Polar region plot', None)

        # if self.check_for_zeros(data2d):
        #     self.plot_kind.value = ['quadmesh']

        return plot_types, default_plots

    def check_for_zeros(self, data):
        """
        If all values are zero, contours and filled contours can not be plotted. 
        Check for all 0's by calculating the mean of the input data. 

        Parameters:
                data (xr): xarray DataArray or Dataset;
        """
        if float(data.mean().values) == 0:
            return True
        else:
            return False

    def set_avail_plot_types(self, plot_types, default_plots, current_plots=None):
        """
        Set plot types widgets options for suer selection.

        Parameters:
                plot_types (dict): plot types available;
                default_plots (dict): default plots;
        """
        last = plot_types.popitem()
        newdict = {last[0]: last[1]}
        plot_types = {**plot_types, **newdict}

        if current_plots is not None:
            if list(default_plots.values()) == current_plots:
                self.plot_type.options = plot_types
            else:
                if any(plot in current_plots for plot in list(default_plots.values())):
                    self.plot_type.options = plot_types
                else:
                    # self.plot_type.value = list(default_plots.values())
                    pass
        else:
            self.plot_type.options = plot_types

        values = []
        for p in self.plot_type.value:
            if p in list(self.plot_type.options.values()):
                values.append(p)
        self.plot_type.value = values
