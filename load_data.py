"""Module allow for us to load data."""

import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def load_csv_data(filename: str, reverse: bool=False) -> pd.DataFrame:
    """Load csv data and return a dataframe."""

    filepath = os.path.join(os.curdir, "data", filename)
    logger.info(f"Working on loading datafile {filepath}")
    data = pd.read_csv(filepath)
    logger.info(f"Succesfully loaded csv file, {data.shape[0]} rows and {data.shape[1]} columns")

    if reverse:
        data = data.iloc[::-1]
        data = data.reset_index()
        data = data.drop("index", axis=1)
        
    return data