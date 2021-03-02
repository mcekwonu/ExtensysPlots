"""Install Originpro style plotting

This will copy the *.mplstyle files into the right directory.

"""

import atexit
import glob
import os
import shutil

import matplotlib
import matplotlib.pyplot as plt
from setuptools import setup
from setuptools.command.install import install


root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()


def install_styles():
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)

    # find stylelib directory, where the *.mplstyle file goes
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    # copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallation(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


setup(
    name='OriginproPlot',
    version='1.0.0',
    author="Chukwuemeka Michael Ekwonu",
    author_email="michael.ekwonu@gmail.com",
    description="Format Matplotlib for originpro style plotting",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "originpro-style",
        "scientific-papers",
        "matplotlib-styles",
        "python"
    ],
    url="https://github.com/mcekwonu/OriginproPlot/",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallation, },
)
