#Crear un programa en que un usuario ingrese 10 numero, 
# y se muestre por pantalla el numero mayor, menor y su suma y resta

nums=[]
for i in range(0,10):
    nums.append(int(input(f"Ingrese el numero {i}: ")))
    if i == 0:
        nmayor=nums[i]
        nmenor=nums[i]
    elif nums[i] > nmayor:
        nmayor=nums[i]
    elif nums[i] < nmenor:
        nmenor=nums[i]
s=nmayor+nmenor
print("El numero mayor es: ", nmayor)
print("El numero menor es: ", nmenor)
print("La suma de las variables es: ",s)
        