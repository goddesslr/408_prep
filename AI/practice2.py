import numpy as np

class LogisticRegression:
    def __init__(self,learning_rate=0.01,max_iter=1000):
        self.lr= learning_rate
        self.max_iter=max_iter
        self.W=None
        
    def _sigmoid(self,z):
        z=np.clip(z,-250,250)
        return 1.0/(1.0+np.exp(-z))
    
    def _compute_loss(self,Y_pred,Y):
        N=Y.shape[0]
        
        ep=1e-15
        Y_pred=np.clip(Y_pred,ep,1-ep)
        loss=-(1/N)*np.sum(Y*np.log(Y_pred)+(1-Y)*np.log(1-Y_pred))
        return loss
    
    def fit(self,X,Y):
        N,d=X.shape
        X_b=np.hstack([np.ones((N,1)),X])
        self.W=np.zeros((d+1,1))
        loss_history=[]
        
        for i in range(self.max_iter):
            Z=X_b@self.W
            Y_pred=self._sigmoid(Z)
            loss_history.append(self._compute_loss(Y_pred,Y))
            
            error=Y_pred-Y
            dw=(1/N)*(X_b.T@error)
            self.W -= self.lr*dw
            
        return loss_history
    
    def predict(self,X_new):
        N_new=X_new.shape[0]
        X_new_b=np.hstack([np.ones((N_new,1)),X_new])
        prob=self._sigmoid(X_new_b@self.W)
        
        return (prob>=0.5).astype(int)

N_samples,n_features=200,3

X_data=np.random.randn(N_samples,n_features)
Y_data=(np.sum(X_data,axis=1)>0).astype(int).reshape(-1,1)

clf=LogisticRegression(learning_rate=0.01,max_iter=500)
loss_record=clf.fit(X_data,Y_data)

pre=clf.predict(X_data[:100])

print(Y_data[:100].flatten())
print(pre[:100].flatten())               