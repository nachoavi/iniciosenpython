#Almacenar en una tupla numeros aleatorios, negativos, positivos, pares e impares y ceros
#Despues mostrar ordenados es una lista correspondiente para los negativos, positivos, pares, impares e ceros
 
nums=(-2,3,5,2,0,-3,0)

print("Positivos: ")
for i in range(0,len(nums)):
    if nums[i] > 0:
        print(nums[i])

print("\nNegativos: ")
for i in range(0,len(nums)):
    if nums[i] < 0:
        print(nums[i])

print("\nPares: ")
for i in range(0,len(nums)):
    if nums[i] %2==0 and nums[i] != 0:
        print(nums[i])

print("\nImpares: ")
for i in range(0,len(nums)):
    if nums[i] %2==1:
        print(nums[i])

print("\nCeros: ")
for i in range(0,len(nums)):
    if nums[i] == 0:
        print(nums[i])