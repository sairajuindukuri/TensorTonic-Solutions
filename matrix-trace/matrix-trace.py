import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A, dtype = float)
    m = A.shape[0]
    l = []
    for i in range(m):
        l.append(A[i,i])
    return np.sum(np.array(l)) 
        
    
