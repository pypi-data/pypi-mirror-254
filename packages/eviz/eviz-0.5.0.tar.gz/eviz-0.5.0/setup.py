import sys
from setuptools import setup

about = {}
with open("eviz/__about__.py", "r") as fp:
    exec(fp.read(), about)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        error = """
        Python {py} detected.
        """.format(py='.'.join(str(v) for v in sys.version_info[:3]))
        print(error)
        sys.exit(1)

    setup(version=about["__version__"])
