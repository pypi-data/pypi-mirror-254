import decimal
import json
import os
import re
import shlex
import shutil
import subprocess
import multiprocessing
import logging
import time

from numbers import Real

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfonts
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import LogFormatter
from numpy import e
from matplotlib.offsetbox import (OffsetImage, TextArea, AnchoredOffsetbox, VPacker, AnnotationBbox)
from matplotlib import rcParams as rc_matplotlib
import eviz.lib.utils as u
import eviz.lib.const as constants
from eviz.lib.utils import timer

logger = logging.getLogger('plot_utils')

UNIT_REGEX = re.compile(
    r'\A([-+]?[0-9._]+(?:[eE][-+]?[0-9_]+)?)(.*)\Z'  # float with trailing units
)
UNIT_DICT = {
    'in': 1.0,
    'ft': 12.0,
    'yd': 36.0,
    'm': 39.37,
    'dm': 3.937,
    'cm': 0.3937,
    'mm': 0.03937,
    'pc': 1 / 6.0,
    'pt': 1 / 72.0,
    'ly': 3.725e17,
}


def subproc(cmd):
    name = multiprocessing.current_process().name
    logger.debug(f'Starting {name} ')
    cmds = shlex.split(cmd)
    p = subprocess.Popen(cmds,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)
    out, err = p.communicate()
    logger.debug(f"{name} Out:\n {out}")
    logger.debug(f"{name} Err:\n {err}")
    logger.debug(f'Exiting {name}')
    return out


def plot_process(filename):
    name = multiprocessing.current_process().name
    logger.info(f'Starting {name} ')
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight')


def run_plot_commands(filenames):
    njobs = len(filenames)
    logger.info(f"Processing {njobs} jobs - please wait ...")
    procs = list()
    for i in range(njobs):
        p = multiprocessing.Process(target=plot_process, args=(filenames[i],))
        procs.append(p)
        p.start()
    for p in procs:
        p.join()


def create_pdf(config):
    from PIL import Image
    import glob
    irgb0 = None

    img_files = sorted(
        glob.glob(config.output_dir + '/*.' + config.print_format))
    pdf_file = 'eviz_plots.pdf'
    ilist = list()
    cnt = 0
    for im in img_files:
        if cnt == 0:
            i0 = Image.open(im)
            irgb0 = i0.convert('RGB')
        else:
            i = Image.open(im)
            irgb = i.convert('RGB')
            ilist.append(irgb)
        cnt += 1

    if cnt == 1 and irgb0:
        irgb0.save(config.output_dir + '/' + pdf_file)
    elif irgb0:
        irgb0.save(config.output_dir + '/' + pdf_file,
                   save_all=True, append_images=ilist)


def formatted_contours(clevs):
    new_clevs = []
    for lev in clevs:
        str_lev = str(lev)
        if "." in str_lev:
            rhs = str_lev.split(".")[1]
            if "e" in rhs or "E" in rhs:
                new_clevs.append(lev)
            elif int(rhs) == 0:
                new_clevs.append(int(float(str_lev)))
            else:
                new_clevs.append(lev)
        else:
            new_clevs.append(lev)
    return new_clevs


def axis_tick_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 12
    elif panels == (3, 1):
        font_size = 12
    elif panels == (2, 2):
        font_size = 12
    else:
        font_size = 8
    return font_size


def bar_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 12
    elif panels == (3, 1):
        font_size = 10
    elif panels == (2, 2):
        font_size = 10
    else:
        font_size = 8
    return font_size


def cbar_shrink(panels=None):
    if panels == (1, 1):  # single image on a page
        frac = 1.0
    elif panels == (3, 1):
        frac = 0.75
    elif panels == (2, 2):
        frac = 0.75
    else:
        frac = 0.5
    return frac


def contour_tick_font_size(panels):
    if panels == (1, 1):  # single image on a page
        font_size = 10
    elif panels == (3, 1):
        font_size = 8
    elif panels == (2, 2):
        font_size = 8
    else:
        font_size = 8
    return font_size


def axes_label_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 12
    elif panels == (3, 1):
        font_size = 10
    elif panels == (2, 2):
        font_size = 10
    else:
        font_size = 8
    return font_size


def cbar_pad(panels=None):
    """
    0.05 if vertical, 0.15 if horizontal;
    fraction of original axes between colorbar
    and new image axes
    """
    if panels == (1, 1):  # single image on a page
        pad = 0.05
    elif panels == (3, 1):
        pad = 0.15
    elif panels == (2, 2):
        pad = 0.05
    else:
        pad = 0.05
    return pad


def cbar_fraction(panels=None):
    """ fraction of original axes to use for colorbar """
    if panels == (1, 1):  # single image on a page
        fraction = 0.05
    elif panels == (3, 1):
        fraction = 0.1
    elif panels == (2, 2):
        fraction = 0.05
    else:
        fraction = 0.05
    return fraction


def image_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 16
    elif panels == (3, 1):
        font_size = 14
    elif panels == (2, 2):
        font_size = 14
    else:
        font_size = 'small'
    return font_size


def subplot_title_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 14
    elif panels == (3, 1):
        font_size = 12
    elif panels == (2, 2):
        font_size = 12
    else:
        font_size = 10
    return font_size


def title_font_size(panels=None):
    if panels == (1, 1):  # single image on a page
        font_size = 14
    elif panels == (3, 1):
        font_size = 12
    elif panels == (2, 2):
        font_size = 12
    else:
        font_size = 12
    return font_size


def contour_label_size(panels=None):
    if panels == (1, 1):  # single image on a page
        label_size = 8
    elif panels == (3, 1):
        label_size = 8
    elif panels == (2, 2):
        label_size = 8
    else:
        label_size = 8
    return label_size


def contour_levels_plot(clevs):
    new_clevs = []
    for lev in clevs:
        clevs_string = str(lev)
        if "e" in clevs_string:
            # print ("Digits are in scientific notation")
            new_clevs.append(lev)
        else:
            if "." not in clevs_string:
                new_clevs.append(int(lev))
            else:
                digits = clevs_string.split('.')[1]  # just get RHS of number

                if int(digits) == 0:
                    #            print ("The level: ", lev, " has no RHS!", int(lev))
                    new_clevs.append(int(lev))
                else:
                    new_clevs.append(lev)
    return new_clevs


def contour_format_from_levels(levels, scale=None):
    digits_list = []
    num_sci_format = 0
    for lev in levels:  # check each contour level
        clevs_string = str(lev)
        if "e" in clevs_string or "E" in clevs_string:  # sci notation
            num_sci_format = num_sci_format + 1
            if "e" in clevs_string or "E" in clevs_string:
                pres = abs(int(clevs_string.split('e')[1]))
                if "E" in str(pres):
                    pres = abs(int(clevs_string.split('E')[1]))
                number = decimal.Decimal(lev)
                clevs_string = str(round(number, pres + 2))
                digits1 = clevs_string.split('.')[1]  # just get RHS of number
                if "E" in str(digits1):
                    digits = digits1.split('E')[0]
                    digits_list.append(len(digits))
                elif "e" in str(digits1):
                    digits = digits1.split('e')[0]
                    digits_list.append(len(digits))
                else:
                    digits_list.append(len(digits1))
        elif "." not in clevs_string:  # not floating point
            digits_list.append(0)
        else:
            digits_list.append(len(clevs_string.split('.')[1]))  # just get RHS of number
    digits_list.sort()
    num_type = "f"
    if num_sci_format > 1:
        num_type = "e"
    if digits_list[-1] == 0:
        contour_format = "%d"
    elif digits_list[-1] <= 3:
        contour_format = "%1." + str(digits_list[-1]) + num_type
    else:
        contour_format = "%1.1e"
    if scale:
        contour_format = LogFormatter(base=e, labelOnlyBase=False)

    return contour_format


def fmt_two_digits(x, pos):
    return f'[{x:.2f}]'


def fmt(x, pos):
    """
    Format color bar labels to show scientific label
    """
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


def fmt_once(x, pos):
    """
    Format color bar labels to show scientific label but not the x10^x
    """
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${}$'.format(a)


def revise_tick_labels(cbar):
    # remove unecessary decimals
    count = 0
    labels = [item.get_text() for item in cbar.ax.get_xticklabels()]
    for label in labels:
        str_label = str(label)
        if "." in str_label:
            rhs = str_label.split(".")[1]
            lhs = str_label.split(".")[0]
            if "e" in rhs or "E" in rhs:
                if "e" in rhs:
                    split_sci_not = rhs.split("e")
                else:
                    split_sci_not = rhs.split("E")
                if int(split_sci_not[0]) == 0:
                    new_sci_not = lhs + ".e" + split_sci_not[1]
                    labels[count] = new_sci_not
            elif int(rhs) == 0:
                labels[count] = str_label.split(".")[0]
        count = count + 1
    cbar.ax.set_xticklabels(labels)
    # remove trailing zeros
    count = 0
    labels = [item.get_text() for item in cbar.ax.get_xticklabels()]
    for label in labels:
        str_label = str(label)
        if "e" not in str_label and "E" not in str_label:
            if "." in str_label:
                strip_str_label = str_label.rstrip('0')
                labels[count] = strip_str_label
        count = count + 1
    cbar.ax.set_xticklabels(labels)
    labels = [item.get_text() for item in cbar.ax.get_xticklabels()]
    # labels minus sign is not accepted by float()
    # make it acceptable:
    labels = [x.replace('\U00002212', '-') for x in labels]
    if float(labels[0]) == float(0):
        labels[0] = "0"
    cbar.ax.set_xticklabels(labels)


def colorbar(mappable):
    """
    Create a colorbar
    https://joseph-long.com/writing/colorbars/
    """
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax)
    plt.sca(last_axes)
    return cbar


def image_scaling(image, num_rows, num_cols):
    """
    Scale the image to desired length(num_rows) and width (num_cols)
    """
    number_rows = len(image)  # source number of rows
    number_columns = len(image[0])  # source number of columns
    return [[image[int(number_rows * r / num_rows)][int(number_columns * c / num_cols)]
             for c in range(num_cols)] for r in range(num_rows)]


def add_logo_xy(logo, ax, x0, y0, scale=50):
    """
    adds image logo and positions it on the figure
    at position x0, y0
    """
    # scale Image
    logo = image_scaling(logo, scale, scale)
    ax.figure.figimage(logo, x0, y0, alpha=1.0, zorder=1, origin="upper")


def add_logo_anchor(ax, logo, label=None, logo_loc='upper left', alpha=0.5):
    """
    adds image logo and optionally, text
    """
    image_box = OffsetImage(logo, alpha=alpha, zoom=0.05)
    if label:
        textbox = TextArea(label, textprops=dict(alpha=alpha))
        packer = VPacker(children=[image_box, textbox], mode='fixed', pad=0, sep=0, align='center')
        ao = AnchoredOffsetbox(logo_loc, pad=0, borderpad=0, child=packer)
    else:
        ao = AnchoredOffsetbox(logo_loc, pad=0.01, borderpad=0, child=image_box)
        ao.patch.set_alpha(0)
    ax.add_artist(ao)


def add_logo_fig(fig, logo):
    """
    adds image logo to a figure
    """
    # (x, y, width, height)
    imax = fig.add_axes([0.9, 0.9, 0.1, 0.1])
    # remove ticks & the box from imax
    imax.set_axis_off()
    # print the logo with aspect="equal" to avoid distorting the logo
    imax.imshow(logo, aspect="equal", alpha=1)


def add_logo(ax, logo):
    """
    adds image logo to axes
    """
    ax.figure.figimage(logo, 1, 1, zorder=3, alpha=.5)


def output_basic(config, name):
    if config.print_to_file:
        output_fname = name + "." + config.print_format
        output_dir = u.get_nested_key_value(config.map_params[config.pindex], ['outputs', 'output_dir'])
        if not output_dir:
            output_dir = constants.output_path
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = os.path.join(output_dir, output_fname)
        plt.savefig(filename, bbox_inches='tight')
    else:
        plt.tight_layout()
        plt.show()


def get_subplot_geometry(axes):
    ss = axes.get_subplotspec()
    geom = ss.get_geometry()[0:2]
    return geom, int(ss.is_first_row()), int(ss.is_first_col()), int(ss.is_last_row()), int(ss.is_last_col())


def dump_json_file(config, plot_type, findex, map_filename, fig, output_dir):
    vis_summary = {}
    source_name = config.source_names[config.ds_index]
    event_stamp = source_name + '_web'

    map_params = config.map_params
    exp_name = map_params[config.pindex]['exp_name']
    field_name = map_params[config.pindex]['field']
    figure = fig
    vis_summary[findex] = {}
    if exp_name:
        vis_summary[findex]['title'] = exp_name
    else:
        axes = figure.get_axes()
        title = axes[0].get_title(loc='left')
        vis_summary[findex]['title'] = title
    vis_summary[findex]['model'] = source_name
    vis_summary[findex]['config_name'] = map_params[config.pindex]['filename']
    vis_summary[findex]['plot_type'] = plot_type
    vis_summary[findex]['level'] = config.level
    if config.level:
        vis_summary[findex]['level'] = config.level

    vis_summary[findex]['filename'] = map_filename
    vis_summary[findex]['field_name'] = field_name

    summary_path = os.path.join(output_dir, event_stamp, event_stamp + '.json')
    vis_summary['time_now'] = time.time()
    vis_summary['log'] = load_log()
    vis_summary['input_files'] = config.file_list
    vis_summary['time_exec'] = timer(config.start_time, time.time())

    archive(output_dir, event_stamp)

    with open(summary_path, 'w') as fp:
        json.dump(vis_summary, fp)
        fp.close()


def load_log():
    """ Retrieve Eviz.LOG used by streamlit """
    with open('Eviz.LOG') as fp:
        lines = fp.readlines()
        fp.close()

    return lines


def archive(output_dir, event_stamp):
    """ Archive data for web results

    Parameters:
        output_dir (str) : Output directory to store images
        event_stamp (str) : Time stamp for archived web results
    """
    fs = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
    full_fs = [os.path.join(output_dir, f) for f in fs]
    archive_path = os.path.join(output_dir, event_stamp)
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)

    for f in full_fs:
        shutil.move(f, archive_path)


def print_map(config, plot_type, findex, fig, level=None):
    map_params = config.map_params
    exp_id = map_params[config.pindex]['exp_id']
    field_name = map_params[config.pindex]['field']

    # Get output directory from Config...
    if config.compare:
        output_dir = u.get_nested_key_value(map_params[config.pindex], ['outputs'])
    else:
        output_dir = u.get_nested_key_value(map_params[config.pindex], ['outputs', 'output_dir'])
    # ...or from Eviz default location
    if not output_dir:
        output_dir = constants.output_path
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    levstr = ''
    if level:
        levstr = "_" + str(level)

    if not config.compare:
        if exp_id:
            exp_id_suf = "_" + str(exp_id) + "."
        else:
            exp_id_suf = "_" + str(config.findex) + "."
    else:
        exp_id_suf = "."

    if 'xy' in plot_type:
        fname = field_name + levstr + exp_id_suf
    elif 'yz' in plot_type:
        fname = field_name + "_yz" + exp_id_suf
    else:
        fname = field_name + "_" + plot_type + exp_id_suf

    if config.print_to_file:
        map_filename = fname + config.print_format
        filename = os.path.join(output_dir, map_filename)
        fig.fig.tight_layout()
        fig.fig.savefig(filename, bbox_inches='tight', dpi=300)
        if config.archive_web_results:
            dump_json_file(config, plot_type, findex, map_filename, fig.fig, output_dir)
    else:
        plt.tight_layout()
        plt.show()


class OOMFormatter(matplotlib.ticker.ScalarFormatter):
    def __init__(self, order=0, fformat="%1.1f", offset=True, math_text=True):
        self.oom = order
        self.fformat = fformat
        matplotlib.ticker.ScalarFormatter.__init__(self, useOffset=offset, useMathText=math_text)

    def _set_order_of_magnitude(self):
        self.orderOfMagnitude = self.oom

    def _set_format(self):
        self.format = self.fformat
        if self._useMathText:
             self.format = r'$\mathdefault{%s}$' % self.format
