"""Module allows us to build basic indicators for analysis."""

import numpy as np
import pandas as pd

def simple_moving_average(trend: pd.Series, periods: int=5) -> pd.Series:
    """Module calculates the simple moving average of a given series and return as pandas series"""

    result = trend.rolling(window=periods).mean()
    
    return pd.Series(result)