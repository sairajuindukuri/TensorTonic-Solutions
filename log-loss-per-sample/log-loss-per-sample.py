import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_true = np.array(y_true, dtype=float)
    p = np.array(y_pred, dtype=float)
    p_clipped = np.clip(p, eps, 1 - eps)
    loss = - (y_true * np.log(p_clipped) + (1 - y_true) * np.log(1 - p_clipped))
    return loss.tolist()