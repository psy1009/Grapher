import numpy as np

def as_array(object):
    if isinstance(object, np.ndarray):
        return object
    return np.array(object)
