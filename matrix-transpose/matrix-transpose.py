import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    n,m = A.shape
    b = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            b[i,j] = A[j,i]
    return b
