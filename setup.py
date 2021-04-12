#setup.py
import pathlib
from setuptools import setup

include_files = ['*.txt']

# This call to setup() does all the work
setup (
    name = 'thorbell',
    version = '0.0.4',
    description="Firmware for CSB-MercurioR1, from THORBELL",
    url="https://github.com/4rielo/thorbell.git",
    author="Ariel Scarafia",
    author_email="ombas.gm@gmail.com",
    data_files = include_files,
)