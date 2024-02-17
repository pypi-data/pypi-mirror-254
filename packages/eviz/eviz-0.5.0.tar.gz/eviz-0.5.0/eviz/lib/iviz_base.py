import logging
import os
import sys

import holoviews as hv
import param
import panel as pn
import yaml
import glob
import cartopy

from bokeh.models import Button
from platform import node

from eviz.models.iviz.wrf_dashboard import WrfDash
from eviz.models.iviz.lis_dashboard import LisDash
from eviz.models.iviz.base_dashboard import BaseDash
from eviz.models.iviz.cf_dashboard import CfDash
from eviz.models.iviz.airnow_dashboard import AirNowDash
from eviz.models.iviz.tabular_dashboard import TabularDash
from eviz.lib.iviz.config import configIviz
from eviz.lib.data.data_selector import DataSelector
from eviz.lib.iviz.params import DatasetParams
from eviz.lib.iviz.dataframe_params import DataframeParams

import eviz.lib.const as constants
import eviz.lib.utils as u

pn.config.css_files = ['eviz/lib/templates/template.css']


class Iviz(param.Parameterized):
    """ The Iviz class processes inputs to the tool and initializes necessary classes.

    Parameters:
        session_file (str) : Name of session file (default is None)
    """
    pn.extension(css_files=['eviz/lib/templates/template.css'])
    pn.config.css_files = ['eviz/lib/templates/template.css']
    hv.extension('bokeh', logo=False)
    spacer = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=20, width=500)
    spacer_large = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=60, width=150)
    spacer_long = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=150, width=500)
    small_spacer = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=13, width=150)
    thin_spacer = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=100, width=50)

    exp_name = None
    comparison_name = None
    output_dir = None
    dataInput = None
    file_list = None
    model = None
    config_dir = None
    custom_config = False
    is_url = False

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # iViz internal state
        self.config_dir = constants.config_path

        if ('borg' or 'discover') in node():
            cartopy.config['data_dir'] = constants.CARTOPY_DATA_DIR

    def input_not_found(self):
        print("Input path or link not found. Please confirm path exists and is formatted correctly.")
        sys.exit()

    def set_input(self, inp, model, dtype):
        """
        Determine what kind of input has been provided either from the CLI or notebook.

        Parameters:
                inp (str): input file or dir
                model (str): a model type 
                dtype (str): data type 

        Returns:
                self.dataInput : either a param.Selector with files provided
                or a single Xarray file.
        """
        if inp is None and model is not None:
            model_exists = True
            input_exists = False
        elif inp is not None and model is None:
            model_exists = False
            input_exists = True
        elif inp is not None and model is not None:
            model_exists = True
            input_exists = True

        print()

        if model_exists and input_exists:
            if model == 'ccm':
                self.model = 'ccm'
                dtype = 'netcdf'

            elif model == 'cf':
                self.model = 'cf'
                dtype = 'netcdf'

            elif model == 'wrf':
                self.model = 'wrf'
                dtype = 'netcdf'

            elif model == 'lis':
                self.model = 'lis'
                dtype = 'netcdf'

            elif model == 'airnow':
                self.model = 'airnow'
                dtype = 'tabular'

            elif model in ['omi-toco']: 
                self.model = model
                dtype = 'hdf'

            elif model in ['omi', 'mopitt-toco']: 
                self.model = model
                # dtype = 'netcdf' 

            elif model == 'landsat':
                self.model = 'base'
                dtype = 'hdf'

            if os.path.isfile(inp):  # if given a file path
                self.dataInput = inp
                self.is_yaml = False
                filename = inp
                file_dict = {'files': inp}
                self.file_config = configIviz(**file_dict)
    
            elif os.path.isdir(inp):
                files = glob.glob(inp + '/*.nc*')
                filename = files[0]
                self.dataInput = param.Selector(objects=files, default=files[0])
                self.param._add_parameter('multi_file', self.dataInput)
                file_dict = {'files': files[0]}
                self.file_config = configIviz(**file_dict)

            elif inp.startswith('http'):
                self.dataInput = inp
                self.is_yaml = False
                filename = inp
                file_dict = {'files': inp}
                self.file_config = configIviz(**file_dict)
                self.is_url = True
            else:
                self.input_not_found()

        elif model_exists and not input_exists:
            if model == 'ccm':
                yaml_path = os.path.join(self.config_dir,'ccm/ccm.yaml')
                specs_path = os.path.join(self.config_dir,'ccm/ccm_specs.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'ccm'
                dtype = 'netcdf'

            elif model == 'cf':
                yaml_path = os.path.join(self.config_dir,'cf/cf.yaml')
                specs_path = os.path.join(self.config_dir,'cf/cf_specs.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'cf'
                dtype = 'netcdf'

            elif model == 'wrf':
                yaml_path = os.path.join(self.config_dir,'wrf/wrf.yaml')
                specs_path = os.path.join(self.config_dir,'wrf/wrf_specs.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'wrf'
                dtype = 'netcdf'

            elif model == 'lis':
                yaml_path = os.path.join(self.config_dir,'lis/lis.yaml')
                specs_path = os.path.join(self.config_dir,'lis/lis_specs.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'lis'
                dtype = 'netcdf'

            elif model == 'airnow':
                yaml_path = os.path.join(self.config_dir,'airnow/airnow.yaml')
                specs_path = os.path.join(self.config_dir,'airnow/airnow.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'airnow'
                dtype = 'tabular'

            elif model in ['omi-toco', 'omi']:
                yaml_path = os.path.join(self.config_dir,'omi/omi.yaml')
                specs_path = os.path.join(self.config_dir,'omi/omi.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = model
                # dtype = 'hdf' if model == 'omi-toco' else 'netcdf'

            elif model == 'landsat':
                yaml_path = os.path.join(self.config_dir,'landsat/landsat.yaml')
                specs_path = os.path.join(self.config_dir,'landsat/landsat.yaml')
                config_info = self.load(yaml_path, specs_path)
                self.set_config_info(config_info)
                filename = self.file_list[0]
                self.model = 'landsat'
                dtype = 'hdf'

        elif input_exists and not model_exists:
            if os.path.isfile(inp):  # if given a file path
                self.dataInput = inp
                self.is_yaml = False
                filename = inp
                self.model = None
                file_dict = {'files': inp}
                self.file_config = configIviz(**file_dict)
    
            elif os.path.isdir(inp):
                self.is_yaml = False
                files = glob.glob(inp + '/*.nc*')
                filename = files[0]
                self.dataInput = param.Selector(objects=files, default=files[0])
                self.param._add_parameter('multi_file', self.dataInput)
                self.model = None
                file_dict = {'files': files[0]}
                self.file_config = configIviz(**file_dict)

            elif inp.startswith('http'):
                self.dataInput = inp
                self.is_yaml = False
                filename = inp
                file_dict = {'files': inp}
                self.file_config = configIviz(**file_dict)
                self.is_url = True
            else:
                self.input_not_found()

        ds = DataSelector(filename, self.model, is_url=self.is_url, dtype=dtype)
        self.file = ds.data
        self.model = ds.model
        self.dtype = ds.dtype

        return self.dataInput  # so dataInput is either the file or the selector depending on if there are multiple files.

    def load(self, yaml_path, specs_path=None):
        """Load the corresponding yaml configuration and model specs file.

        Returns:
                cfg (dict): tool configuration info
                specs (dict): field specs
        """
        cfg = u.load_yaml(yaml_path)
        specs = u.load_yaml(specs_path)
        return cfg, specs

    def get_list(self, d):
        return [*d]

    def load_session(self, session_file=None):
        """ If a session file is provided by the user at startup, load the yaml file.

        Parameters:
                session_file (yaml): a yaml dict file with parameter settings
                and widget values from an iViz session.

        Returns:
                session (dict) : dictionary with tool param names and values
        """
        if session_file is not None:
            with open(session_file[0]) as f:
                session = yaml.load(f, Loader=yaml.FullLoader)
        else:
            session = None
        return session

    def load_options(self, plot_options_file=None):
        """ If plot settings are provided by the user at startup, load plot options file.

        Parameters:
                plot_options_file (yaml): a yaml dict file with plot settings.

        Returns:
                plot_options (dict) : dictionary with plot settings
        """
        if plot_options_file is not None:
            with open(plot_options_file[0]) as f:
                plot_options = yaml.load(f, Loader=yaml.FullLoader)
        else:
            plot_options = None
        return plot_options

    def set_config_info(self, config):
        """Use a configuration file to set all needed class variables.

        Parameters:
            config (list): the loaded config and specs dictionaries.

        Returns:
            self.file_config (dict) : all config info needed
        """
        cfg = config[0]
        specs = config[1]  # Could be None if not given a specs file

        self.app_data = cfg
        self.specs_data = specs
        self.file_list = []
        self.file_dict = {}
        config_dict = {}

        if 'inputs' in self.app_data:
            self.inputs = self.app_data['inputs']

            # ==================================== TO DO ========================================
            #   I should have this section just check for name and location and combine them
            #   with os.path.join if both are present. If only location, just a
            #   dir->param.ObjectSelector, if only name, then just don't need to do a join.
            # ===================================================================================

            if 'name' in self.app_data['inputs'][0] and 'location' in self.app_data['inputs'][0]:
                n_files = len(self.app_data['inputs'])
                for i in range(n_files):
                    if 'location' in self.app_data['inputs'][i]:
                        filename = os.path.join(self.app_data['inputs'][i]['location'],
                                                self.app_data['inputs'][i]['name'])
                    else:
                        filename = os.path.join('/', self.app_data['inputs'][i]['name'])
                    self.file_list.append(filename)
                n_files = len(self.file_list)
                for i in range(n_files):
                    n = str(self.file_list[i])
                    self.file_dict[n] = self.inputs[i]
                self.file_dict['file_dict'] = self.file_dict

            elif 'name' not in self.app_data['inputs'][0] and 'location' in self.app_data['inputs'][0]:
                file_dir = self.app_data['inputs'][0]['location']
                self.file_dict['location'] = file_dir
                self.file_dict['file_dict'] = self.app_data['inputs']
                # if 'exp_name' in self.app_data['inputs'][0]:
                # self.file_dict['exp_name'] = self.app_data['inputs'][0]['exp_name']
                self.file_list = file_dir
                self.file_dict['file_dict'] = self.file_dict

            elif 'name' in self.app_data['inputs'][0] and 'location' not in self.app_data['inputs'][0]:
                n_files = len(self.app_data['inputs'])
                for i in range(n_files):
                    self.file_list.append(self.app_data['inputs'][i]['name'])

                for i in range(n_files):
                    n = str(self.file_list[i])
                    self.file_dict[n] = self.inputs[i]
                    if 'exp_name' in self.file_dict[n]:
                        self.file_dict[n]['exp_name'] = self.inputs[i]['exp_name']
                    self.file_dict['file_dict'] = self.file_dict

            config_dict['file_dict'] = self.file_dict
            config_dict['file_list'] = self.file_list
            config_dict['is_yaml'] = True
            config_dict['specs_data'] = specs
            config_dict['filename'] = self.file_list[0]
            config_dict['app_data'] = self.app_data

            file_config = configIviz(**config_dict)
        else:
            print("Please provide an input")
            sys.exit()

        self.set_yaml_dataInput(self.file_list)  # running this sets self.dataInput
        self.file_config = file_config

    def set_yaml_dataInput(self, input_file):
        """ Set the class variable self.dataInput if yaml being used. 
        
        Note:
            Can be dir, filepath, list of files, or dict of files.

        Parameters:
                input_file (): dir, filepath, list, or dict

        Returns:
                self.dataInput () : either a param.Selector with files provided
                or str of single file.
        """
        if input_file is None:
            files = glob.glob(os.getcwd() + '/*.nc*')
            self.dataInput = param.Selector(objects=files, default=files[0])
            self.param._add_parameter('multi_file', self.dataInput)
            self.yaml_files = True
        elif os.path.isdir(str(input_file)):
            files = glob.glob(input_file + '*.nc*')
            self.dataInput = param.Selector(objects=files, default=files[0])
            self.param._add_parameter('multi_file', self.dataInput)
        elif os.path.isfile(str(input_file)):
            self.dataInput = str(input_file)
        elif isinstance(input_file, list):
            if len(input_file) == 1:
                self.dataInput = str(input_file[0])
                # self.files = None
            else:
                self.dataInput = param.Selector(objects=input_file, default=input_file[0])
                self.param._add_parameter('multi_file', self.dataInput)
                self.yaml_files = True
        elif isinstance(input_file, dict):
            input_file = list(input_file.keys())
            self.dataInput = param.Selector(objects=input_file, default=input_file[0])
            self.param._add_parameter('multi_file', self.dataInput)
            self.yaml_files = True

        self.params.dataInput = self.dataInput
        return self.dataInput

    def get_dash(self):
        """ Determine the corresponding dashboard to use based on determined model type.

        Parameters:
            self.model (str): model type

        Returns:
            dash (cls) : corresponding model dashboard, generic if none
        """
        if self.model == 'wrf':
            dash = WrfDash
        elif self.model == 'lis':
            dash = LisDash
        elif self.model == 'airnow':
            dash = AirNowDash
        elif self.model == 'tabular':
            dash = TabularDash
        elif self.model in ['ccm', 'ccm3d', 'geos', 'base', 'omi-toco', 'omi',
                            'mopitt-toco', None]:
            dash = BaseDash
        elif self.model == 'cf':
            dash = CfDash
        return dash

    def view(self):
        """
        Arrange all the final objects from dashboard and parameters classes to create final plot and
        widget layout.

        Returns:
            row (pn.Row) : final panel Row object with plot and widgets for dashboard.
        """
        file2params = pn.Param(self.params.param, parameters=['comparison_field', 'z2', 't2'],
                               widgets={
                                   'z2': {'type': pn.widgets.IntSlider},
                                   't2': {'type': pn.widgets.IntSlider}}, width=160, show_name=False)
        main_params = pn.Param(self.params.param, parameters=['multi_file', 'field', 'z', 't', 'xc', 'yc',
                                                    'cmap'],
                               max_width=500,
                               min_width=100, width_policy='max', show_name=False,
                               widgets={
                                   'z': {'type': pn.widgets.IntSlider},
                                   't': {'type': pn.widgets.IntSlider}, 
                                   })
        main_params2 = pn.Param(self.params.param, parameters=['field', 'z', 't', 'xc', 'yc', 'cmap', 
                                ], 
                                max_width=500,
                                min_width=100, width_policy='max', show_name=False,
                                widgets={
                                    'z': {'type': pn.widgets.IntSlider},
                                    't': {'type': pn.widgets.IntSlider},
                                    })
        
        column_params = pn.Param(self.dash.params.param, parameters=['show_statistics', 'show_data', 'add_histo'],
                                 max_width=350, min_width=100, width_policy='max', show_name=False)
        tabs_toggle = pn.Param(self.dash.params.param, parameters=['tabs_switch'], widgets={
            'tabs_switch': {'type': pn.widgets.Toggle, 'width': 150}},
                               width=150, margin=0, show_name=False)
        tool_options_panel = pn.Row(self.thin_spacer, pn.Column(tabs_toggle,
                                                                self.dash.params.add_to_tabs_btn,
                                                                self.dash.params.animate_toggle,
                                                                self.dash.animate,
                                                                self.dash.params.progressbar,
                                                                self.spacer_large),
                                    pn.Column(
                                        self.dash.params.save_menu_button,
                                        column_params),
                                    )


        if type(self.dataInput) == param.Selector:
            params_column = pn.Column(main_params, self.spacer_large, tool_options_panel,
                                      self.dash.params.differencing_toggle, 
                                      self.dash.params.explore_files, 
                                      self.dash.do_diff, 
                                      self.dash.do_explorer,
                                      )
        else:
            params_column = pn.Column(main_params2, self.spacer_large, tool_options_panel,
                                      self.dash.params.differencing_toggle, 
                                      self.dash.params.explore_files, 
                                      self.dash.do_diff, 
                                      self.dash.do_explorer,
                                      )

        widget_column = pn.WidgetBox(
            self.spacer,
            pn.Column(params_column, file2params),
            self.dash.plot_opts,
            self.dash.plot_second,
            self.dash.clear_second,
            self.dash.add_to_tabs,
            self.dash.save_layout,
            self.dash.plot_difference,
            self.dash.clear_diff,
            self.dash.save_session,
            self.dash.save_plot_opts,
            self.spacer_long,
            max_height=1400,
            width=550,
        )

        plot_column = self.dash.column  # the actual plots that are produced in dashboard
        row = pn.Row(widget_column, plot_column, self.dash.notyf, width=700) 

        return row

    def set_panel_widgets(self, vals):
        """
        If a session file or plot options file is input by user, this function
        sets all the panel based widgets manually.

        Parameters:
            vals (dict): all the session and plot options values.

        """
        self.Params.invert_yaxis_z = vals['invert_yaxis_z']
        self.Params.invert_xaxis_z = vals['invert_xaxis_z']
        self.Params.invert_yaxis = vals['invert_yaxis']
        self.Params.invert_xaxis = vals['invert_xaxis']
        self.Params.alpha = vals['alpha']
        self.Params.differencing_toggle = vals['differencing_toggle']
        self.Params.animate_toggle = vals['animate_toggle']
        self.Params.second_file_input = vals['second_file_input']
        self.Params.title_input = vals['title_input']
        self.Params.operations = vals['operations']
        self.Params.color_levels = vals['color_levels']

        self.Params.yz_ylim = (vals['yz_ylim.value.1'],
                                     vals['yz_ylim.value.2'])
        self.Params.yz_xlim = (vals['yz_xlim.value.1'],
                                     vals['yz_xlim.value.2'])
        self.Params.xy_ylim = (vals['xy_ylim.value.1'], vals['xy_ylim.value.2'])
        self.Params.xy_xlim = (vals['xy_xlim.value.1'], vals['xy_xlim.value.2'])

        if 'plot_second_file_button.clicks' in vals:
            self.Params.plot_second_file_button.clicks = vals['plot_second_file_button.clicks']
        if 'clear_button.clicks' in vals:
            self.Params.clear_button.clicks = vals['clear_button.clicks']
        if 'difference_button.clicks' in vals:
            self.Params.difference_button.clicks = vals['difference_button.clicks']
        if 'clear_diff_button.clicks' in vals:
            self.Params.clear_diff_button.clicks = vals['clear_diff_button.clicks']
        if 'apply_operation_button.clicks' in vals:
            # TODO: This has no effect. Fix?
            self.Params.apply_operation_button.clicks
        if 'zoom_plot_button.clicks' in vals:
            self.Params.zoom_plot_button.clicks = vals['zoom_plot_button.clicks']
        if 'add_time_series_plot_btn.clicks' in vals:
            self.Params.add_time_series_plot_btn.clicks = vals['add_time_series_plot_btn.clicks']
        if 'add_plots_button.clicks' in vals:
            self.Params.add_plots_button.clicks = vals['add_plots_button.clicks']
        if 'enable_projection.clicks' in vals:
            self.Params.enable_projection.clicks = vals['enable_projection.clicks']
        if 'add_plots_button.clicks' in vals:
            self.Params.add_to_tabs_btn.clicks = vals['add_to_tabs_btn.clicks']

        # ADD PARAMS PANEL WIDGETS
        self.Params.plot_type.value = vals['plot_type.value']
        self.Params.plot_kind.value = vals['plot_kind.value']
        self.Params.yz_ylim = (vals['yz_ylim.value.1'],
                                     vals['yz_ylim.value.2'])
        self.Params.yz_xlim = (vals['yz_xlim.value.1'],
                                     vals['yz_xlim.value.2'])
        self.Params.xy_xlim = (vals['xy_xlim.value.1'], vals['xy_xlim.value.2'])
        self.Params.xy_ylim = (vals['xy_ylim.value.1'], vals['xy_ylim.value.2'])
        self.Params.xy_ylim2 = (vals['xy_ylim2.value.1'], vals['xy_ylim2.value.2'])
        # if 'save_menu_button.clicked' in vals:
        # self.Params.save_menu_button.clicked = vals['save_menu_button.clicked']

    def get_params_class(self, dtype):
        if dtype == 'tabular' or dtype == 'airnow':
            params = DataframeParams
        else:
            params = DatasetParams
        return params

    def make_params(self, session_file=None, plot_options_file=None):
        """ Run necessary functions and initialize Params class values.

        Parameters:
                session_file (str): optional iViz session file to restore
                plot_options (str): optional plot options file to apply.

        Returns:
                self.Params (cls) : initialized Params class
        """
        params = self.get_params_class(self.dtype)

        if plot_options_file is not None:
            plot_options = self.load_options(plot_options_file)
            self.Params = params(self.dataInput, self.file, self.model, **plot_options)
        elif session_file is not None:
            session_file = self.load_session(session_file)
            self.Params = params(self.dataInput, self.file, self.model, **session_file)
            self.set_panel_widgets(session_file)
        else:
            self.Params = params(self.dataInput, self.file, self.model)

        return self.Params

    def make_template(self):
        """
        After initializing all needed classes and arranging plots and widgets in one panel
        Row, create the Panel template for content to be embedded in. Serve the tool on
        a randomly generated localhost address, automatically opens, using pn.serve().

        """
        # Panel widgets needed for template modal and header
        self.dash.params.save_session_button.visible = True
        self.dash.params.save_plot_opts_button.visible = True
        nccs_link = pn.pane.HTML('<a href="https://www.nccs.nasa.gov">NASA Center for Climate Simulations</a>',
                                 style={'color': '#FFFFFF', 'font-size': '16px', 'text-decoration': 'none'})
        repo_link = pn.pane.HTML('<a href="https://git.mysmce.com/astg/visualization/eviz.mai">Gitlab</a>',
                                 style={'color': '#FFFFFF', 'font-size': '16px', 'text-decoration': 'none'})
        logout = Button(label="Logout", width=115, margin=0, align='center')
        modal_btn = pn.widgets.Button(name='Open File Explorer', width=125, margin=0, align='center')
        # logout.js_on_click(CustomJS(code="  window.location.href='%s'" % curdoc().session_context.logout_url))
        smaller_spacer = pn.Row(pn.Spacer(sizing_mode='stretch_both'), height=13, width=25)  # , background='#96DED1')

        # Assemble for template
        header = pn.Row(pn.Row(nccs_link, repo_link, align='center'), smaller_spacer, modal_btn, smaller_spacer,
                        self.dash.params.save_session_button, smaller_spacer, self.dash.params.save_plot_opts_button,
                        smaller_spacer, align='center')  # vis.astg_logo, vis.nasa_meatball,

        modal = pn.Column(self.dash.params.multi_selector, self.dash.params.add_files_button, self.dash.add_files,
                          self.dash.params.run_time_avg_btn, pn.Row(self.dash.params.param.all_variables,
                                                                    self.dash.params.variable_input),
                          self.dash.params.add_time_series_plot_btn,
                          # align='center',
                          width=800)

        # Create Panel template
        # def create_template():
        template = pn.template.BootstrapTemplate(title='',
                                                 logo='docs/static/iviz_logo.png',
                                                 modal=[modal],
                                                 header=[header],
                                                 header_background='#0A1832',
                                                 header_color='#FFFFFF',  # header_color is the text color of the header
                                                 sidebar_width=530,
                                                 favicon="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/200px-NASA_logo.svg.png",
                                                 )

        # Define template modal event to open when modal button is clicked
        def open_mod(e):
            template.open_modal()

        modal_btn.on_click(open_mod)
        app = self.view()
        top = app[0][1]
        bottom = app[0][2]
        plots = app[1]
        notyf = app[2]
        side = pn.WidgetBox(top, bottom, background='#1B345C', width=500)
        template.main.append(plots)
        template.main.append(notyf)
        template.sidebar.append(side)

        # pn.serve(template)
        return template

    def set_iviz(self, i=None, s=None, d=None, se=None, p=None):
        """ Initializes all classes and sets them to class variables, includes
        self.params, and self.dash. 
        
        Runs all needed functions to create app template and serve the app. 
        Auto runs pn.serve to launch app in web browser tab.

        Parameters:
                session_file (str): optional iViz session file to restore
                plot_options (str): optional plot options file to apply.

        Returns:
                template (pn.template.BootstrapTemplate) : final app
        """
        self.set_input(i, s, d)
        self.params = self.make_params(se, p)
        dash = self.get_dash()
        self.dash = dash(self.file_config, self.params)

    def make_app(self, i=None, s=None, d=None, se=None, p=None):
        """ Initializes all classes and sets them to class variables, includes
        self.params, and self.dash. 
        
        Runs all needed functions to create app template and serve the app. 
        Auto runs pn.serve to launch app in web browser tab.

        Parameters:
                session_file (str): optional iViz session file to restore
                plot_options (str): optional plot options file to apply.

        Returns:
                template (pn.template.BootstrapTemplate) : final app
        """
        self.set_iviz(i, s, d, se, p)
        template = self.make_template()
        pn.extension(css_files=['eviz/lib/templates/template.css'])
        pn.config.css_files = ['eviz/lib/templates/template.css']

        pn.serve(template)

    def make_notebook(self, i=None, s=None, d=None, se=None, p=None):
        """ Initializes all classes and sets them to class variables, includes
        self.params, and self.dash. 
        
        Runs all needed functions to create the app without the panel web template. 
        For use in the JupyterNotebook.

        Parameters:
            session_file (str): optional iViz session file to restore
            plot_options (str): optional plot options file to apply.

        Returns:
            app (pn.Row) : returns final tool as pn.Row instead of template.
        """
        self.set_iviz(i, s, d, se, p)
        # self.dash.notebook_widgets()
        pn.config.css_files = ['eviz/lib/templates/template.css']
        pn.extension(css_files=['eviz/lib/templates/template.css'])
        app = self.view()
        return app

    def make_panel(self, inp=None, source=None, dtype=None, session_file=None, plot_options=None):
        """
        Initializes all classes and sets them to class variables, includes
        self.params, and self.dash. Runs all needed functions to create app
        template and returns the .servable app. Returns template without
        starting panel server automatically. Best for use with 'Render
        with Panel' button in notebook. Run function, add .servable,
        press green 'Render with Panel' button from JupyterLab/Hub
        toolbar.

        Parameters:
                inp (str): tool input, source config or file, or dir path
                session_file (str): optional iViz session file to restore
                plot_options (str): optional plot options file to apply.

        Returns:
                template (pn.template.BootstrapTemplate) : final app
        """
        self.set_iviz(inp, source, dtype, session_file, plot_options)
        template = self.make_template()
        pn.extension(css_files=['eviz/lib/templates/template.css'])
        pn.config.css_files = ['eviz/lib/templates/template.css']

        return template

