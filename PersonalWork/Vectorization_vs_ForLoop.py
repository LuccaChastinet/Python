# Explanation to why using vectorization is better than for loops (it takes less time to complete the task given)

import numpy as np
import time

# Vectorization ->

a = np.random.rand(1000000) # Random 1 million numbers
b = np.random.rand(1000000) # Random 1 million numbers

tic = time.time() # Tic and Toc used to calculate the time for the operation

c = np.dot(a,b) # Vectorization used here

toc = time.time()

print(c) # Demonstration that both approaches to the problem give the same results

print("Vectorized version:" + str(1000*(toc-tic))+ "ms")

# For loop ->

c = 0
tic = time.time()

for i in range(1000000):
  c += a[i]*b[i]

toc = time.time()

print(c)
print("For loop:" + str(1000*(toc-tic))+ "ms")
