def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    import numpy as np
    # Write code here
    arr = np.array(x, dtype = float)
    return np.where(arr>0, arr, alpha* (np.exp(arr)-1)).tolist()