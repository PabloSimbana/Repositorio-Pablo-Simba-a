import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista interna para almacenar tareas (texto + estado)
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task_event)  # Enter añade tarea

        # Lista visual
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.toggle_complete)  # doble clic

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        self.add_button = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(frame_buttons, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

    # Añadir tarea
    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")
            return

        self.tasks.append({"text": task_text, "completed": False})
        self.update_listbox()
        self.entry.delete(0, tk.END)

    def add_task_event(self, event):
        self.add_task()

    # Marcar como completada
    def mark_complete(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = selected[0]
        self.tasks[index]["completed"] = True
        self.update_listbox()

    # Alternar completado con doble clic
    def toggle_complete(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()

    # Eliminar tarea
    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")
            return

        index = selected[0]
        del self.tasks[index]
        self.update_listbox()

    # Actualizar lista visual
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.listbox.insert(tk.END, "✔ " + task["text"])
            else:
                self.listbox.insert(tk.END, task["text"])


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    