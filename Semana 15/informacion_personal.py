# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Nayerli Martinez",  # Nombre
    "edad": 19,  # Edad
    "ciudad": "Ibarra",  # Ciudad
    "profesion": "Estudiante"  # Profesión
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Atuntaqui"  # Nueva ciudad asignada

# Verificar si la clave "telefono" existe. Si no existe, agregarla.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989627052"  # Número

# Eliminar la clave "edad", ya que no es necesaria
informacion_personal.pop("edad", None)  # Eliminar la clave de forma segura

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)

# Resultado esperado:
# {
#   'nombre': ' Nayerli Martinez',
#   'ciudad': 'Atuntaqui',
#   'profesion': 'Estudiante',
#   'telefono': '0989627052'
# }