import numpy as np
import time
matrix1=np.array([[1,2,3]
              ,[3,4,5]
              ,[4,5,6]])
matrix3=np.array([[1,2,3]
              ,[3,4,5]
              ,[4,5,6]])
print(matrix1)

print(matrix1*matrix3)
ma1=matrix1.flatten()
print(ma1)
ma2=matrix1.ravel()
print(ma2)


matrix2=np.zeros((4,5),dtype = np.int32)

print(matrix2)

sub_max1=matrix1[1:3,0:2]
print(sub_max1)
sub_max1[0:2,0:2]=999
print(sub_max1)

print(matrix1)

matrix2[0:3,0:2]=np.array([[12,23],
                  [34,56]
                  ,[45,67]])
print(matrix2)
matrix2[0:3,0:2]=np.array([12,23])
print(matrix2)
arr2=np.array([1,2,3,-1,-2,-3,-4,5,6,7])
print(arr2)
abs_arr2=arr2[arr2>=0]
print(abs_arr2)

sum_1=matrix1.sum(axis=1)
print(sum_1)

sum_0=matrix1.sum(axis=0)
print(sum_0)

ai_output=np.array([[[42]]])
print(ai_output,ai_output.shape)
result1=np.squeeze(ai_output)
print(result1,result1.shape)