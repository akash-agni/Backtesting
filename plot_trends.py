"""Module allows to plot trends quickly."""

import pandas as pd
import seaborn as sns
from typing import List
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def plot_multi_line_plots(data: pd.DataFrame, columns_to_plot: List[str], X_Col: str, Y_Col: str) -> plt.figure:
    figure = plt.figure(figsize=(16, 9))
    sns.set(style="darkgrid")

    for col_name, args in columns_to_plot.items():
        X = data[X_Col].iloc[args["skip_rows"]:]
        Y = data[col_name].iloc[args["skip_rows"]:]
        plt.plot(X, Y, figure=figure, label=col_name)
        plt.legend(col_name)

    return figure