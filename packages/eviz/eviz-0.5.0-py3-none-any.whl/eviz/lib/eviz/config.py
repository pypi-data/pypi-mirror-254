import logging
import os
import sys
from dataclasses import dataclass, field
from typing import List, Dict, Any
import matplotlib as mpl
import yaml
from matplotlib import pyplot as plt

import eviz.lib.utils as u
from eviz.lib import const as constants
from eviz.lib.data.netcdf4_reader import NetCDFDataReader
from eviz.lib.data.hdf5_reader import HDF5DataReader
from eviz.lib.data.hdf4_reader import HDF4DataReader
from eviz.lib.data.tabular_reader import CSVDataReader
from eviz.lib.eviz.geos.geos_history import parse_history, get_collection_with_field

FILE_EXTENSIONS = (
    'nc',
    'nc4',
    'hdf',
    'hdf4',
    'h5',
    'hdf5',
    'csv',
    'dat',
    'grib',
    'grib2',
)

rc_matplotlib = mpl.rcParams  # PEP8 4 lyfe


@dataclass
class Config:
    """ This class defines attributes and methods for managing user-defined configurations necessary to create plots.

    The configurations are defined in YAML files. There are some default configurations that work quite well
    as starting points. These are found under config/ and include templates for GEOS, WRF and LIS models (among
    others). Once YAML files are parsed, their contents are stored in dict structures which are all part of
    the Config object.

    Parameters:
        source_names (list) : The names of the `supported` sources.
        config_files  (list) : A list of YAML files associated with the sources.

    Notable Attributes:
        app_data (dict) : a dictionary that holds the contents of the APP YAML file
        spec_data (dict) : a dictionary that holds the contents of the SPEC YAML file

    Note:
        Every other Config attribute is a subset of app_data ad spec_data.

    """
    source_names: list[str]
    config_files: list[str]
    # Class attributes
    app_data: Dict[str, Any] = field(default_factory=dict)
    spec_data: Dict[str, Any] = field(default_factory=dict)
    history_data: Dict[str, Any] = field(default_factory=dict)
    # inputs: list = field(default_factory=list)
    meta_attrs: dict = field(default_factory=dict)
    meta_coords: dict = field(default_factory=dict)
    readers: dict = field(default_factory=dict)
    compare_fields: List[str] = None  # Add the compare fields attribute
    ds_index: int = 0
    # YAML defaults
    # -- inputs --
    _to_plot: dict = field(default_factory=dict)
    _file_list: dict = field(default_factory=dict)
    _trop_height_file_list: dict = field(default_factory=dict)
    _sphum_conv_file_list: dict = field(default_factory=dict)
    _exp_name: str = None
    _description: str = None
    # -- for_inputs --
    # compare defaults
    _compare_exp_ids: list = field(default_factory=list)
    _extra_diff_plot: bool = False
    _compare: bool = False
    _comp_panels: tuple = field(default_factory=tuple)
    _cmap: str = 'rainbow'
    _profile: bool = False
    _use_trop_height: bool = False
    _use_sphum_conv: bool = False
    # _yaml_path: str = None
    _specs_yaml_exists: bool = True
    _use_cartopy: bool = True
    # -- outputs --
    _add_logo: bool = False
    _print_to_file: bool = False
    _print_format: str = 'png'
    _make_pdf: bool = False
    _print_basic_stats: bool = False
    _mpl_style: str = 'classic'
    _output_dir: str = None
    # -- history (GEOS only) --
    _use_history: bool = False
    _history_expid: str = None
    _history_expdsc: str = None
    _history_dir: str = None
    _history_collection: str = None
    _history_year: str = None
    _history_month: str = None
    _history_season: str = None
    _history_to_plot: dict = field(default_factory=dict)
    # --system options --
    _use_mp_pool: bool = False
    _archive_web_results: bool = False
    _collection: str = None
    # Figure options
    ax_opts: dict = field(default_factory=dict)
    _map_params: dict = field(default_factory=dict)
    _subplot_specs: tuple = field(default_factory=tuple)

    def __post_init__(self):
        self.logger.info("Start init")
        self.findex = 0
        self.ax_opts = {}
        self.spec_data = {}

        _concat = self._concatenate_yaml()
        self._init_file_list_to_plot()
        self._init_readers()
        self._init_for_inputs()
        self._init_outputs()
        self._init_map_params(_concat)
        self._init_system_opts()
        self._init_history()
        self.meta_coords = u.read_meta_coords()
        self.meta_attrs = u.read_meta_attrs()
        self._init_comparisons()

        self.get_default_plot_params()
        plt.style.use(self.mpl_style)

    def _concatenate_yaml(self):
        concat = []
        result = {}
        output_dirs = []

        _source_index = 0
        for file_path in self.config_files:
            self.ds_index = _source_index
            with open(file_path, 'r') as file:
                yaml_content = yaml.safe_load(file)
                yaml_content['source'] = self.source_names[_source_index]
                concat.append(yaml_content)
                if 'inputs' in yaml_content:
                    if 'inputs' not in result:
                        result['inputs'] = []
                    result['inputs'].extend(yaml_content['inputs'])
                else:
                    self.logger.error(f'No inputs are specified in {file_path}.')
                    sys.exit()

                # We can have a sources, like 'ccm', 'geos', 'generic', 'omi', 'airnow', etc.
                # The first 3 are 'nc4' readers, 'omi' is an 'omi' reader which can be 'nc4'
                # or 'h5', and 'airnow' is a 'csv' reader - reader here is a 'format'
                foo = self.get_source_from_name(self.source_names[_source_index])
                result[self.source_names[_source_index]] = foo
                if 'for_inputs' in yaml_content:
                    if 'for_inputs' not in result:
                        result['for_inputs'] = {}
                    result['for_inputs'].update(yaml_content['for_inputs'])

                if 'system_opts' in yaml_content:
                    if 'system_opts' not in result:
                        result['system_opts'] = {}
                    result['system_opts'].update(yaml_content['system_opts'])

                if 'outputs' in yaml_content:
                    if 'outputs' not in result:
                        result['outputs'] = yaml_content['outputs']
                    else:
                        # Concatenate values from 'outputs'
                        for key, value in yaml_content['outputs'].items():
                            if key not in result['outputs']:
                                result['outputs'][key] = value

                # Special case for GEOS sources
                # Can only apply history settings to GEOS sources
                if 'geos' in self.source_names and len(set(self.source_names)) == 1:
                    if 'history' in yaml_content:
                        if 'history' not in result:
                            result['history'] = {}
                        result['history'].update(yaml_content['history'])

                if 'outputs' in yaml_content and 'output_dir' in yaml_content['outputs']:
                    output_dirs.append(yaml_content['outputs']['output_dir'])

                # Load associated specs file if specified
                specs_file = os.path.join(os.path.dirname(file_path),
                                          f"{os.path.splitext(file_path)[0]}_specs.yaml")
                if os.path.exists(specs_file):
                    with open(specs_file, 'r') as specs_file:
                        try:
                            _specs = yaml.safe_load(specs_file)
                            if not _specs:
                                self.logger.error(f'Problems reading YAML file.')
                                sys.exit()
                            self.spec_data.update(_specs)
                        except FileNotFoundError:
                            self.logger.error(f'A model specifications YAML file was not found.')
                            self._specs_yaml_exists = False
                else:
                    self.logger.warning(f'A model specifications YAML file was not found.')
                    self._specs_yaml_exists = False
            _source_index += 1

        self.app_data = result
        return concat

    def _init_map_params(self, concat):
        _inputs = {}
        _maps = {}

        def process_input_dict(input_dict):
            current_inputs = input_dict.get('inputs', [])
            current_outputs = input_dict.get('outputs', [])
            # Assume compare_ids has only two elements!!!
            compare_ids = u.get_nested_key_value(self.app_data, ['for_inputs', 'compare', 'ids'])
            if compare_ids:
                # TODO: remove this restriction in the future
                if len(compare_ids) > 2:
                    compare_ids = compare_ids[0:2]

            self._outdirs = u.get_nested_key_value(self.app_data, ['outputs', 'output_dir'])
            compare_flag = False
            compare_dir = None
            if compare_ids:
                compare_flag = True
                compare_dir = os.path.join(os.path.dirname(self._outdirs), 'comparisons')

            for i, input_entry in enumerate(current_inputs):  # these can't be empty
                current_name = input_entry.get('name', '')
                current_to_plot = input_entry.get('to_plot', {})

                current_input_dict = {'inputs': {'name': current_name}, 'outputs': current_outputs}
                for field_name, field_values in current_to_plot.items():
                    current_input_dict[field_name] = field_values.split(',')
                _inputs[len(_inputs)] = current_input_dict

                filename = os.path.join(input_entry.get('location', ''), input_entry.get('name', ''))
                exp_name = input_entry.get('exp_name', '')
                exp_id = input_entry.get('exp_id', '')
                description = input_entry.get('description', '')
                ignore = input_entry.get('ignore', '')
                source_name = input_dict.get('source', '')
                source_reader = self.app_data[source_name]

                compare_with = []
                if compare_flag:
                    if exp_id in compare_ids:
                        current_outputs = compare_dir
                    compare_with = [element for element in compare_ids if element != exp_id][0]

                source_index = self.source_names.index(source_name)
                # If we want to_plot all variables, get list from dataset
                if 'all' in current_to_plot.keys():
                    data = self.readers[source_name].read_data(filename)
                    to_ignore = ignore.split(',')
                    for field_name in data['vars']:
                        ignore_field = any(ig in field_name for ig in to_ignore)
                        if ignore_field:
                            continue
                        field_values = current_to_plot['all']
                        field_specs = u.get_nested_key_value(self.spec_data, [field_name])
                        _maps[len(_maps)] = {'source_name': source_name,
                                             'source_reader': source_reader,
                                             'source_index': source_index,
                                             'field': field_name,
                                             'filename': filename,
                                             'file_index': i,
                                             'exp_name': exp_name,
                                             'exp_id': exp_id,
                                             'description': description,
                                             'ignore': to_ignore,
                                             'to_plot': field_values.split(','),
                                             'compare': compare_flag,
                                             'compare_with': compare_with,
                                             'outputs': current_outputs,
                                             'field_specs': field_specs}
                else:
                    for field_name, field_values in current_to_plot.items():
                        field_specs = u.get_nested_key_value(self.spec_data, [field_name])
                        _maps[len(_maps)] = {'source_name': source_name,
                                             'source_reader': source_reader,
                                             'source_index': source_index,
                                             'field': field_name,
                                             'filename': filename,
                                             'file_index': i,
                                             'exp_name': exp_name,
                                             'exp_id': exp_id,
                                             'description': description,
                                             'ignore': ignore.split(','),
                                             'to_plot': field_values.split(','),
                                             'compare': compare_flag,
                                             'compare_with': compare_with,
                                             'outputs': current_outputs,
                                             'field_specs': field_specs}

        for input_dict in concat:
            process_input_dict(input_dict)

        self._map_params = _maps

    def _init_comparisons(self):
        self.a_list = []
        self.b_list = []
        self.map_list = []

        for key, data in self.map_params.items():
            if data['compare']:
                compare_with_value = data['compare_with']
                if compare_with_value == self.compare_exp_ids[1]:
                    self.a_list.append(data)
                elif compare_with_value == self.compare_exp_ids[0]:
                    self.b_list.append(data)
            else:
                self.map_list.append(data)

    def _init_readers(self):
        """ Determine 'readers' needed from assumed data formats"""
        _data_types_needed = {}
        # Determine data type base on filename extension
        for i in range(len(self._file_list)):
            file_path = self._file_list[i]['filename']
            file_extension = os.path.splitext(file_path)[1]
            # Hacks for WRF and test (this latter is not a 'real' source)
            wrf_source = False
            test_source = False
            if 'wrf' in file_path:
                wrf_source = True
                _data_types_needed['NetCDF'] = True
            elif 'test' in file_path:
                test_source = True
                _data_types_needed['NetCDF'] = True
            else:
                if file_extension == '.nc' or file_extension == '.nc4':
                    _data_types_needed['NetCDF'] = True
                elif file_extension == '.csv' or file_extension == '.dat':
                    _data_types_needed['CSV'] = True
                elif file_extension == '.h5' or file_extension == '.he5':
                    _data_types_needed['HDF5'] = True
                elif file_extension == '.hdf':
                    _data_types_needed['HDF4'] = True

        # Set reader objects for each needed data type
        for s in self.source_names:  # a source may have multiple types!
            j = 0
            for reader, is_needed in _data_types_needed.items():
                if is_needed:
                    file_path = self._file_list[j]['filename']
                    file_extension = os.path.splitext(file_path)[1]
                    self.logger.info(f"Setup {reader} reader")
                    if wrf_source or test_source:
                        self.readers[s] = self._get_reader(s, '.nc')
                    else:
                        self.readers[s] = self._get_reader(s, file_extension)
                j += 1

    @staticmethod
    def _get_reader(source_name: str, file_extension: str) -> 'DataReader':
        if file_extension == ".csv" or file_extension == ".dat":
            return CSVDataReader(source_name)
        elif file_extension == ".hdf4" or file_extension == ".hdf":
            return HDF4DataReader(source_name)
        elif file_extension == ".hdf5" or file_extension == ".he5":
            return HDF5DataReader(source_name)
        elif file_extension == ".nc" or file_extension == ".nc4":
            return NetCDFDataReader(source_name)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")

    def _init_for_inputs(self) -> None:
        """ Initialize parameters in for_inputs section of the APP file.

        Note:
            The for_inputs parameters are settings used by inputs.

        """
        if 'for_inputs' in self.app_data:
            try:
                self._compare = self.app_data['for_inputs']['compare']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._compare = False
            if self._compare:
                try:
                    _exp_ids = self.app_data['for_inputs']['compare']['ids']
                    self._compare_exp_ids = _exp_ids.split(',')
                except KeyError as e:
                    self.logger.debug(f'key error {e}, using default')
                    self._compare_exp_ids = []
                    self._compare = False

            try:
                self._extra_diff_plot = self.app_data['for_inputs']['compare']['extra_diff']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._extra_diff_plot = False
            if self._extra_diff_plot:
                self._comp_panels = 2, 2
            else:
                self._comp_panels = 3, 1

            try:
                self._profile = self.app_data['for_inputs']['compare']['profile']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._profile = False
            try:
                self._cmap = self.app_data['for_inputs']['compare']['cmap']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._cmap = 'rainbow'

            try:
                self._use_trop_height = self.app_data['for_inputs']['trop_height']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._use_trop_height = False
            try:
                self._use_sphum_conv = self.app_data['for_inputs']['sphum_field']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._use_sphum_conv = False
            try:
                self._subplot_specs = self.app_data['for_inputs']['subplots']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._subplot_specs = (1, 1)

            # It is convenient to specify use of Cartopy at the app level
            if 'use_cartopy' in self.app_data['for_inputs']:
                self._use_cartopy = self.app_data['for_inputs']['use_cartopy']

    def _init_outputs(self) -> None:
        """ Initialize parameters in outputs section of the APP file.
        """
        if 'outputs' in self.app_data:
            try:
                self._add_logo = self.app_data['outputs']['add_logo']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._add_logo = False
            try:
                self._print_to_file = self.app_data['outputs']['print_to_file']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._print_to_file = False
            # self._set_output_dir()

            try:
                self._print_format = self.app_data['outputs']['print_format']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._print_format = 'png'
            try:
                self._make_pdf = self.app_data['outputs']['make_pdf']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._make_pdf = False
            try:
                self._print_basic_stats = self.app_data['outputs']['print_basic_stats']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._print_basic_stats = False
            try:
                self._mpl_style = self.app_data['outputs']['mpl_style']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._mpl_style = 'classic'
        # else:
        #     self._set_output_dir()
        # TODO: Add make_gif option

    def _init_system_opts(self) -> None:
        """ Initialize parameters in system_opts section of the APP file.
        """
        if 'system_opts' in self.app_data:
            try:
                self._use_mp_pool = self.app_data['system_opts']['use_mp_pool']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._use_mp_pool = False
            try:
                self._archive_web_results = self.app_data['system_opts']['archive_web_results']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._archive_web_results = False
            try:
                self._collection = self.app_data['system_opts']['collection']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
                self._collection = ''

    def _init_history(self) -> None:
        """ Initialize parameters in history section of the APP file.
        """
        if 'history' in self.app_data:
            try:
                self._use_history = self.app_data['history']['use_history']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_dir = self.app_data['history']['history_dir']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_collection = self.app_data['history']['history_collection']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_year = self.app_data['history']['history_year']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_month = self.app_data['history']['history_month']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_season = self.app_data['history']['history_season']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')
            try:
                self._history_to_plot = self.app_data['history']['history_to_plot']
            except KeyError as e:
                self.logger.debug(f'key error {e}, using default')

    def _set_output_dir(self) -> None:
        """ Initialize output_dir parameter with sensible defaults """
        if self.print_to_file:
            if not constants.output_path:
                out_dir = "./output_plots"
                # if 'outputs' in self.app_data and 'output_dir' in self.app_data['outputs']:
                #     out_dir = self.app_data['outputs']['output_dir']
                # else:
                #     self.logger.debug(f'Using default out_dir: {out_dir}')
            else:
                out_dir = constants.output_path
            if not os.path.exists(out_dir):
                self.logger.debug(f'making directory: {out_dir}')
                os.makedirs(out_dir)
            self._output_dir = out_dir
        else:
            self.logger.debug('Will display plots interactively')

    def _init_file_list_to_plot(self) -> None:
        """ Create the list of files that contain the data to be plotted.

        The list will be constructed with the entries specified in the inputs entry of the APP_YAML.
        """
        if self._use_history:
            if not self._history_year or not self._history_month:
                self.logger.error(
                    "YOU NEED TO PROVIDE THE year OR/AND THE month")
                self.logger.error(f"\t Edit the config file and try again.")
                sys.exit()
            return None  # TODO: self.make_dict(self.hist_list_files())
        else:
            self._get_file_list()
            # Reset self.compare, just in case
            if len(self._file_list) == 1:
                self.compare = False

        # The following was tailored for GEOS output, so it may lack generality
        self._set_trop_height_file_list()
        self._set_sphum_conv_file_list()

    def _get_file_list(self):
        """ Get all specified input files from the top level "app" YAML file """
        if 'inputs' in self.app_data:
            n_files = len(self.app_data['inputs'])
            self.logger.debug(f'Looping over {n_files} file entries:')
            for i in range(n_files):
                if 'location' in self.app_data['inputs'][i]:
                    filename = os.path.join(self.app_data['inputs'][i]['location'],
                                            self.app_data['inputs'][i]['name'])
                else:
                    filename = os.path.join(self.app_data['inputs'][i]['name'])
                self._file_list[i] = self.app_data['inputs'][i]
                self._file_list[i]['filename'] = filename
                # self.ds_index = i

                self.logger.debug(f"file_list[{i}] = {self._file_list[i]}")
        else:
            self.logger.error(f"The 'inputs' entry does not specify any files (name+location).")
            sys.exit()

    # TODO: trop_height and sph_conv files are GEOS-specific
    # Therefore, GEOS-specific functionality should be moved to a ConfigGeos class
    def _set_trop_height_file_list(self):
        """ Get all specified tropopause height files from the top level "app" YAML file """
        if self._use_trop_height:
            if 'trop_height' in self.app_data['for_inputs']:
                n_files = len(self.app_data['for_inputs']['trop_height'])
                self.logger.debug(f'Looping over {n_files} trop_height file entries:')
                for i in range(n_files):
                    if 'location' in self.app_data['for_inputs']['trop_height'][i]:
                        filename = os.path.join(self.app_data['for_inputs']['trop_height'][i]['location'],
                                                self.app_data['for_inputs']['trop_height'][i]['name'])
                    else:
                        filename = os.path.join('/', self.app_data['for_inputs']['trop_height'][i]['name'])
                    self._trop_height_file_list[i] = self.app_data['for_inputs']['trop_height'][i]
                    self._trop_height_file_list[i]['filename'] = filename
                    self._trop_height_file_list[i]['exp_name'] = \
                        self.app_data['for_inputs']['trop_height'][i]['exp_name']
                    self._trop_height_file_list[i]['trop_field_name'] = \
                        self.app_data['for_inputs']['trop_height'][i]['trop_field_name']
                    self.logger.debug(self.trop_height_file_list[i])
            else:
                self.logger.warning(f"The 'for_inputs' entry does not specify trop-height-containing files.")
                self._use_trop_height = False

    def _set_sphum_conv_file_list(self):
        """ Get all specified specific humidity files from the top level "app" YAML file """
        if self._use_sphum_conv:
            if 'sphum_field' in self.app_data['for_inputs']:
                n_files = len(self.app_data['for_inputs']['sphum_field'])
                self.logger.debug(f'Looping over {n_files} sphum_field file entries:')
                for i in range(n_files):
                    if 'location' in self.app_data['for_inputs']['sphum_field'][i]:
                        filename = os.path.join(self.app_data['for_inputs']['sphum_field'][i]['location'],
                                                self.app_data['for_inputs']['sphum_field'][i]['name'])
                    else:
                        filename = os.path.join('/', self.app_data['for_inputs']['sphum_field'][i]['name'])
                    self._sphum_conv_file_list[i] = self.app_data['for_inputs']['sphum_field'][i]
                    self._sphum_conv_file_list[i]['filename'] = filename
                    self._sphum_conv_file_list[i]['exp_name'] = \
                        self.app_data['for_inputs']['sphum_field'][i]['exp_name']
                    self._sphum_conv_file_list[i]['trop_field_name'] = \
                        self.app_data['for_inputs']['sphum_field'][i]['sphum_field_name']
                    self.logger.debug(self.sphum_conv_file_list[i])
            else:
                self.logger.warning(f"The 'for_inputs' entry does not specify sphum_field-containing files.")
                self._use_sphum_conv = False

    # TODO: GEOS HISTORY.rc is GEOS-specific
    # Therefore, GEOS-specific functionality should be moved to a ConfigGeos class
    def hist_list_files(self):
        """ Read GEOS HISTORY.rc file and construct the list of data files to be used.
        """
        in_files = list()
        self.logger.info(f"Processing GEOS HISTORY.rc file.")

        # Extract parameters from the configuration dictionary
        year = self.history_year
        month = self.history_month

        list_fields = self.history_to_plot
        if isinstance(list_fields, str):
            list_fields = list(list_fields.split(","))

        syear = 'Y' + str(year)
        smonth = 'M' + str(month).zfill(2)

        # Set the full path to the HISTORY.rc file
        hist_fname = os.path.join(self._history_dir, 'HISTORY.rc')
        if os.path.isfile(hist_fname):
            self.logger.debug(f"Using HISTORY.rc file: {hist_fname}")

            # Parse the HISTORY.rc file and create a dictionary of all the settings in the file
            _from_hist_rc = parse_history(hist_fname)

            _expid = _from_hist_rc['EXPID']

            # Loop over all the fields to identify the monthly file name containing each field_name.
            for field_name in list_fields:
                # Get the collection the field_name belongs to:
                list_collections = get_collection_with_field(self.history, field_name)  # TODO: fix this
                if list_collections:
                    collection = list_collections[0]
                    # TODO: directory structure + fname should be set via a template
                    # TODO: need to account for files other than 'monthly'
                    # If the field_name is in a collection, construct the monthly file name
                    # expid.collection.monthly.yyyymm.nc4
                    if self._history_season:
                        fname = _expid + '.' + collection + '.monthly.CLIM.' + \
                                self._history_season + '.nc4'
                        out_file = os.path.join(
                            self.history_dir, collection, fname)
                    else:
                        fname = _expid + '.' + collection + '.monthly.' + \
                                str(year) + str(month).zfill(2) + '.nc4'
                        # Determine full path to the file
                        # input_dir/collection/Yyyyy/Mmm/expid.collection.monthly.yyyymm.nc4
                        out_file = os.path.join(self.history_dir, collection, syear, smonth, fname)
                    # Append the file to the list
                    in_files.append(out_file)
                else:
                    self.logger.warning(
                        f"\t Field {field_name} is not available in any collection.")
                    self.logger.warning(f"\t It will not be plotted.")
                    # Remove field_name from the list
                    del self._history_to_plot[field_name]
                    if not self._history_to_plot:
                        self.logger.warning("-" * 65)
                        self.logger.warning(f"\t There are no fields to plot.")
                        self.logger.warning("-" * 65)
                        sys.exit()
        if in_files:
            self.logger.debug("---> The following files will be read in: ")
            for i, file in enumerate(in_files, start=1):
                self.logger.debug(f"{i}. {file}")

        in_files = list(set(in_files))

        return in_files

    def get_file_index(self, filename):
        """ Get the file index associated with the filename """
        for i, entry in enumerate(self.app_data['inputs']):
            if filename in entry['filename']:
                return i
        return 0

    def get_comp_file_index(self, filename, source_name):
        """  Is filename in map_params with the given source_name? if so get index
        """
        i = 0
        for key in self.map_params.keys():
            source = self.map_params[key]
            if filename in self.map_params[key]['filename'] and source == source_name:
                return i
            else:
                i += 1
        return 0

    def get_meta_coord(self, key):
        """ Return a meta coords value associated with a model's key """
        if key in self.meta_coords:
            print(key)
            return self.meta_coords[key][self.source_names[self.ds_index]]
        return None

    def get_plot_specs(self, for_name):
        plot_specs = []
        if not self.spec_data:
            return plot_specs

        ind_spec = self.spec_data[for_name]
        for k, v in ind_spec.items():
            if 'plot' in k:
                plot_specs.append(k)
        return plot_specs

    def get_levels(self, to_plot, plot_type):
        """ Get model levels to plot from YAML specs file"""
        levels = u.get_nested_key_value(self.spec_data, [to_plot, plot_type, 'levels'])
        if not levels:
            return []
        else:
            return levels

    def get_levels_old(self, toplot, plot_type):
        """ Get model levels to plot from YAML specs file"""
        try:
            if plot_type == constants.xyplot:
                return self.spec_data[toplot][constants.xyplot]['levels']
            elif plot_type == constants.polarplot:
                return self.spec_data[toplot][constants.polarplot]['levels']
            else:
                return []
        except KeyError:
            self.logger.debug('levels not specified')
            return []

    def get_file_description(self, file):
        """ Get user-defined file description (default: None)"""
        try:
            return self.file_list[file]['description']
        except Exception as e:
            self.logger.debug(f'key error {e}, returning default')
            return None

    def get_file_exp_name(self, i):
        """ Get user-defined experiment name associated with the input file (default None)"""
        try:
            return self.file_list[i]['exp_name']
        except Exception as e:
            self.logger.debug(f'key error {e}, returning default')
            return None

    def get_file_exp_id(self, i):
        """ Get user-defined experiment ID associated with the input file (default None)
        If an expid is set, then it will be used to compare with another expid, as set in compare field
        """
        try:
            return self.file_list[i]['exp_id']
        except Exception as e:
            self.logger.debug(f'key error {e}, returning default')
            return None

    @staticmethod
    def get_dim_names(pid):
        dim1, dim2 = None, None
        if 'yz' in pid:
            dim1, dim2 = 'lat', 'lev'
        elif 'xt' in pid:
            dim1 = 'time'
        elif 'tx' in pid:
            dim1, dim2 = 'lon', 'time'
        else:
            dim1, dim2 = 'lon', 'lat'
        return dim1, dim2

    def get_model_dim_name(self, dim_name):
        """ Get model-specific dimension name associated with the source as defined in meta coordinates"""
        return self._get_model_dim_name(dim_name)

    def _get_model_dim_name(self, dim_name):
        if self.source_names[self.ds_index] in self.meta_coords[dim_name]:
            return self.meta_coords[dim_name][self.source_names[self.ds_index]]
        return None

    def get_model_attr_name(self, attr_name):
        """ Get model-specific attribute name associated with the source as defined in meta attributes"""
        return self.meta_attrs[attr_name][self.source_names[self.ds_index]]

    @staticmethod
    def get_source_from_name(name):
        if name in ['generic', 'geos', 'ccm', 'cf', 'wrf', 'lis']:
            return 'generic'
        elif name in ['airnow', 'fluxnet']:
            return 'csv'
        elif name in ['omi', 'mopitt', 'landsat']:
            return 'hdf5'

    @staticmethod
    def get_default_plot_params():
        params = {
            'image.origin': 'lower',
            'image.interpolation': 'nearest',
            'image.cmap': 'gray',
            'axes.grid': False,
            'savefig.dpi': 150,
            'axes.labelsize': 10,
            'axes.titlesize': 14,
            'font.size': 10,
            'legend.fontsize': 6,  # was 10
            'xtick.labelsize': 8,
            'ytick.labelsize': 8,
            'font.family': 'sans-serif',
        }
        return params

    # TODO: Fix this or remove!
    def get_data(self, name):
        data = self.readers[0].datasets[0]['ptr'].get(name)
        if data is None:
            self.logger.error(name + " does not exist")
            return None
        if len(data.shape) == 4:
            data = data[0, 0, :, :]
        elif len(data.shape) == 3:
            data = data[0, :, :]
        elif len(data.shape) == 2:
            data = data
        else:
            self.logger.info('Data shape not supported')
        return data

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    @property
    def map_params(self):
        return self._map_params

    @property
    def subplot_specs(self):
        return self._subplot_specs

    @property
    def compare(self):
        return self._compare

    @compare.setter
    def compare(self, new_val):
        self._compare = new_val

    @property
    def extra_diff_plot(self):
        return self._extra_diff_plot

    @property
    def cmap(self):
        return self._cmap

    @property
    def use_cartopy(self):
        return self._use_cartopy

    @property
    def have_specs_yaml_file(self):
        return self._specs_yaml_exists

    @property
    def trop_height_file_list(self):
        return self._trop_height_file_list

    @property
    def sphum_conv_file_list(self):
        return self._sphum_conv_file_list

    @property
    def use_trop_height(self):
        return self._use_trop_height

    @property
    def use_sphum_conv(self):
        return self._use_sphum_conv

    @property
    def add_logo(self):
        return self._add_logo

    @property
    def print_to_file(self):
        return self._print_to_file

    @property
    def output_dir(self):
        return self._output_dir

    @property
    def print_format(self):
        return self._print_format

    @property
    def make_pdf(self):
        return self._make_pdf

    @property
    def mpl_style(self):
        return self._mpl_style

    @property
    def print_basic_stats(self):
        return self._print_basic_stats

    @property
    def use_mp_pool(self):
        return self._use_mp_pool

    @property
    def archive_web_results(self):
        return self._archive_web_results

    # TODO: Move GEOS stuff to ConfigGeos class
    @property
    def collection(self):
        return self._collection

    @property
    def use_history(self):
        return self._use_history

    @property
    def history_expid(self):
        return self._history_expid

    @property
    def history_expdsc(self):
        return self._history_expdsc

    @property
    def history_dir(self):
        return self._history_dir

    @property
    def history_collection(self):
        return self._history_collection

    @property
    def history_year(self):
        return self._history_year

    @property
    def history_month(self):
        return self._history_month

    @property
    def history_to_plot(self):
        return self._history_to_plot

    @property
    def to_plot(self):
        return self._to_plot

    @property
    def compare_exp_ids(self):
        return self._compare_exp_ids

    @property
    def file_list(self):
        # TODO: rename file_list to file_dict?
        return self._file_list

    # TODO: Move!
    @staticmethod
    def _make_plot_id(plot_type, p_index, level):
        suff = str(p_index) + '.'
        if 'yz' in plot_type:
            return "_z." + suff
        elif 'xt' in plot_type:
            return "_ts." + suff
        elif 'tx' in plot_type:
            return "_hov." + suff
        else:
            if level is not None:
                return "_" + str(level) + "." + suff
            else:
                return suff
