import os
import logging
import time
from argparse import Namespace
from dataclasses import dataclass, field
from eviz.lib.eviz.config import Config
from eviz.models.root_factory import GenericFactory, WrfFactory, LisFactory
from eviz.models.root_factory import AirnowFactory
from eviz.models.root_factory import MopittFactory
from eviz.models.root_factory import LandsatFactory
from eviz.models.root_factory import OmiFactory
from eviz.models.root_factory import FluxnetFactory
import eviz.lib.const as constants


def get_config_path_from_env():
    env_var_name = "EVIZ_CONFIG_PATH"
    return os.environ.get(env_var_name)


def create_config(args):
    source_names = args.sources[0].split(',')
    config_dir = args.config
    config_file = args.configfile
    if config_file:
        return Config(source_names=source_names, config_files=config_file)

    if config_dir:
        config_files = [os.path.join(config_dir[0], source_name, f"{source_name}.yaml") for source_name in
                        source_names]
    else:
        config_dir = get_config_path_from_env()
        if not config_dir:
            print(f"Warning: No configuration directory specified. Using default.")
            config_dir = constants.config_path
        config_files = [os.path.join(config_dir, source_name, f"{source_name}.yaml") for source_name in
                        source_names]

    return Config(source_names=source_names, config_files=config_files)


def get_factory_from_user_input(inputs):
    """ Return subclass associated with user input sources"""
    mappings = {
        "test": GenericFactory(),      # for unit tests
        "generic": GenericFactory(),   # generic is NetCDF
        "geos": GenericFactory(),      # use this for MERRA
        "ccm": GenericFactory(),       # CCM and CF are "special" streams
        "cf": GenericFactory(),
        "lis": LisFactory(),
        "wrf": WrfFactory(),
        "airnow": AirnowFactory(),     # CSV
        "fluxnet": FluxnetFactory(),   # CSV
        "omi": OmiFactory(),           # HDF5
        "mopitt": MopittFactory(),     # HDF5
        "landsat": LandsatFactory(),   # HDF4
        # Add other mappings for other subclasses
        # Need MODIS, GRIB, CEDS, EDGAR
    }
    return [mappings[i] for i in inputs]


@dataclass
class Eviz:
    """ This is the Eviz class definition. It takes in a list of (source) names and creates
    data-reading-classes (factories) associated with each of those names.

    Parameters:
        source_names (list): source models to process
        factory_models (list): source models to process
        args (Namespace): source models to process
    """
    source_names: list
    args: Namespace = None
    model_info: dict = field(default_factory=dict)
    model_name: str = None
    _config: Config = None

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    @property
    def config(self):
        return self._config

    def __post_init__(self):
        self.logger.info("Start init")
        # Add this workaround to simplify working within a Jupyter notebook, that is to avoid
        # having to pass a Namespace() object, create args with the appropriate defaults
        if not self.args:
            self.args = Namespace(sources=self.source_names,
                                  compare=False,
                                  file=None, vars=None,
                                  configfile=None, config=None,
                                  data_dirs=None, output_dirs=None,
                                  verbose=1)
        self.factory_sources = get_factory_from_user_input(self.source_names)
        self._config = create_config(self.args)
        # TODO: Associate each model with its corresponding data directory
        #  Note that data can be in local disk or even in a remote locations
        # TODO: enable processing of S3 buckets

    def run(self):
        """ Create plots """
        _start_time = time.time()
        self._config.start_time = _start_time
        _model = self.factory_sources[0].create_root_instance(self.config)
        _model()

    def set_data(self, input_files):
        """ Assign model input files as specified in model config file

        Parameters:
            input_files (list): Names of input files
        """
        config = self.model_info[self.model_name]['config']
        config.set_input_files(input_files)

    def set_output(self, output_dir):
        """ Assign model output directory as specified in model config file

        Parameters:
            output_dir (str): Name output directory
        """
        config = self.model_info[self.model_name]['config']
        config.set_output_dir(output_dir)
