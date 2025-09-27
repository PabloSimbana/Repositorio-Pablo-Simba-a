# Crear el diccionario inicial
informacion_personal = {
    "nombre": "David Simbaña",
    "edad": 19,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar o modificar la clave "profesion"
informacion_personal["profesion"] = "Ingeniero de Software"

# Verificar si existe la clave "telefono", si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "600-123-456"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)
