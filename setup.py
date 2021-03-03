"""Install OriginproPlot.

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


package_name = 'OriginproPlot'

# Get the description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as fb:
    long_description = fb.read()


def install_styles():
    style_files = glob.glob('styles/**/*.mplstyle', recursive=True)

    # find stylelib directory, where the *.mplstyle file goes
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    # copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for style_file in style_files:
        print(os.path.basename(style_file))
        shutil.copy(
            style_file,
            os.path.join(mpl_stylelib_dir, os.path.basename(style_file)))


class PostInstallation(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


setup(
    name=package_name,
    version='1.0.0',
    author="Chukwuemeka Michael Ekwonu",
    author_email="mersthub@gmail.com",
    description="Matplotlib format for originpro style plots",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords=[
        "originpro-plot",
        "matplotlib-style-sheets",
        "scientific-publications",
        "matplotlib-figures",
        "python"
    ],
    url="https://github.com/mcekwonu/OriginproPlot/",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallation, },
)
