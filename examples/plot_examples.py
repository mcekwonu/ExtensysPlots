"""Plot examples of ExtensysPlots style."""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from examples.utils import is_exist_dir, make_patch_spines_invisible


def g(x, m, L=10):
    return np.cosh(m*(L-x)) / np.cosh(m*L)


save_dir = os.path.join(os.path.dirname(__file__), 'figures')
is_exist_dir(save_dir)

pparams = dict(xlabel='Fractional distance into pore, $x/L$', ylabel='Concentration $(mol.dm^{-3})$')

x = np.linspace(0, 1, 301)


with plt.style.context(['extensys']):
    fig, ax = plt.subplots()

    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig1'.format(save_dir), dpi=300)


with plt.style.context(['extensys-ms']):
    fig, ax = plt.subplots()

    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig2'.format(save_dir), dpi=300)


with plt.style.context(['extensys-gd']):
    fig, ax = plt.subplots()

    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig3'.format(save_dir), dpi=300)


with plt.style.context(['extensys-nb']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.7, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig4'.format(save_dir), dpi=300)


with plt.style.context(['extensys', 'dark_background']):
    fig, ax = plt.subplots()
    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.7, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig5'.format(save_dir), dpi=300)


with plt.style.context(['extensys-sc']):
    fig, ax = plt.subplots()

    for i in range(10):
        x = np.random.normal(0, 5, 40)
        y = 2*x + np.random.normal(0, 2, 40)
        ax.plot(x, y, label=r"$\#${}".format(i + 1))

    ax.set_xlabel(r"$\log_{2}\left(\frac{t}{t_o}\right)$")
    ax.set_ylabel(r"$\log_{2}\left(\frac{L}{L_o}\right)$")
    ax.set_xlim([-1, 5])
    ax.set_ylim([-1, 5])
    ax.legend(bbox_to_anchor=(0.7, 1.0, 0.2, 0.1), ncol=5)
    fig.savefig('{}/fig6'.format(save_dir), dpi=300)


with plt.style.context(['extensys-pl']):
    fig, ax = plt.subplots()

    for i, m in enumerate([1.0, 5.0, 10.0, 20.0, 25.0, 50.0]):
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig7'.format(save_dir), dpi=300)


# data for multiple y-axis plot
df = pd.read_csv('data.csv')
labels = df.columns

with plt.style.context(['extensys']):
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax4 = ax.twinx()

    ax3.spines["left"].set_position(("axes", -0.25))
    make_patch_spines_invisible(ax3)
    ax3.spines["left"].set_visible(True)
    ax3.yaxis.tick_left()
    ax3.yaxis.set_label_position("left")

    ax4.spines["right"].set_position(("axes", 1.25))
    make_patch_spines_invisible(ax4)
    ax4.spines["right"].set_visible(True)

    p1, = ax.plot(df[labels[0]], df[labels[1]], color='red', label=labels[1])
    p2, = ax2.plot(df[labels[0]], df[labels[3]], color='brown', label=labels[3])
    p3, = ax3.plot(df[labels[0]], df[labels[2]], color='limegreen', label=labels[2])
    p4, = ax4.plot(df[labels[0]], df[labels[4]], color='orange', label=labels[4])

    ax.set(**{'xlabel': labels[0] + r'(${^o}$C)', 'ylabel': labels[1]})
    ax2.set_ylabel(labels[3])
    ax3.set_ylabel(labels[2])
    ax4.set_ylabel(labels[4])

    ax.yaxis.label.set_color(p1.get_color())
    ax.tick_params(axis='y', colors=p1.get_color())
    
    ax2.tick_params(axis='y', colors=p2.get_color())
    ax2.yaxis.label.set_color(p2.get_color())
    
    ax3.tick_params(axis='y', colors=p3.get_color())
    ax3.yaxis.label.set_color(p3.get_color())
    
    ax4.tick_params(axis='y', colors=p4.get_color())
    ax4.yaxis.label.set_color(p4.get_color())

    lines = [p1, p2, p3, p4]
    ax.legend(lines, [l.get_label() for l in lines], bbox_to_anchor=(0.8, 1.0, 0.2, 0.1), ncol=2)
    fig.savefig('{}/fig8'.format(save_dir), dpi=300)

