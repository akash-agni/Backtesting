"""We use this module to build strategies"""

import pandas as pd
from strategy import StrategyBase

class StrategyRunner:

    def __init__(self, data: pd.DataFrame, strategy: StrategyBase, fund: int=100000, parallel: bool=True):
        self.data = data
        self.strategy = strategy
        self.fund = fund
        self.parallel = parallel
        self.fund_invested = 0
        self.units_owned = 0

    def run(self):

        signal_seq = []
        for pos, signal in self.strategy.next():
            signal_seq.append(signal_seq)
            if signal == 0:
                continue
            elif signal == 1:
                if self.parallel and (self.fund >= self.data["CLOSE"].iloc[pos]):
                    print(f"Buying a Unit at {self.data.iloc[pos].to_dict()}, current fund is {self.fund}")
                    self._buy(self.data["CLOSE"].iloc[pos])
                else:
                    print("No funds to buy")
            else:
                if self.fund_invested > 0:
                    print(f"Selling a Unit at {self.data.iloc[pos].to_dict()}, current fund is {self.fund}")
                    self._sell(self.data["CLOSE"].iloc[pos])
                else:
                    print("Nothing invested to sell.")


    def report(self) -> int:
        return self.fund + self.fund_invested
    
    def _buy(self, price) -> None:
        self.fund -= price
        self.fund_invested += price
        self.units_owned += 1

    def _sell(self, price) -> None:
        self.fund_invested -= price
        self.fund += price
        self.units_owned -= 1

