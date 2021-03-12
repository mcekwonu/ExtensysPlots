import os


def is_exist_dir(dirpath):
    try:
        os.makedirs(dirpath)
    except OSError:
        pass


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
