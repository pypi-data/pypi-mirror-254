import holoviews as hv
import param
import panel as pn
import glob
import os

pn.extension()
hv.extension('bokeh', logo=False)

from eviz.lib.iviz import params_util

avail_plot_types = {
    'XY (Lat/lon)': 'xy', 
    'YZ (Lat/lev)': 'yz',
    'Profile (field/lev) Plot': 'zt', 
    'Polar region plot': 'polar',
    'Z avg. boxplot': 'zbox',
    'Boxplot (field/time)': 'box',
    'Histogram (field/time)': 'hist',
    'Z avg. histogram (field/time)': 'zhist',
}

projections = [
    'PlateCarree', 
    'AlbersEqualArea', 
    'AzimuthalEquidistant', 
    'EckertI', 
    'EckertII', 
    'EckertIII', 
    'EckertIV', 
    'EckertV', 
    'EckertVI', 
    'EqualEarth', 
    'EquidistantConic', 
    'EuroPP', 
    # 'Geocentric': ccrs.Geocentric(),
    # 'Geodetic': ccrs.Geodetic(), 
    # 'Geostationary', 
    'Gnomonic', 
    'InterruptedGoodeHomolosine', 
    'LambertAzimuthalEqualArea', 
    'LambertConformal',
    'LambertCylindrical',
    'Mercator', 
    'Miller',
    'Mollweide',
    'NearsidePerspective',
    'NorthPolarStereo', 
    'Orthographic', 
    'Robinson', 
    'RotatedPole',
    'Sinusoidal', 
    'SouthPolarStereo', 
    'Stereographic', 
    'TransverseMerc'
]


class BaseParams(param.Parameterized):

    """
    The BaseParams class initializes all param and panel objects required by iviz. 

    Parameters:
            dataInput (str): input file information, either a param.Selector or a filename;
            file (xr): xarray DatArray or Dataset, ingested by data module;
            model (str): earth system model input or determined;
    """

    multi_file = param.Parameter(default=None, label='Select file')
    field = param.Selector(label='Variable')#, default=None)
    xc = param.ObjectSelector(default=None, precedence=-1) 
    yc = param.ObjectSelector(default=None, precedence=-1)
    tc = param.ObjectSelector(default=None, precedence=-1)
    zc = param.ObjectSelector(default=None, precedence=-1)
    z = param.Integer(default=0, label='Vertical level')
    t = param.Integer(default=0, label='Time')
    #        File 2        #
    comparison_file = param.Selector(default=None, label='Select comparison file')
    comparison_field = param.ObjectSelector(default=None, precedence=-1, label='Variables')
    xc2 = param.ObjectSelector(default=None, precedence=-1)
    yc2 = param.ObjectSelector(default=None, precedence=-1)
    zc2 = param.ObjectSelector(default=None, precedence=-1)
    tc2 = param.ObjectSelector(default=None, precedence=-1)
    z2 = param.Integer(default=0, precedence=-1, label='Vertical level')
    t2 = param.Integer(default=0, precedence=-1)

    clim = param.Range(default=None,label='Colorbar range separated by a comma')
    set_xy_clim = param.Boolean(False, label='Use custom clim?')
    clim_min = param.Number()
    clim_max = param.Number()
    zonal_clim = param.Range(default=None,label='Set colorbar range separated by a comma')
    set_yz_clim = param.Boolean(False, label='Use custom clim?')
    zonal_clim_min = param.Number()
    zonal_clim_max = param.Number()
    ymin = param.Number(default=None)
    ymax = param.Number(default=None)

    #     ### PANEL WIDGETS ###
    gif_dim = pn.widgets.RadioButtonGroup(name='Dim to gif over', width=180)
    yz_ylim = param.Range(label='Y axis range', step=1)
    yz_xlim = param.Range(label='X axis range', step=1)
    xy_ylim = param.Range(label='Y axis range', step=1)
    xy_xlim = param.Range(label='X axis range', step=1)
    xy_ylim2 = param.Range(precedence=-1, label='2nd file Y extent')
    xy_xlim2 = param.Range(precedence=-1, label='2nd file X extent')

        ##MULTI SELECT##
    plot_type = pn.widgets.MultiChoice(options=avail_plot_types, value=['xy', 'yz'], name='Plot types available', 
                            width=350, margin=10)
    plot_kind = pn.widgets.MultiChoice(options=['quadmesh', 'contourf', 'contour', 'image', 'hist', 'box', 'violin'], 
                            value=['contourf'], 
                            name='Plot kinds available', margin=10) #should change to ObjectSelector?
    plot_kind_profile = pn.widgets.MultiChoice(options=['line', 'scatter'], value=['line'], margin=10, 
                            name='Plot kinds available')

    #######################
    #      CONSTANTS      #
    #######################
    show_coastlines = param.Boolean(False)
    show_lakes = param.Boolean(False)
    show_states = param.Boolean(False)
    show_rivers = param.Boolean(False)
    show_data = param.Boolean(False)
    custom_title = param.Boolean(False)
    show_statistics = param.Boolean(False)
    tabs_switch = param.Boolean(True, label="Toggle plot tabs")
    column_slider = param.Integer(1, bounds = (1,3), label="Number of columns in plot layout")
    differencing_button = param.Action(label="Do differencing")
    show_grid = param.Boolean(False, label='Show grid')
    color_levels = param.Integer(default=18, bounds=(2,30), label='Contour color levels')
    cnorm = param.ObjectSelector(objects=['linear', 'log', 'eq_hist'], default='linear', 
                                label='Colorbar normalization')
    diff_cmap = param.ObjectSelector(objects=['bwr', 'bwr_r', 'seismic', 'RdBu', 'reds', 'blues', 
                                                'greens', 'cividis'],label='Difference plot colorbar')
    zonal_cnorm = param.ObjectSelector(objects=['linear', 'log', 'eq_hist'], default='linear', 
                                label='Zonal colorbar normalization')
    zero_clim = param.Boolean(False, label='Start colorbar at 0')
    share_colorbar = param.Boolean(True, label='Share colorbar range w/ 2nd file')
    layout = param.Parameter()
    layout2 = param.Parameter()
    regions = param.ObjectSelector(objects=['global', 'north america', 'south america', 'europe', 'asia', 
                                    'aus + oceania', 'africa'], default='global', label='Spatial select')    
    zoom = param.ObjectSelector(objects=['zoom in on data', 'zoom in on plot'], default='zoom in on plot', 
                                label='How to select')
    logy_z = param.Boolean(False, label="Log y axis on zonal plot")

    invert_yaxis_z = param.Boolean(default=True, label="Invert y axis zonal")
    invert_xaxis_z = param.Boolean(default=False, label="Invert x axis zonal")
    invert_yaxis = param.Boolean(default=False, label='Invert y axis')
    invert_xaxis = param.Boolean(default=False, label='Invert x axis')

    proj = param.ObjectSelector(objects=projections, default=projections[0], label='Select a Cartopy projection')
    diff_types = param.ObjectSelector(objects=['difference', 'percent difference', 'percent change', 'ratio'],
                                     default='difference', label='Comparison type')
    diff_types_1d = param.ObjectSelector('align', objects=['align', 'overlay'], label='Diff plot types')
    add_trop = param.Boolean(default=False, label='Add tropopause height line', precedence=-1)
    add_histo = param.Boolean(default=False, label='Adjust data values in colormap')
    # explore_files = param.Boolean(default=False, label='Explore files')
    alpha = param.Number(default=1.0, bounds=(0.0, 1.0), label='Transparency')
    
    all_variables = param.Boolean(True, label='Use all variables?')
    cmap_category = param.ObjectSelector(objects=['Diverging', 'Rainbow', 'Categorical', 'Miscellaneous', 
                                    'Uniform Sequential', 'Mono Sequential', 'Other Sequential'], 
                                    default='Diverging', label='Filter by colormap category')
    cmap_provider = param.ObjectSelector(objects=['matplotlib', 'bokeh', 'colorcet'], default='matplotlib', 
                                    label='Colormap provider')
    cmap_reverse = param.Boolean(False, label='Reverse the colormap')
    colorbar_position = param.ObjectSelector(objects=['bottom', 'top', 'right', 'left'], default='bottom', 
                                    label='Colorbar or legend location')
    cartopy_feature_scale = param.ObjectSelector(objects=['110m', '50m', '10m'], default='110m', label="Scale \
                                                    of overlay feature", precedence=1)

    cmaps_available = param.ObjectSelector(label='Select from filtered cmaps')               
    trop_field = param.ObjectSelector(label='Tropopause fields available', precedence=-1)
    hmdir = os.path.expanduser('~')
    multi_selector = pn.widgets.FileSelector(hmdir,  width=500)#align='center',
    cmap = param.ObjectSelector('rainbow', objects=['rainbow', 'viridis', 'spectral', 'colorwheel', 'YlGnBu_r',
                                     'bgy', 'plasma', 'RdYlBu_r', 'coolwarm', 'coolwarm_r', 'GnBu'], label="Colormap", 
                                     )
    comparison_source = param.ObjectSelector('ccm', objects=['ccm', 'cf', 'merra-2', 'omi', 
                                                             'mopitt'], 
                                            label='Model or observation source')

        ###PANEL WIDGETS###
        ##BUTTONS##
    save_layout_button = pn.widgets.Button(name='Save layout', align='start', width=150)
    add_files_button = pn.widgets.Button(name='Add Selections to File Options')
    add_time_series_plot_btn = pn.widgets.Button(name='Create Time Series Plot')
    add_plots_button = pn.widgets.Button(name='Plot all files')
    enable_projection = pn.widgets.Button(name='Set projection', align='start')
    gif_button = pn.widgets.Button(name='Generate gif', align='start', width=180)
    plot_second_file_button = pn.widgets.Button(name='Add secondary file', align='start', width=150)
    clear_button = pn.widgets.Button(name='Clear secondary file', align='start', width=150)
    difference_button = pn.widgets.Button(name='Create comparison', align='start', width=150)
    clear_diff_button = pn.widgets.Button(name='Clear comparison', align='start', width=150)
    save_session_button = pn.widgets.Button(name='Save Session', width=125, align='start', margin=0, visible=False)
    save_plot_opts_button = pn.widgets.Button(name='Save plot options', width=125, align='start', margin=0, visible=False)
    go_to_user_home = pn.widgets.Button(name='Go to user home dir', width=110)
    # add_to_tabs_btn = pn.widgets.Button(name='Add to tabs', width=150, margin=0)
    add_to_tabs_btn = pn.widgets.Button(name='Add to tabs', align='start', width=150)
    run_time_avg_btn = pn.widgets.Button(name='Run Time Avg')
    apply_operation_button = pn.widgets.Button(name='Apply operation to data')
    zoom_plot_button = pn.widgets.Button(name='Apply zoom to plot')

        ##TOGGLES##
    differencing_toggle = pn.widgets.Toggle(name='Create comparisons', width=150)
    animate_toggle = pn.widgets.Toggle(name='Animate', width=150)
    explore_files = pn.widgets.Toggle(name='Explore files', width=150, value=False)

        ##TEXT INPUT##
    variable_input = pn.widgets.TextInput(placeholder='Enter variables separated by a comma')
    second_file_input = pn.widgets.TextInput(name='Find files',  placeholder='Enter path here')
    title_input = pn.widgets.TextInput(name='Plot title',  placeholder='Type plot title here')
    title_input2 = pn.widgets.TextInput(name='Plot 2 title', placeholder='Type title for plot 2 here')
    units = pn.widgets.TextInput(name='units', placeholder='Change units label')
    colorbar_labels = pn.widgets.TextInput(name='Colorbar label', placeholder='Change label of colorbar')
    
        ##PROGRESS BAR##
    progressbar = pn.widgets.Progress(name='Creating gif...', active=True, width=200, visible=False)
        ##RADIO GROUP##
    operations = pn.widgets.RadioButtonGroup(options=['multiply', 'divide', 'add', 'subtract'])
    save_formats = pn.widgets.RadioBoxGroup(options=['html', 'png'], value='png', width=10, inline=True)
        ##LITERAL INPUT##
    lit_input = pn.widgets.LiteralInput(name='Enter value for operation', type=float)
        ##MENU BUTTON##
    save_menu_button = pn.widgets.MenuButton(name='Save layout', items=[('html', 'html'), ('png', 'png'), 
                                        ], width=150)

    # Extra plot type parameters # 
    profile_invert_axes = param.Boolean(True, label='Switch axes')
    profile_invert_yaxis = param.Boolean(True, label='Invert y axis')
    profile_logy = param.Boolean(False, label='Log y axis')

    # Polar plot parameters #
    # polar_projection = param.ObjectSelector(objects=['South', 'North'], default='South')
    polar_projection = pn.widgets.RadioButtonGroup(options=['South', 'North'])
    polar_central_longitude = param.Integer(default=100, step=1, label='Central Longitude', bounds=(-180, 180))
    polar_coastlines = param.Boolean(True, label='Polar plot coastlines')

    # 1d plot parameters # 
    plot_by = param.Boolean(label='Plot by time variable?')
    avg_by_lev = param.Boolean(True, label='Average by lev?')

    # file2 = None
    globallons = None
    globallats = None
    gif_dim_opts = []

    def react(self, *events):
        print(f"React to events ({len(events)}):")
        for event in events:
            print(f"\tTriggered by '{event.name}' now set to {event.new} (previously equal to {event.old})")

    def __init__(self, dataInput, file, model, **params):
        """
        Params class
            DataSource class as input, use the DataSource.dataInput and the DataSource.yaml_model as inputs 
            Open the file from datasource, either param.Selector, file path, Opendap object
            Once file is actually opened, get information needed to file parameter bounds, options, slider
            settings etc. Then pass the opened file and parameters to Dashboard class 
        """
        super().__init__(**params)  # run this to intialize all the parameter objects
        param.get_logger().setLevel(param.CRITICAL)
        self.dataInput = dataInput  # Rename these
        self.file = file
        self.model = model 

        self.set_file_selector()  # Run set file selector so that 'multi_file' the parameters gets added to this class
        self.meta_coords = params_util.load_model_coords()

        self._set_params()

    def _set_params(self):
        pass

    def set_file_selector(self):
        """
        If a data dorectpry is being used, set the 'multi_file' parameter.
        """
        if type(self.dataInput) == param.Selector:
            self.param._add_parameter('multi_file', self.dataInput)

    # @param.depends('multi_file')
    def set_input(self):
        """
        Set the 'input' filename.
        """
        if type(self.dataInput) == param.Selector:
            try:
                self.input = os.path.split(str(self.multi_file))[-1::][0]
            except:
                self.input = str(self.multi_file)
        else:
            try:
                self.input = os.path.split(str(self.dataInput))[-1::][0]
            except:
                self.input = str(self.dataInput)
        return self.input

    @param.depends('multi_file')
    def set_plot_types_on_var_change(self, file, field, xc, yc, tc, zc):
        """
        If the selected field changes or the file selected is changed, check and set what plot types are 
        available using the data and dimensions available. 

        Sets:
                plot_types.options (list): List of all possible plots
                plot_types.value (list): Default set of possible plots.
        """
        plot_types, default_plots = self.get_avail_plot_types(file[field], 
                                                                    #  self.data2d, 
                                                                     xc, yc,
                                                                     tc, zc)
        self.set_avail_plot_types(plot_types, default_plots, self.plot_type.value)

    def set_dim_params(self, model, xc, yc, tc, zc):
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

        # elif model == 'omi-toco':
        #     xc = meta_coords['xc']['omi']
        #     yc = meta_coords['yc']['omi']
        #     tc = meta_coords['tc']['omi']

        elif model in ['omi', 'mopitt', 'omi-toco']:
            xc = 'lon'
            yc = 'lat'
            tc = 'time'

        elif model == 'airnow': 
            xc = meta_coords['xc']['airnow']
            yc = meta_coords['yc']['airnow']
        
        elif model == 'wrf':
            xc = meta_coords['xc']['wrf']['coords'].split(",")[0]
            yc = meta_coords['yc']['wrf']['coords'].split(",")[0]
            tc = meta_coords['tc']['wrf']['dim']
            zc = meta_coords['zc']['wrf']['dim'].split(",")[0]
            # xc = 'lon'
            # yc = 'lat'
            # zc = 'lev'
            xc = 'west_east'
            yc = 'south_north'

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


        elif model is None:
            print(' Please enter in full, case-sensitive, which coordinate to use for x and y axis ')
            print(' Available coords: ')
            print(self.coords)
            x_user_input = input(" X coordinate: ")
            y_user_input = input(" Y coordinate: ")
            if len(self.coords) > 2:
                time_user_input = input(" Time coorinate: ")
                tc = time_user_input
            if len(self.coords) > 3:
                z_user_input = input(" Z Coordinate (enter 'None' if None): ")
                zc = z_user_input
                z_user_input = z_user_input.lower() 

            xc = x_user_input
            yc = y_user_input

        return xc, yc, tc, zc 
