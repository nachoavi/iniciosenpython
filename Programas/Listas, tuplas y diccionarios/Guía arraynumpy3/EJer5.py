import numpy as np

nums=np.array([10,4,3,6,1,2])

for i in range(1,nums.size):
    for j in range(nums.size-i):
        if nums[j] > nums[j+1]:
            aux=nums[j]
            nums[j] = nums[j+1]
            nums[j+1]=aux
print(nums)