import numpy as np  

li = np.array(input().split(" "), dtype=np.int)
li[0], li[1] = li[1], li[0]
li[0], li[2] = li[2], li[0]

print(li[0], li[1], li[2])