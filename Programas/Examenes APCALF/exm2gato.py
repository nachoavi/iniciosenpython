tablero=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)
    return True

def poner_ficha(tablero,x,y,ficha):
    if tablero[x-1][y-1] == " ":
        tablero[x-1][y-1] = ficha
    else:
        print("Esta coordenada ya esta siendo utilizada, use una que este libre.")
    return tablero

def final(tablero):
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != " ":
            return tablero[fila][0]
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != " ":
            return tablero[0][columna]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] !=" ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] !=" ":
        return tablero[0][2]
    
    for fila in tablero:
        if " " in fila:
            return ""
    return "EMPATE"

def pregunta_casilla():
    while True:
        x = int(input("Introduce la coordenada X del 1 al 3: "))
        y = int(input("Introduce la coordenada Y del 1 al 3: "))
        ficha = input("Introduce 0 para círculo o X para cruz: ")
    return