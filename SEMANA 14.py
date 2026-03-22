import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class AgendaApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # ----- FRAME LISTA DE EVENTOS -----
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        columnas = ("Fecha", "Hora", "Descripción")

        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)

        self.tree.pack()

        # ----- FRAME ENTRADA DE DATOS -----
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # Fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha = DateEntry(frame_entrada, width=12, background='darkblue',
                               foreground='white', borderwidth=2)
        self.fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora = tk.Entry(frame_entrada)
        self.hora.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.descripcion = tk.Entry(frame_entrada, width=40)
        self.descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # ----- FRAME BOTONES -----
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.grid(row=0, column=1, padx=10)

        btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
        btn_salir.grid(row=0, column=2, padx=10)

    # ----- FUNCION AGREGAR EVENTO -----
    def agregar_evento(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        descripcion = self.descripcion.get()

        if fecha == "" or hora == "" or descripcion == "":
            messagebox.showwarning("Campos vacíos", "Debe completar todos los campos")
            return

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar campos
        self.hora.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)

    # ----- FUNCION ELIMINAR EVENTO -----
    def eliminar_evento(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Seleccione un evento para eliminar")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")

        if confirmacion:
            for item in seleccionado:
                self.tree.delete(item)


# ----- EJECUTAR APP -----
root = tk.Tk()
app = AgendaApp(root)
root.mainloop()
