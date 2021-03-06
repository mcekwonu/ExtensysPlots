# Extensys Plots

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4572436.svg)](https://doi.org/10.5281/zenodo.4572436)

Matplotlib extensys style for making figures
This repo has Matplotlib Extensys style to format your figure for scientific publications and presentation.

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig1.png" width=500>

## Getting Started
The easist way to install ExtensysPlots is to use [pip](https://pip.pypa.io/en/stable/): 
```
# to install the latest release (from PyPI) 
pip install ExtensysPlots

# in Ubuntu/Debian
python3 -m pip install extensysplots

# to install latest commit (from GitHub)
pip install git+https://github.com/mcekwonu/ExtensysPlots.git
```

The pip installation will automatically move all of the Matplotlib style files ```*.mplstyle``` into the appropriate directory on your computer.

Please see the [FAQ](https://github.com/mcekwonu/ExtensysPlots#faq) section for more information and troubleshooting.

## Using the Style

"extensys" is the main style from this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt
plt.style.use('extensys')
```

Available styles include: 

```python
extensys, extensys-pl, extensys-gd, extensys-nb, extensys-sc
```

To use any of the styles temporarily, you can use:

```python
with plt.style.context(['extensys']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

The default format to save figure is ```.png``` with ```dpi=500```. Other formats by obtained by passing it in the ```plt.savefig``` as well as the ```dpi```. For example:

```python
plt.savefig("figures/fig1" + ".pdf", dpi=1000)
```

## Examples
<p /p>

The ```extensys``` style:

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig1.png" width=500>


<p /p>

The ```extensys-ms``` style (with markers)

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig2.png" width=500>


<p /p>

The ```extensys-gd``` style (with grid)

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig3.png" width=500>


<p /p>

The ```extensys-nb``` style (with jupyter notebook)

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig4.png" width=500>


<p /p>

The ```extensys``` + ```dark_background``` style

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig5.png" width=500>


<p /p>

The ```extensys-sc``` style (with scatter)

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig6.png" width=500>



<p /p>

The ```extensys-pl``` plain style

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig7.png" width=600>


<p /p>

Plotting multiple left and right y-axis using ```extensys``` style

<img src="https://github.com/mcekwonu/ExtensysPlots/raw/main/examples/figures/fig8.png" width=600>


## Help and Contribution

Please feel free to contribute to the ExtensysPlots repo! Before starting a new style or making any changes, please create an issue through the [GitHub issue tracker](https://github.com/mcekwonu/ExtensysPlots/issues). 

If you need any help with ExtensysPlots, please first check the [FAQ](https://github.com/mcekwonu/ExtensysPlots#faq) and search through the [previous GitHub issues](https://github.com/mcekwonu/ExtensysPlots/issues). If you can't find an answer, create a new issue through the [GitHub issue tracker](https://github.com/mcekwonu/ExtensysPlots/issues).

You can checkout [Matplotlib's documentation](https://matplotlib.org) for more information on plotting settings.

## FAQ

1. Installing ExtensysPlots manually

    * If you like, you can install the ```*.mplstyle``` files manually. First, clone the repository and then copy all of the ```*.mplstyle``` files into your Matplotlib style directory.  
    If you're not sure where this is, in an interactive python console type:

        ```python
        import matplotlib
        print(matplotlib.get_configdir())
        ```
        
        In my case it returned ```/home/mce/.config/matplotlib``` on Ubuntu and ```C:\Users\User\.matplotlib``` on Windows. Please verify the location of matplotib configdir as the location may differ for different users depending on how the matplotlib package was installed.
    
    * You should get back something like ```/home/mce/.config/matplotlib```. You would then put the ```*.mplstyle``` files in ```/home/mce/.config/matplotlib/stylelib/``` (you need to create the stylelib directory):
    * For Ubuntu
        ```python 
        cp styles/*.mplstyle ~/.config/matplotlib/stylelib/
        ```
   * For Windows
        ```python
        cp styles/*.mplstyle ~/.matplotlib/stylelib/
        ```

2. Using different fonts:

    * ExtensysPlots uses the default sans-serif font. If you would like to specify a different font, you can use:
    
        ```python
        import matplotlib.pyplot as plt
        plt.style.use('extensys')
        plt.rcParams.update({
        "font.family": "serif",   # specify font family here
        "font.serif": ["Times"],  # specify font here
        "font.size":12})          # specify font size here
        ```
        
3. Adjusting the legend placement:

    * You can adjust the legend borderpad when you have more than four legend parameters, for proper placement. You will need to try different values manually and see that it is placed correctly.
        ```python
        import matplotlib.pyplot as plt
        plt.style.use('extensys')
        plt.rcParams.update({"legend.borderaxespad": -4.0})
        ```
        
4. Installing ExtensysPlots within Google Colab, IPython, Jupyter Notebooks, etc.:
    
    * After installing ExtensysPlots within one of these environments, you may need to reload the Matplotlib style library. For example:
    
        ```python
        !pip install ExtensysPlots
        import matplotlib.pyplot as plt
        plt.style.reload_library()
        plt.style.use('extensys')
        ```

## ExtensysPlots in Academic Papers

The following papers used ExtensysPlots:

 * M.T. Nasir, M.C. Ekwonu, J.A. Esfahani, K.C. Kim, ["Performance assessment and multi-objective optimization of an organic Rankine cycles and vapor compression cycle based combined cooling, heating, and power system"](https://doi.org/10.1016/j.seta.2021.101457), Sustainable Energy Technologies and Assessments, Volume 47, 2021, 101457, ISSN 2213-1388. [(open access)](https://www.sciencedirect.com/science/article/pii/S2213138821004677).

If you use ```ExtensysPlots``` in your paper/thesis, feel free to add it to the list!

## Citation

You don't have to cite ExtensysPlots if you use it but it's nice if you do:

```latex
@article{ExtensysPlots,
    author    = {Michael Chukwuemeka Ekwonu},
    title     = {{mcekwonu/ExtensysPlots}},
    month     = {mar},
    year      = {2021},
    publisher = {},
    version   = {1.0.0},
    doi       = {10.5281/zenodo.4572436},
    url       = {https://doi.org/10.5281/zenodo.4572436}
}
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
