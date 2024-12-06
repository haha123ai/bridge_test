# haha
# time:2024/12/6 11:12
from backtest.data import Data
from backtest.get import Get
from backtest.post import Post

#输入本金，还有每次买入的部分
post = Post(1000000,0.2)
post.post()
post.getRestult() #获取每个周期，
'''
周期开始时间，买入的部分，周期结束时间
['20230516', 200000.0, '20230525']
'''

get = Get(post)
'''
显示的是一个列表，
每个值表示每个周期的收益情况'''
get.get()


