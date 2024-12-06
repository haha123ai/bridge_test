# haha
# time:2024/12/5 16:42
from backtest.data import Data

class Post:
    def __init__(self,baseMoney,pen):
        self.baseMoney = baseMoney
        self.pen = pen
        self.runMoney = 0
        self.str = []


    def post(self):
        da = Data()
        #print(da.df["trade_date"])
        i = len(da.df) - 1
        while(i >= 0):
            cyclicality = []
            right_date = da.df.iloc[i]["trade_date"]
            passTsix = da.getPassdata(right_date,26)
            passTwo = da.getPassdata(right_date,12)
            if passTwo != 0 and passTsix != 0 and passTwo > passTsix:
                cyclicality.append(right_date)
                self.runMoney = self.baseMoney * self.pen
                self.baseMoney -= self.runMoney
                cyclicality.append(self.runMoney)
                q = i - 1
                while(q >= 0):
                    next_date = da.df.iloc[q]["trade_date"]
                    passTsix = da.getPassdata(next_date, 26)
                    passTwo = da.getPassdata(next_date, 12)
                    if passTwo != 0 and passTsix != 0 and passTwo < passTsix:
                        cyclicality.append(next_date)
                        break
                    q -= 1
                self.str.append(cyclicality)

            i -= 1

    def getRestult(self):
        print(self.str)
        return self.str



