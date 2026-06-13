import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.array(v)
    n = v.shape[0]
    p = np.zeros((n,n))
    for i in range(n):
        p[i,i] = v[i]

    return p
    
