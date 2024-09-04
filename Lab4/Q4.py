import numpy as np
A = np.random.rand(20)
A = (A - np.percentile(A, 25)) / (np.percentile(A, 75) - np.percentile(A, 25))
print(A)