"""
This code defines the script required by setuptools.
"""

# Non-standard imports.
from setuptools import setup

# Local constants.
PACKAGE_NAME = "hosker_rutil"
VERSION = "1.1.0"
DESCRIPTION = "Rust utility functions"
GIT_URL_STEM = "https://github.com/tomhosker"
AUTHOR = "Tom Hosker"
AUTHOR_EMAIL = "tomdothosker@gmail.com"
SCRIPT_PATHS = ("scripts/hosker-rutil-install-specials",)
INSTALL_REQUIRES = ("hosker_utils", "numpy")
INCLUDE_PACKAGE_DATA = True

###################################
# THIS IS WHERE THE MAGIC HAPPENS #
###################################

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=GIT_URL_STEM+"/"+PACKAGE_NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    package_dir={ PACKAGE_NAME: "source" },
    packages=[PACKAGE_NAME],
    scripts=SCRIPT_PATHS,
    install_requires=INSTALL_REQUIRES,
    include_package_data=INCLUDE_PACKAGE_DATA
)
