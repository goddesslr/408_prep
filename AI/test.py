def elementwise_product(x, y):
    # 补全该函数
	return x.value()*y.value()

x, y = [[1,2,3], [2,3,1], [3, 1, 2]], [[1,0,0], [0,1,0], [0,0,1]]
print(elementwise_product(x, y))