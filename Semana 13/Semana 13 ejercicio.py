def calcular_promedio_semanal_y_ciudad(datos):
    """
    Calcula el promedio de temperatura por semana y por ciudad.

    :param datos: Diccionario con los nombres de las ciudades como claves
                  y una lista de listas donde cada sublista representa las temperaturas semanales.
    :return: Diccionario con promedios por ciudad y promedios semanales por ciudad.
    """
    resultados = {}
    for ciudad, temperaturas_semanales in datos.items():
        promedios_semanales = {
            f"Semana {i+1}": sum(semana) // len(semana)  # Promedio de cada semana
            for i, semana in enumerate(temperaturas_semanales)
        }
        promedio_ciudad = sum(promedios_semanales.values()) // len(promedios_semanales)  # Promedio total de la ciudad
        resultados[ciudad] = {
            "promedio_ciudad": promedio_ciudad,
            "promedios_semanales": promedios_semanales
        }
    return resultados


# Ejemplo de datos: Temperaturas organizadas por ciudad y por semanas
datos_temperaturas = {
    "Ibarra": [[21, 22, 23], [20, 21, 22], [19, 20, 21], [22, 23, 24]],
    "Guayaquil": [[18, 19, 20], [19, 18, 17], [20, 21, 19], [17, 18, 20]],
    "Cuenca": [[25, 26, 24], [24, 25, 26], [26, 25, 27], [23, 24, 25]]
}

resultados = calcular_promedio_semanal_y_ciudad(datos_temperaturas)

# Muestra los resultados
for ciudad, info in resultados.items():
    print(f"{ciudad}:")
    print(f"  Promedio de la ciudad: {info['promedio_ciudad']} °C")
    for semana, promedio in info['promedios_semanales'].items():
        print(f"  {semana}: {promedio} °C")

