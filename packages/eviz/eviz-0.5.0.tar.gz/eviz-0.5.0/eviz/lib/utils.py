import sys
import os
import errno
import yaml
import logging
import pathlib
import subprocess
import matplotlib.pyplot as plt
from matplotlib.transforms import BboxBase as bbase
from . import const as constants

logger = logging.getLogger(__name__)


def logger_setup(logger_name, verbose=1):
    """Set up the application logger.

    Args:
        logger_name (str) : Name of the logger.
        verbose (int) : verbosity level.
    """

    # Set STDOUT verbose level
    verbose_level = logging.INFO
    if verbose == 2:  # DEBUG
        verbose_level = logging.DEBUG
    elif verbose == 1:  # INFO
        verbose_level = logging.INFO
    elif verbose == 0:  # ERROR
        verbose_level = logging.ERROR

    # Note LOG file is always set to verbose_level = logging.DEBUG
    logging.basicConfig(
        filename=str(logger_name) + ".LOG",
        format="%(levelname)s :: %(module)s (%(funcName)s:%(lineno)d) : %(message)s",
        level=logging.DEBUG,
        filemode="w",
    )
    # Add a stream handler (using stdout) to default logger
    stdout_log = logging.StreamHandler(sys.stdout)
    # Set level to INFO
    stdout_log.setLevel(verbose_level)
    formatter = logging.Formatter("%(levelname)s :: %(module)s (%(funcName)s:%(lineno)d) : %(message)s")
    stdout_log.setFormatter(formatter)
    root = logging.getLogger()
    root.addHandler(stdout_log)
    plt.set_loglevel("info")
    logging.getLogger('PIL').setLevel(logging.WARNING)


def load_yaml(yaml_filename):
    """Given a YAML file, create the corresponding YAML data structure .

    Args:
        yaml_filename (str) : Path to the YAML file.

    Returns:
        yaml_config (yaml) : A YAML data structure.
    """
    my_yaml = os.path.abspath(yaml_filename)
    try:
        logger.debug('loading yaml %s' % my_yaml)
        with open(my_yaml) as f:
            yaml_config = yaml.load(f, Loader=yaml.FullLoader)
            logger.debug('%s yaml loaded successfully' % my_yaml)
        return yaml_config
    except FileNotFoundError:
        logger.error(f'{my_yaml} does not exist')
        return None
    except yaml.scanner.ScannerError:
        logger.error(f'YAML syntax error in {my_yaml}.')
        return None
    except Exception as e:
        logger.error(f'loading yaml failed {str(e.value)}')
        return None


def get_default_yaml_path(model_name) -> str:
    """Retrieve the default YAML path associated with a model.

    Args:
        model_name (str) :  Model name.
    Returns:
        yaml_config (str) :  YAML file path relative to EViz top level directory.
    """
    if model_name == 'ccm':
        return constants.ccm_yaml_path
    elif model_name == 'cf':
        return constants.cf_yaml_path
    elif model_name == 'geos':
        return constants.geos_yaml_path
    elif model_name == 'lis':
        return constants.lis_yaml_path
    elif model_name == 'wrf':
        return constants.wrf_yaml_path
    elif model_name == 'generic':
        return constants.generic_yaml_path
    else:  # It should never get here, but just in case:
        logger.error(f"{model_name} is not supported.")
        sys.exit()


def timer(start_time, end_time):
    """Simple timer.

    Args:
        start_time (time.time) : Start time
        end_time (time.time) : end time

    Returns:
        Time duration
    """
    from datetime import timedelta
    return str(timedelta(seconds=(end_time - start_time)))


def get_repo_root_dir(repo_path: str) -> str:
    """Given a path to a file or dir in a repo, find the root directory of the repo.

    Args:
        repo_path (str) :  Any path into the repo.

    Returns:
        The repo's root directory.
    """
    path = pathlib.Path(repo_path)
    if not path.is_dir():
        path = path.parent
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        universal_newlines=True,
        cwd=str(path),
    )
    proc.check_returncode()
    return proc.stdout.strip()


def mkdir_p(path):
    # Layer on top of os.makedirs - with error checking
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            logger.error("Permission denied: cannot create " + path)
            sys.exit()


def get_nested_key_value(dictionary, keys):
    """
    Get the value of a nested key in a dictionary.

    Parameters:
    - dictionary: The input dictionary.
    - keys: A list of keys specifying the path to the nested key.

    Returns:
    - The value of the nested key, or None if the key doesn't exist.
    """
    current_dict = dictionary
    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            return None
    if isinstance(current_dict, str) and ',' in current_dict:
        current_dict = current_dict.split(',')
    return current_dict


def get_reader_from_name(name):
    """ Get reader name (as defined in RootFactory) from a given source name """
    if name in ['generic', 'geos', 'ccm', 'cf', 'wrf', 'lis']:
        return 'generic'
    elif name in ['airnow', 'fluxnet']:
        return 'csv'
    elif name in ['omi', 'mopitt', 'landsat']:
        return 'hdf5'


def get_season_from_file(file_name):
    if "ANN" in file_name:
        return "ANN"
    elif "JJA" in file_name:
        return "JJA"
    elif "DJF" in file_name:
        return "DJF"
    elif "SON" in file_name:
        return "SON"
    elif "MAM" in file_name:
        return "MAM"
    else:
        return None


def read_meta_coords() -> dict:
    """ Read meta coordinates YAML file and load into data structure"""
    root_path = os.path.dirname(os.path.abspath('eviz_base.py'))
    coord_file_path = constants.meta_coords_path
    if not os.path.exists(coord_file_path):
        coord_file_path = os.path.join(
            root_path, constants.meta_coords_path)
    return load_yaml(coord_file_path)


def read_meta_attrs() -> dict:
    """ Read meta attributes YAML file and load into data structure"""
    root_path = os.path.dirname(os.path.abspath('eviz_base.py'))
    attr_file_path = constants.meta_attrs_path
    if not os.path.exists(attr_file_path):
        attr_file_path = os.path.join(
            root_path, constants.meta_attrs_path)
    return load_yaml(attr_file_path)


def squeeze_fig_aspect(fig, preserve='h'):
    # https://github.com/matplotlib/matplotlib/issues/5463
    preserve = preserve.lower()
    bb = bbase.union([ax.bbox for ax in fig.axes])

    w, h = fig.get_size_inches()
    if preserve == 'h':
        new_size = (h * bb.width / bb.height, h)
    elif preserve == 'w':
        new_size = (w, w * bb.height / bb.width)
    else:
        raise ValueError(
            'preserve must be "h" or "w", not {}'.format(preserve))
    fig.set_size_inches(new_size, forward=True)
