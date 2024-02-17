import re

def is_landsat(fn):
    """ Determines if an object holds Landsat info from its filename

    Returns:
        Boolean
    """
    lxs = "L[COITEM][1-8]"
    loc = "[0-9][0-9][0-9]" + "[0-9][0-9][0-9]"
    date = "[12][0-9][0-9][0-9]" + "[0-3][0-9][0-9]"
    data = "[A-Z][A-Z][A-Z]" + "[0-9][0-9]"
    ext = "[.]..."

    convention = "^.*" + lxs + loc + date + data + ext
    match = re.search(convention, fn)

    if isinstance(match, type(None)):
        return False
    else:
        if match.group() == fn:
            return True
        else:
            return False

def is_omi(fn):
    """ Determines if an object holds omi info from its filename

    Returns:
        Boolean
    """
    instr = "OM.+"
    dtype = "L[1-3]-.+"
    date = "[1-2][0-9][0-9][0-9]m[0-1][0-9][0-3][0-9].*"
    vers = "v[0-0][0-9][0-9]-" + date + "t[0-2][0-9][0-6][0-9][0-6][0-9]"
    ext = "[.]..."

    convention = "^.*" + instr + "_" + dtype + "_" + date + "_" + vers + ext
    match = re.search(convention, fn)

    if isinstance(match, type(None)):
        return False
    else:
        if match.group() == fn:
            return True
        else:
            return False