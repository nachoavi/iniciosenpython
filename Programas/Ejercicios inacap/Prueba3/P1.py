def tabla():
    mul=0
    summulti=0
    for x in range (1,11):
        mul=10*x
        summulti=summulti+mul
        print("10 * ",x," = ", mul)   
    return summulti

print("La suma de los multiplos es: ",tabla())



        