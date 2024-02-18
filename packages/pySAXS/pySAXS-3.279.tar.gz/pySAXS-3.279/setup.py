#!/usr/bin/env python

# This file is licensed under the CeCILL License
# See LICENSE for details.

#from distutils.core import setup
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from __init__ import __version__,__subversion__,__author__,__author_email__,__url__
#import pyshortcuts
#import pySAXS

setup(name='pySAXS',
      version=__version__+__subversion__,
      description='Python for Small Angle X-ray Scattering data treatment',
      long_description="Python for Small Angle X-ray Scattering data acquisition, treatment and computation of model SAXS intensities",
      author=__author__,
      author_email=__author_email__,
      url=__url__,
      license='CeCILL',
      package_dir={'pySAXS' : '.'},
      packages=['pySAXS','pySAXS.LS','pySAXS.guisaxs','pySAXS.guisaxs.qt',\
                'pySAXS.models','pySAXS.tools','pySAXS.models.super','pySAXS.examples',\
                'pySAXS.mcsas','pySAXS.filefilters'],
      #all files (.dat or pdf) are specified in MANIFEST.in
      package_data = {'pySAXS' : ['doc/*','filefilters/*.ini','saxsdata/*',\
                                  'guisaxs/qt/*.*','guisaxs/images/*.*','guisaxs/ui/*.*','*.txt','xraylib/*']},
      install_requires=['lmfit','ConfigParser','unidecode','weightedstats','pyshortcuts','pyFAI','numba','openpyxl','PyQt5','pandas','openpyxl'],
      #extras_require={"PDF":  ["ReportLab>=1.2", "RXP"],"RST": ["docutils>=0.3"] },
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points = {
        'console_scripts': ['pysaxs = pySAXS.guisaxs.qt.mainGuisaxs:main'],
    }
    
)
