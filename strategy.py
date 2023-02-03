"""Modules contain all our strategies."""

from typing import Dict, Tuple
import pandas as pd
from basic_indicators import simple_moving_average

class StrategyBase:

    def __init__(self):
        pass

    def next(self) -> int:
        pass


class MovingAverageCrossOver(StrategyBase):

    def __init__(self, data: pd.DataFrame, slow: int=10, fast: int=5, type: str="simple"):
        self.data = data
        self.slow = slow
        self.fast = fast
        self._fast_curr_pos = None

        self.data["SLOW"] = simple_moving_average(self.data["CLOSE"], slow)
        self.data["FAST"] = simple_moving_average(self.data["CLOSE"], fast)

    
    def next(self) -> Tuple[int, int]:

        length = len(self.data)

        self._fast_curr_pos = self._currpos(self.slow)

        for i in range(self.slow+1, length):
            newPos = self._currpos(i)

            if newPos == self._fast_curr_pos:
                self._fast_curr_pos = newPos
                yield i, 0
            elif (self._fast_curr_pos == "below") and (newPos == "above"):
                self._fast_curr_pos = newPos
                yield i, 1
            else:
                self._fast_curr_pos = newPos
                yield i, -1

    
    def _currpos(self, pos: int):
        if self.data["FAST"].iloc[pos] < self.data["SLOW"].iloc[pos]:
            return "below"
        
        else:
            return "above"
        
