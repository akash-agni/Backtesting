"""Module allows us to build basic indicators for analysis."""

import numpy as np
import pandas as pd

def simple_moving_average(trend: pd.Series, periods: int=5) -> pd.Series:
    """Module calculates the simple moving average of a given series and return as pandas series"""

    queue = []
    result = []
    curr_sum = 0
    size = len(trend)
    for i in range(0, size):
        if len(queue) < periods:
            queue.append(trend.iloc[i])
            curr_sum += trend.iloc[i]
            result.append(0)
        else:
            curr_sum -= queue.pop()
            curr_sum += trend.iloc[i]
            queue.append(trend.iloc[i])
            result.append(curr_sum/periods)
    
    return pd.Series(result)