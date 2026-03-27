import numpy as np
array1=np.array([[1,2,3],[4,5,6]],dtype=np.int32)
print(f"新建数组shi{array1}")
array_empty=np.empty((4,5))
print(f"新建空白数组为{array_empty}")
array_zero=np.zeros((6,5))
print(f"新建0数组为{array_zero}")
array_one=np.ones((6,8))
print(f"新建全1数组为{array_one}")

array_arange=np.arange(1,9,2)
print(f"新建跳跃数组为{array_arange}")
array_linspace=np.linspace(0,10,5)
print(f"新建等取点数组为{array_linspace}")

print(f"数组array1的维度是{array1.ndim}")
print(f"数组array1的形状是{array1.shape}")
print(f"数组array1的大小是{array1.size}")
print(f"数组array1的格子大小为{array1.dtype}")
print(f"判断底层array1 C语言的连续性{array1.flags['C_CONTIGUOUS']}")

matrix=np.ones((5,3),dtype=np.int32)
print(f"新建矩阵步幅为{matrix.strides}")

matrix_T=matrix.T
print(f"转置之后的矩阵步幅为{matrix_T.strides}")
print(f"转置矩阵的形状为{matrix_T.shape},大小为{matrix_T.size}")