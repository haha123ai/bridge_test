# haha
# time:2024/12/5 18:22
from backtest.post import Post
from backtest.data import Data

class Get:
    def __init__(self,po):
        self.data = Data()
        self.post = po
        self.revenue = 0
        self.revList = []

    def get(self):
        str2 = self.post.post()
        print(str2)
        for i in range(len(self.post.str)):
            start_date = self.post.str[i][0]
            end_date = self.post.str[i][2]
            right_money = self.post.str[i][1]

            first_price = self.data.getClose(start_date)
            last_price = self.data.getClose(end_date)

            self.revenue = int(right_money * (last_price - first_price))
            self.revList.append(self.revenue)

        for i in self.revList:
            print(i)
        return self.revList




