# import time

# nums = list(range(10_000_000))

# start = time.time()

# result = [x + 1 for x in nums]

# end = time.time()
# print("List time:", end - start)


import numpy as np
import time

nums = np.arange(1_000_000)

start = time.time()

result = nums * 2

end = time.time()

print("NumPy time:", end - start)