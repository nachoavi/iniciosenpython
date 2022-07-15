import numpy as np

num=np.array([1,2,3,4,5,6,7,8,9,10])

for i in range(1,num.size):
    for j in range(num.size - i):
        if num[j] < num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp
print(num)
