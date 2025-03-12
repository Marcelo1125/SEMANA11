matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_numero(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return True, (i,j)
    return False, none, none
numero_a_buscar = 5
encontrado, posicion = buscar_numero(matriz, numero_a_buscar)
if encontrado:
    print(f"El numero {numero_a_buscar} se encontro en la posicion {posicion}")
else:
        print(f"El numero {numero_a_buscar} no se encuentra en la matriz.")

