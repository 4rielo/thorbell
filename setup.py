#setup.py
import esky.bdist_esky
from esky.bdist_esky import Executable as Executable_Esky
from cx_Freeze import setup, Executable

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text

include_files = ['*.txt']

# This call to setup() does all the work
setup (
    name = 'thorbell',
    version = '0.0.3',
    description="Firmware for CSB-MercurioR1, from THORBELL",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/4rielo/thorbell.git",
    author="Ariel Scarafia",
    author_email="ombas.gm@gmail.com",
    data_files = include_files,
)