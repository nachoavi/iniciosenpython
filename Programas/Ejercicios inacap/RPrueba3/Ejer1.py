def tabla():
    x=0
    mul=10
    sum=0
    while x < 10:
        x=x+1
        re=x*mul
        print(mul,"*",x,re)
        sum=sum+re
    return sum

print("La suma de los multiplos es: ",tabla())

    