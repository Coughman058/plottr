from matplotlib import cycler

config = {
    'matplotlibrc': {
        'axes.grid': True,
        'axes.prop_cycle': cycler('color', ['1f77b4', 'ff7f0e', '2ca02c', 'd62728', '9467bd', '8c564b',
                                            'e377c2', '7f7f7f', 'bcbd22', '17becf']),
        'figure.dpi': 150,
        'figure.figsize': (4.5, 3),
        'font.size': 6,
        'font.family': ['Helvetica', 'Arial', 'DejaVu Sans', 'Bitstream Vera Sans'],
        'grid.linewidth': 0.5,
        'grid.linestyle': '--',
        'image.cmap': 'magma',
        'legend.fontsize': 6,
        'legend.frameon': True,
        'legend.numpoints': 1,
        'legend.scatterpoints': 1,
        'lines.marker': 'o',
        'lines.markersize': '3',
        'lines.markeredgewidth': 1,
        'lines.markerfacecolor': 'w',
        'lines.linestyle': '-',
        'lines.linewidth': 1,
        'savefig.dpi': 300,
        'savefig.transparent': False,
    },

}
