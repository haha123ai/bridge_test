#### data
获取tushare中的数据：  
ts_code='000001.SZ', start_date='20230101', end_date='20231231'  
选定平安银行的数据，开始时间是20230101，结束时间是20231231  
getPassdata方法：是获取start_data之前days的平均close  


#### post方法
传入两个参：  
baseMoney：本金  
pen：每次使用的百分比  

getRestult:  
获取周期的方法,结果以矩阵形式呈现。  
['20230516', 200000.0, '20230525']  
周期开始时间，买入的部分，周期结束时间

#### get方法  
显示每个post对应周期的收益情况  
每个值表示每个周期的收益
