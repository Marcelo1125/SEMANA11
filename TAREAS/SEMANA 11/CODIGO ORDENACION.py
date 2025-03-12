matriz =[
    [90, 80, 70],
    [21, 50, 40],
    [10, 20, 30]
]
def matriz_a_lista(matriz):
    return [num for fila in matriz for num in fila]
def lista_a_matriz(lista):
    return [lista[i:i+3] for i in range(0, 9, 3)]
def boole_sort(lista):
    n = len(lista)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n-1):
            if lista[i]> lista[i+1]:
                lista[i], lista[i + 1] = lista [i + 1], lista[i]
                ordenado = False
    return lista
print("matriz original:")
for fila in matriz:
     print(fila)
lista = matriz_a_lista(matriz)
lista_ordenada =boole_sort(lista)
matriz_ordenada = lista_a_matriz(lista_ordenada)
print("/nmatriz ordenada:")
for fila in matriz_ordenada:
    print(fila)
