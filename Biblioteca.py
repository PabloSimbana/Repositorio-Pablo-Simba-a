# ================================
# Clase Libro
# ================================
class Libro:
    """
    Representa un libro dentro de la biblioteca.
    Usa una tupla para almacenar el título y autor ya que
    estos atributos no cambian una vez creado el libro.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False  # Estado del libro

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}"


# ================================
# Clase Usuario
# ================================
class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    Mantiene una lista de libros prestados.
    """

    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de ISBN de libros prestados

    def prestar_libro(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

    def listar_prestados(self):
        return self.libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {self.libros_prestados}"


# ================================
# Clase Biblioteca
# ================================
class Biblioteca:
    """
    Gestiona libros, usuarios y préstamos.
    Usa:
    - Diccionario para libros (ISBN -> Libro)
    - Conjunto para IDs únicos de usuarios
    """

    def __init__(self):
        self.libros = {}  # Diccionario de libros
        self.usuarios = {}  # Diccionario de usuarios
        self.ids_usuarios = set()  # Conjunto para asegurar IDs únicos

    # ------------------------------
    # Gestión de libros
    # ------------------------------
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ------------------------------
    # Gestión de usuarios
    # ------------------------------
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_usuarios:
            print("ID de usuario ya registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print("Usuario registrado correctamente.")

    def eliminar_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ------------------------------
    # Préstamos
    # ------------------------------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no existe.")
            return

        libro = self.libros[isbn]

        if libro.prestado:
            print("El libro ya está prestado.")
        else:
            libro.prestado = True
            self.usuarios[user_id].prestar_libro(isbn)
            print("Libro prestado correctamente.")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no existe.")
            return

        libro = self.libros[isbn]

        if isbn in self.usuarios[user_id].libros_prestados:
            libro.prestado = False
            self.usuarios[user_id].devolver_libro(isbn)
            print("Libro devuelto correctamente.")
        else:
            print("Ese usuario no tiene este libro.")

    # ------------------------------
    # Búsquedas
    # ------------------------------
    def buscar_por_titulo(self, titulo):
        resultados = [l for l in self.libros.values() if l.obtener_titulo().lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [l for l in self.libros.values() if l.obtener_autor().lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [l for l in self.libros.values() if l.categoria.lower() == categoria.lower()]
        return resultados

    # ------------------------------
    # Libros prestados por usuario
    # ------------------------------
    def listar_libros_usuario(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[user_id]
        for isbn in usuario.libros_prestados:
            print(self.libros[isbn])


# ================================
# PRUEBA DEL SISTEMA
# ================================

biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("1984", "George Orwell", "Distopía", "222")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "333")

# Añadir libros
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Ana", 1)
usuario2 = Usuario("Luis", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro(1, "111")
biblioteca.prestar_libro(2, "222")

# Listar libros prestados
print("\nLibros prestados a Ana:")
biblioteca.listar_libros_usuario(1)

# Devolver libro
biblioteca.devolver_libro(1, "111")

# Buscar libro
print("\nBuscar por autor:")
resultados = biblioteca.buscar_por_autor("George Orwell")
for libro in resultados:
    print(libro)
    