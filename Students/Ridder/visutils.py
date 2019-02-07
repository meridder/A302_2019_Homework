"""

This module contains two functions that will load and display magnitude
data. The resolution (gridsize) can be manipulated.

"""

from astropy.table import QTable
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

def load_and_prepare_cmd(filename):
    """
    This function reads in a csv file, constrains g and g-r, then 
    outputs the two values as arrays.
    """
    table = QTable.read(filename)
    table = table[np.where((table['g'] > 14) & (table['g'] < 24))]
    table['g-r'] = table['g'] - table['r']
    table = table[np.where((table['g-r'] > -0.5) & (table['g-r'] < 2.5))]
    g = np.array(table['g'])
    gr = np.array(table['g-r'])
    return g, gr

def interactive_hess(g, gr):
    """
    Takes two arrays and creates an interactive plot with a default
    gridsize of 100.
    """
    def plot(g, gr, grd = 100):
        plt.hexbin(gr, g, gridsize = grd, bins = 'log', cmap = 'inferno')
        plt.show()
    interact(plot, g = fixed(g), gr = fixed(gr), grd = (50, 300, 1), continuous_update = False)
