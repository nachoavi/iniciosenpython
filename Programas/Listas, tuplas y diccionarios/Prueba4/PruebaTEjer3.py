nums=(6,4,8,9,10)
x=0
for i in range(0,len(nums)):
    if nums[i] %2==0:
        x=x+1
        print(nums[i])
print("La cantidad de numeros pares encontrados fueron: ",x)