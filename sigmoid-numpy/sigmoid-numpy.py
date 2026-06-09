import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Writode here
    #x = np.asarray(x, dtype = float)
    return 1/(1+np.exp(-np.array(x)))
    