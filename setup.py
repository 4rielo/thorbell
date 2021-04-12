#setup.py
#from setuptools import setup
from distutils.core import setup

# This call to setup() does all the work
setup (
    name = 'thorbell',
    version = '0.0.7',
    description="Firmware for CSB-MercurioR1, from THORBELL",
    url="https://github.com/4rielo/thorbell.git",
    author="Ariel Scarafia",
    author_email="ombas.gm@gmail.com",
    packages=['CSB_MercurioR1','data','docs','fonts','icons','images']
)