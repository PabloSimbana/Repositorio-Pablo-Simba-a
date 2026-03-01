import json


# ==============================
# Clase Producto
# ==============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir a diccionario (para guardar en archivo)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crear producto desde diccionario
    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ==============================
# Clase Inventario
# ==============================
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: id -> Producto

    # Añadir producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("⚠ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("✔ Producto agregado correctamente.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✔ Producto eliminado.")
        else:
            print("⚠ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("✔ Producto actualizado.")
        else:
            print("⚠ Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("⚠ No se encontraron productos.")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Guardar en archivo
    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            json.dump(
                [producto.to_dict() for producto in self.productos.values()],
                archivo,
                indent=4
            )
        print("✔ Inventario guardado en archivo.")

    # Cargar desde archivo
    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    producto = Producto.from_dict(item)
                    self.productos[producto.get_id()] = producto
            print("✔ Inventario cargado.")
        except FileNotFoundError:
            print("⚠ Archivo no encontrado. Se creará uno nuevo.")


# ==============================
# Interfaz de Usuario
# ==============================
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario.json")
            print("Saliendo del sistema...")
            break

        else:
            print("⚠ Opción inválida.")


if __name__ == "__main__":
    menu()
