# OriginproPlot
Matplotlib style for making originpro plot figures
This repo has Matplotlib OriginPro style to format your figure for scientific publications and presentation.

# Getting started
The easist way to install OriginproPlot is to use pip: 
```
# to install the latest release (from PyPi) 
pip install OriginproPlot

# to install latest commit (from github)
pip install git+https://github.com/mcekwonu/OriginproPlot.git
```

The pip installation will automatically move all of the Matplotlib style files *.mplstyle into the appropriate directory on your computer.

Please see the FAQ section for more information and troubleshooting.

# Using the Style
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

You can adjust the legend borderpad for proper placement if you have more that four parameters using:
for example, and manually set the borderpad after trying out the position values.
```python

plt.rcParams['legend.borderaxespad'] = -4.5
    plt.rcParams.update()
