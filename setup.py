#setup.py
from setuptools import setup
#from distutils.core import setup

# This call to setup() does all the work
setup (
    name = 'thorbell',
    version = '0.0.11',
    description="Firmware for CSB-MercurioR1, from THORBELL",
    url="https://github.com/4rielo/thorbell.git",
    author="Ariel Scarafia",
    author_email="ombas.gm@gmail.com",
    packages=['CSB_MercurioR1'],
    package_dir={'CSB_MercurioR1':'CSB_MercurioR1'},
    package_data={
        'CSB_MercurioR1': ['data/*'],
        'CSB_MercurioR1': ['docs/*'],
        'CSB_MercurioR1': ['fonts/*'],
        'CSB_MercurioR1': ['icons/*.png'],
        'CSB_MercurioR1': ['images/*.png'],
        },
    include_package_data=True,
)