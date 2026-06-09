import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    arr = np.array(x, dtype = float)
    return arr * 1/(np.exp(-arr)+1)