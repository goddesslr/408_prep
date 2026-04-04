import pandas as pd
import numpy as np
import sys

df1=pd.DataFrame({'A':[10,20,30,np.nan],'B':[20,np.nan,56,70]})

print(df1)
mask=df1.isna()

print(mask)
mean_A=df1['A'].mean()

df1.fillna(value=mean_A,inplace=True)
print(df1)

sc1=pd.DataFrame({'name':['A','B','C','D'],'scores':[90,89,76,98]})
sc2=pd.DataFrame({'name':['A','B','F','G'],'Age':[19,20,18,17]})
print(sc1)
print(sc2)

sc12=pd.concat([sc1,sc2],axis=0,ignore_index=True)
sc123=pd.concat([sc1,sc2],axis=1)
print(sc12)
print(sc123)

mer1=pd.merge(left=sc1,right=sc2,how='inner',on = 'name')
mer2=pd.merge(left=sc1,right=sc2,how='left',on='name')
mer3=pd.merge(left=sc1,right=sc2,how='right',on = 'name')
mer4=pd.merge(left=sc1,right=sc2,how='outer',on = 'name')
mer5=pd.merge(left=sc1,right=sc2,on = 'name')
print(mer1)
print(mer2)
print(mer3)
print(mer4)
print(mer5)

data = {
    'Date': ['2023-01-15', '2023-01-20', '2023-02-10', '2023-02-25', '2023-01-05', '2023-02-18'],
    'Region': ['East', 'East', 'West', 'West', 'North', 'East'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Apple'],
    'Revenue': [100, 150, 200, 300, 120, 180]
}
df = pd.DataFrame(data)

print(df)

sum_region=df.groupby('Region')['Revenue'].agg(['sum','mean'])
print(sum_region)

s1=pd.Series({'A':12,'B':34,'C':56},dtype=np.int32)
s2=pd.Series({'V':22,'B':23,'N':66},dtype=np.int32)
s3=s1+s2
s4=s1.add(s2,fill_value=0)
print(s3)
print(s4)