# Creamos una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión,
# días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 2

# Matriz 3D
temperaturas = [[[None for _ in range(len(dias))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Matriz con temperaturas (entre 15°C y 35°C)
import random
for ciudad_index in range(len(ciudades)):
    for semana in range(semanas):
        for dia_index in range(len(dias)):
            temperaturas[ciudad_index][semana][dia_index] = random.randint(15, 35)

# Mostrar temperaturas diarias y el promedio de temperaturas semana 1 y semana2 de cada ciudad
print("Temperaturas diarias y promedio por ciudad y semana:")
for ciudad_index, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        print(f"\nCiudad: {ciudad}, Semana {semana + 1}")
        temperaturas_semanales = temperaturas[ciudad_index][semana]
        for dia_index, temperatura in enumerate(temperaturas_semanales):
            print(f"  {dias[dia_index]}: {temperatura}°C")
        # Calcular el promedio
        promedio = sum(temperaturas_semanales) / len(temperaturas_semanales)
        print(f"Promedio semanal: {promedio:.2f}°C")

