# haha
# time:2024/12/5 13:37
import tushare as ts

class Data:
    def __init__(self):
        ts.set_token('85ca420b173fecf79e62c97d8ebb7cdc8df4d7b5a1ecaed9eedce247')
        pro = ts.pro_api()
        self.df = pro.daily(ts_code='000001.SZ', start_date='20230101', end_date='20231231')
        self.len = len(self.df)

    def getPassdata(self,start_data,days):
        temp = self.len - 1
        sum = 0
        while(temp >= 0):
            if self.df.iloc[temp]["trade_date"] >= start_data:
                break
            temp -= 1
        if start_data == self.df.iloc[temp]["trade_date"]:
            str1 = self.df.iloc[temp+1:self.len]
        else:str1 = self.df.iloc[temp:self.len]
        if len(str1) < days:
            #print(f"不足{days}天")
            return 0
        else:
            for i in range(days):
                #print(str1.iloc[i]["close"])
                sum += str1.iloc[i]["close"]
        return sum / days

    def getClose(self,date):
        for i in range(len(self.df)):
            if date == self.df.iloc[i]["trade_date"]:
                return self.df.iloc[i]["close"]







