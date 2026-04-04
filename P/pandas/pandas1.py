import numpy as np
import pandas as pd

s1=pd.Series(data=[1,2,3],index=['a','b','c'])
print(s1)

in1={'d':3,'f':4,'g':5}
s2=pd.Series(in1)
print(s2)
data1={'name':['a','b','c'],'Age':[23,34,21],'scores':[90,89,67]}
df1=pd.DataFrame(data1)
print(df1)

#定义一个陷阱数据框架
df_trap=pd.DataFrame({'value':[100,200,300,400]},index=[1,2,0,4])
re_iloc=df_trap.iloc[0:2]
re_loc=df_trap.loc[2:0]
print(re_iloc)
print(re_loc)