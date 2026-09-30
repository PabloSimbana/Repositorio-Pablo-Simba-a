import heapq
import os
import time

class SistemaVuelos:
    def __init__(self):
        # Estructura basada en listas de adyacencia (Diccionario anidado: {origen: {destino: costo}})
        self.grafo = {}

    def agregar_vuelo(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = {}
        self.grafo[origen][destino] = costo

    def cargar_desde_archivo(self, ruta_archivo):
        # Crea un archivo ficticio si no existe para simular la base de datos solicitada en la guía
        if not os.path.exists(ruta_archivo):
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write("Quito,Guayaquil,50\n")
                f.write("Quito,Bogota,120\n")
                f.write("Bogota,Lima,150\n")
                f.write("Guayaquil,Lima,200\n")
                f.write("Lima,Buenos Aires,400\n")
                f.write("Bogota,Buenos Aires,450\n")
        
        # Lectura de los datos desde el archivo de texto
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    origen, destino, costo = datos[0].strip(), datos[1].strip(), float(datos[2].strip())
                    self.agregar_vuelo(origen, destino, costo)
        print("[✔] Base de datos de vuelos cargada exitosamente desde el archivo.\n")

    def mostrar_reporteria(self):
        """Módulo de reportería para visualizar y consultar los elementos de la estructura de datos."""
        print("=" * 45)
        print("          REPORTERÍA DE LA RED DE VUELOS")
        print("=" * 45)
        if not self.grafo:
            print("La red de vuelos se encuentra vacía.")
            return
        
        contador = 1
        for origen, destinos in self.grafo.items():
            for destino, costo in destinos.items():
                print(f"[{contador}] Ruta Directa: {origen} ➔ {destino} | Costo: ${costo:.2f}")
                contador += 1
        print("=" * 45 + "\n")

    def buscar_vuelo_mas_barato(self, inicio, fin):
        """Algoritmo de Dijkstra para encontrar la ruta óptima de menor costo."""
        cola_prioridad = [(0, inicio, [inicio])]
        visitados = set()

        while cola_prioridad:
            costo_actual, actual, camino = heapq.heappop(cola_prioridad)

            if actual == fin:
                return costo_actual, camino

            if actual in visitados:
                continue
            visitados.add(actual)

            if actual in self.grafo:
                for vecino, peso in self.grafo[actual].items():
                    if vecino not in visitados:
                        heapq.heappush(cola_prioridad, (costo_actual + peso, vecino, camino + [vecino]))
        
        return float('inf'), []

# Bloque principal de ejecución de la actividad
if __name__ == "__main__":
    app_vuelos = SistemaVuelos()
    archivo_db = "vuelos_db.txt"
    
    # 1. Carga de datos
    app_vuelos.cargar_desde_archivo(archivo_db)
    
    # 2. Ejecución de la Reportería
    app_vuelos.mostrar_reporteria()
    
    # 3. Prueba de optimización y cálculo de ruta más barata
    origen_prueba = "Quito"
    destino_prueba = "Buenos Aires"
    
    print(f"Calculando la ruta más económica de '{origen_prueba}' a '{destino_prueba}'...")
    
    # Medición del tiempo de ejecución
    inicio_tiempo = time.perf_counter()
    costo_total, ruta_optima = app_vuelos.buscar_vuelo_mas_barato(origen_prueba, destino_prueba)
    fin_tiempo = time.perf_counter()
    
    tiempo_ejecucion_ms = (fin_tiempo - inicio_tiempo) * 1000

    print("\n" + "-" * 45)
    print("               RESULTADOS DE LA BÚSQUEDA")
    print("-" * 45)
    if ruta_optima:
        print(f"Ruta óptima: {' ➔ '.join(ruta_optima)}")
        print(f"Costo total acumulado: ${costo_total:.2f}")
    else:
        print("No se encontró una ruta disponible entre los destinos seleccionados.")
        
    print(f"Tiempo de ejecución del algoritmo: {tiempo_ejecucion_ms:.4f} ms")
    print("-" * 45)