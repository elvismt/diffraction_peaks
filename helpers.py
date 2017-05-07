import pandas as pd
from collections import OrderedDict
import os, json

def load_data():
    data = OrderedDict()
    for fname in os.listdir('data'):
        if fname.endswith('.json'):
            with open(os.path.join('data', fname), 'r') as f:
                js = json.load(f)
            data[js['name']] = pd.DataFrame({
                'x': js['x'], 'y': js['y']})
    return data

import math
import numpy as np
import matplotlib.pyplot as plt

def plot_grid(nrows, ncols, nplots=None):
    if nplots is None:
        nplots = nrows * ncols
    fig, axs = plt.subplots(nrows, ncols, figsize=(15,8))
    plt.subplots_adjust(hspace=0.4)
    if nplots % 2 != 0:
        fig.delaxes(axs[-1][-1])
    return fig, axs
