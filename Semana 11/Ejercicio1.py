#Matriz 3x3x3 Arreglo Multidimencional.
matriz = [
    [[10, 11, 12], [13, 14, 15],[16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]]
]

# Valor que queremos encontrar
valor_a_encontrar = 84
encontrado = False

# Encontrar el número en la matriz 3D
for i, capa in enumerate(matriz):
    for j, fila in enumerate(capa):
        for k, elemento in enumerate(fila):
            if elemento == valor_a_encontrar:
                print(f"El número {valor_a_encontrar} encontrado en la capa {i}, fila {j}, columna {k}")
                encontrado = True
                break
        if encontrado:
            break
    if encontrado:
        break
#Mensaje
if not encontrado:
    print(f"El número {valor_a_encontrar} no se encuentra en la matriz")