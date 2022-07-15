import numpy as np

num=np.array([1,2,3,4,5,6,7,8,9,10])

for i in range(1,num.size+1):
    print(num[-i])