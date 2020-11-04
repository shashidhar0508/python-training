import time
import numpy as np

SIZE = 1000000

L1, L2 = range(SIZE), range(SIZE)
A1, A2 = np.arange(SIZE), np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time() - start) * 1000)

start = time.time()
result = A1 + A2
print((time.time() - start) * 1000)
