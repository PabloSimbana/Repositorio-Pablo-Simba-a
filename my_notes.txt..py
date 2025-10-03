# -----------------------------------------------
# Escritura y lectura de archivos en Python
# Autor: [Tu Nombre]
# Asignatura: [Nombre de la asignatura]
# -----------------------------------------------

# Escritura de un archivo de texto
# Creamos (o sobreescribimos si ya existe) un archivo llamado my_notes.txt
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Nota 2: Estoy practicando las funciones write() y readline().\n")
    file.write("Nota 3: Es importante cerrar los archivos después de usarlos.\n")

# Lectura de un archivo de texto
# Abrimos el archivo en modo lectura
with open("my_notes.txt", "r") as file:
    # Leemos el contenido línea por línea utilizando readline()
    linea = file.readline()
    while linea:
        print(linea.strip())  # strip() elimina los saltos de línea extra
        linea = file.readline()

# Nota: Al usar 'with open()', el archivo se cierra automáticamente
# cuando se sale del bloque, por lo que no es necesario usar file.close().
