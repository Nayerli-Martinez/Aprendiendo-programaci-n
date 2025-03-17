#Metodo bubble_sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz 3x3 con valores numéricos
matriz = [
    [45, 40, 35],
    [30, 25, 20],
    [15, 10, 5]
]
#Matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar de forma ascendente la segunda fila (fila índice)
fila_a_ordenar = 1
bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz)
