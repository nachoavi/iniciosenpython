def factorial(a):
    multiplicador = 1
    for i in range(a):
        multiplicador *= i+1
    return multiplicador

print(factorial(4))


