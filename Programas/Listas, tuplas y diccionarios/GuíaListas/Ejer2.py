num=[1,2,3,4,5,6,7,8,9,10]

for i in range(1,len(num)):
    for j in range(len(num) - i):
        if num[j] < num[j+1]:
            temp=num[j]
            num[j] = num[j+1]
            num[j+1] = temp
print(num)
