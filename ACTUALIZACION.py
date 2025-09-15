import random
import statistics

def calcular_promedio_ciudades(matriz, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad a lo largo de todas las semanas.

    Parámetros:
        matriz (list): Lista 3D con las temperaturas en el formato [ciudad][semana][día].
        ciudades (list): Lista con los nombres de las ciudades en el mismo orden que la matriz.

    Retorna:
        dict: Un diccionario donde la clave es la ciudad y el valor es el promedio de temperaturas.
    """
    promedios = {}
    for i, ciudad in enumerate(ciudades):
        # Aplanar todas las semanas de la ciudad en una sola lista de días
        todas_temperaturas = [temp for semana in matriz[i] for temp in semana]
        promedios[ciudad] = statistics.mean(todas_temperaturas)
    return promedios


# ------------------------
# Ejemplo de uso
# ------------------------
ciudades = ["Madrid", "Barcelona", "Valencia"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz = [
    [[random.randint(10, 35) for _ in dias_semana] for _ in range(num_semanas)]
    for _ in ciudades
]

# Calcular promedios
promedios = calcular_promedio_ciudades(matriz, ciudades)

# Mostrar resultados
print("\nPromedio de temperaturas por ciudad:")
for ciudad, promedio in promedios.items():
    print(f"  {ciudad}: {promedio:.2f} °C")
