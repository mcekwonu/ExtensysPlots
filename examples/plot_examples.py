"""Plot examples of OriginproPlot style."""

import os
import numpy as np
import matplotlib.pyplot as plt


def is_exist_dir(dirpath):
    try:
        os.makedirs(dirpath)
    except OSError:
        pass
    else:
        print(f'{dirpath} successfully created!')


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


def g(x, m, L=10):
    return np.cosh(m*(L-x)) / np.cosh(m*L)


save_dir = os.path.join(os.path.dirname(__file__), 'figures')
is_exist_dir(save_dir)

# markers = ['o', 'v', '^', '<', 's', 'd', '>', 'x', 'D', '+', 'p', '*']
pparams = dict(xlabel='fractional distance into pore\n$x/L$', ylabel='Concentration $(mol.dm^{-3})$')

x = np.linspace(0, 1, 301)

with plt.style.context(['originpro']):
    fig, ax = plt.subplots()
    for m in [0.1, 0.5, 1.0, 2, 2.5, 5.0]:
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.75, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig1'.format(save_dir))


with plt.style.context(['originpro']):
    fig, ax = plt.subplots()
    for m in [1, 5, 10, 20, 25, 50]:
        ax.plot(x, g(x, m), label='m = ' + str(m))
    ax.set(**pparams)
    ax.grid(True)
    ax.legend(bbox_to_anchor=(0.75, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig2'.format(save_dir))


with plt.style.context(['originpro']):
    fig, ax = plt.subplots()

    ax2 = ax.twinx()

    for r in [1, 5, 10, 20, 25, 50]:
        ax.plot(x, g(x, r), label='rate = ' + str(r))
        ax2.plot(x, g(x, r)-1, label='rate = ' + str(r))
    ax.set(**pparams)
    ax.legend(bbox_to_anchor=(0.8, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig3'.format(save_dir))


# multiple y-axis
with plt.style.context(['originpro']):
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    ax2 = ax.twinx()

    for r in [1, 5, 10, 20, 25, 50]:
        p1, = ax.plot(x, g(x, r), color='red', label='rate = ' + str(r))
        p2, = ax2.plot(x, 2*g(x, r), color='brown', label='rate = 2' + str(r))

    ax.set(**pparams)
    ax.yaxis.label.set_color(p1.get_color())
    ax.tick_params(axis='y', colors=p1.get_color())
    ax.yaxis.label.set_color(p2.get_color())
    ax2.tick_params(axis='y', colors=p2.get_color())

    lines = [p1, p2]
    #ax.legend(lines, [l.get_label() for l in lines], bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    ax.legend(bbox_to_anchor=(0.6, 1.0, 0.2, 0.1), ncol=3)
    fig.savefig('{}/fig4'.format(save_dir))
    fig.show()

