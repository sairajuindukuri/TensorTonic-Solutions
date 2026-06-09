import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    #return np.maximum(np.array(x), alpha*np.array(x))
    return np.where(np.array(x, dtype =float)>=0, np.array(x), alpha*np.array(x))