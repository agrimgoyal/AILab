import numpy as np
def relu(x):
    return np.maximum(0, x)
r10 = relu(10)
print(r10)