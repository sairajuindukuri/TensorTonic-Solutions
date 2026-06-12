import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.array(X, float)
    y = np.array(y, float)
    m,n = X.shape
    b = 0.0
    w = np.zeros(n)
    for _ in range(steps):
        alpha = np.dot(X,w) + b
        y1 = _sigmoid(alpha)
        gw = np.dot(X.T, (y1-y))/m
        gb = np.sum(y1-y)/m
        w -= lr*gw
        b -= lr*gb

    return w,b
        
    
    