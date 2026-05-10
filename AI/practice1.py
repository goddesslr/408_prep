import numpy as np
import matplotlib.pyplot as plt

#模拟数据
np.random.seed(272)
data_size=100

x=np.random.uniform(low=1.0,high=10,size=data_size)
y=20*x + 10 + np.random.normal(loc=0.0,scale=10.0,size=data_size)

shuffed_index=np.random.permutation(data_size)

x,y= x[shuffed_index],y[shuffed_index]

split_index=int(data_size*0.7)
x_train,y_train=x[:split_index],y[:split_index]
x_test,y_test=x[split_index:],y[split_index:]

#使用面向对象编程编写回归模型

class LinearRegression1D:
    def __init__(self,learning_rate=0.01,max_iter=10,seed=314):
        self.lr=learning_rate
        self.max_iter=max_iter
        self.seed=seed
        self.w=None
        self.b=None
    
    def fit(self,x,y):
        np.random.seed(self.seed)
        self.w=np.random.normal(loc=0.0,scale=1.0)
        self.b=np.random.normal(loc=0.0,scale=1.0)
        
        for i in range(self.max_iter):
            y_pred=self.w*x+self.b
            
            dw=np.mean((y_pred-y)*x)*2
            db=np.mean((y_pred-y))*2
            
            self.w -= self.lr*dw
            self.b -= self.lr*db
            
    def predict(self,x):
        return self.w*x+self.b
    
regr=LinearRegression1D(learning_rate=0.01,max_iter=10)
regr.fit(x_train,y_train)

def show_data(x_data,y_data,w,b):
    plt.scatter(x_data,y_data,marker='.',c="red",label='Real data')
    plt.plot(x_data,w*x_data+b,c='blue',linewidth=2,label='Fitted Line')
    
    plt.legend()
    save_path="LinearRegression1D_result.png"
    plt.savefig(save_path,dpi=300,bbox_inches='tight')
    plt.show()

print(f"训练结束 w={regr.w:.2f},b={regr.b:.2f}")
show_data(x_train,y_train,regr.w,regr.b)

        
        
    
        
        
    
