# Escritura de Archivo de Texto:
# Creamos un archivo llamado my_notes.txt y escribimos tres líneas de notas personales.

with open("my_notes.txt", "w") as file:
    file.write("Mi nombre es Nayerli Martinez.\n")
    file.write("Tengo 19 años .\n")
    file.write("Vivo en la provincia de Imbabura .\n")
# El archivo se cierra automáticamente al usar 'with'.

# Lectura de Archivo de Texto:
# Abrimos el archivo my_notes.txt y leemos su contenido línea por línea utilizando readline().
with open("my_notes.txt", "r") as file:
    line = file.readline()  # Leemos la primera línea usando readline().
    while line:  # Continuamos mientras haya contenido para leer.
        print(line.strip())  # Mostramos la línea eliminando el salto de línea.
        line = file.readline()  # Leemos la siguiente línea.

# Cierre de Archivos:
# No se requiere un cierre manual, ya que 'with' asegura que el archivo se cierre automáticamente.
