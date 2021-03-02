## Originpro Plots
<p>Matplotlib style for making originpro plot figures
This repo has Matplotlib Originpro style to format your figure for scientific publications and presentation.</p>

## Getting Started
The easist way to install OriginproPlots is to use [pip](https://pip.pypa.io/en/stable/): 
```
# to install the latest release (from PyPI) 
pip install OriginproPlots

# to install latest commit (from GitHub)
pip install git+https://github.com/mcekwonu/OriginproPlots.git
```

The pip installation will automatically move all of the Matplotlib style files ```*.mplstyle``` into the appropriate directory on your computer.

Please see the [FAQ](https://github.com/mcekwonu/OriginproPlots#faq) section for more information and troubleshooting.

## Using the Style
"originpro" is the main style from this repo. Whenever you want to use it, simply add the following to the top of your python script:
```python
import matplotlib.pyplot as plt
plt.style.use('originpro')
```
To use any of the styles temporarily, you can use:
```python
with plt.style.context(['originpro']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

You can adjust the legend borderpad for proper placement if you have more that four parameters using:

```python
# for example, manually set the borderpad after trying out the position values and update the matplotlib parameters.
import matplotlib.pyplot as plt
plt.style.use('originpro')
plt.rcParams.update({
'legend.borderaxespad': -4.5 })     # specify value here
```
## Examples
The ```Originpro``` style:

## Help and Contribution
<p>Please feel free to contribute to the OriginproPlots repo! Before starting a new style or making any changes, please create an issue through the GitHub issue tracker. That way we can discuss if the changes are necessary and the best approach.</p>

If you need any help with OriginproPlots, please first check the [FAQ](https://github.com/mcekwonu/OriginproPlots#faq) and search through the [previous GitHub issues](https://github.com/mcekwonu/OriginproPlots/issues). If you can't find an answer, create a new issue through the [GitHub issue tracker](https://github.com/mcekwonu/OriginproPlots/issues).

You can checkout [Matplotlib's documentation](https://matplotlib.org) for more information on plotting settings.

## FAQ
1. Installing OriginproPlots manually

    * If you like, you can install the ```*.mplstyle``` files manually. First, clone the repository and then copy all of the ```*.mplstyle``` files into your Matplotlib style directory.  
    If you're not sure where this is, in an interactive python console type:

        ```python
        import matplotlib
        print(matplotlib.get_configdir())
        ```
    
    * You should get back something like ```/home/mcekwonu/.matplotlib```. You would then put the ```*.mplstyle``` files in ```/home/mcekwonu/.matplotlib/stylelib/``` (you may need to create the stylelib directory):

        ```python 
        cp styles/*/*.mplstyle ~/.matplotlib/stylelib/
        ```

2. Using different fonts:

    * originproPlots uses the default sans-serif font. If you would like to specify a different font, you can use:
        ```python
        import matplotlib.pyplot as plt
        plt.style.use('originpro')
        plt.rcParams.update({
        "font.family": "serif",   # specify font family here
        "font.serif": ["Times"],  # specify font here
        "font.size":11})          # specify font size here
        ```
3. Installing OriginproPlots within Google Colab, IPython, Jupyter Notebooks, etc.:
    
    * After installing OriginproPlots within one of these environments, you may need to reload the Matplotlib style library. For example:
        ```python
        !pip install OriginproPlots
        import matplotlib.pyplot as plt
        plt.style.reload_library()
        plt.style.use('science')
        ```

## OriginproPlots in Academic Papers
The following papers use OriginproPlots:

If you use ```OriginproPlots``` in your paper/thesis, feel free to add it to the list!

## Citing OriginproPlots

You don't have to cite OriginproPlots if you use it but it's nice if you do:


```latex
- id: mcekwonu2021
  title: mcekwonu/OriginproPlots
  author:
  - family: Ekwonu
    given: Michael C.
    month: mar
    year:  2021
    publisher: {}
    version: {1.0.0}
    type: article
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
