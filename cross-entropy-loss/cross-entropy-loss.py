import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)
    ce = -np.mean(np.log(y_pred[np.arange(n), y_true]))
    return ce