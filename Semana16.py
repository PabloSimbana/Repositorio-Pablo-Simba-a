import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista interna de tareas (texto, estado)
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Añadir", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Completar", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")
            return

        self.tasks.append((task_text, False))
        self.update_listbox()
        self.entry.delete(0, tk.END)

    def complete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
            return

        index = selected[0]
        task_text, _ = self.tasks[index]
        self.tasks[index] = (task_text, True)
        self.update_listbox()

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
            return

        index = selected[0]
        del self.tasks[index]
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        for i, (task, completed) in enumerate(self.tasks):
            if completed:
                display_text = f"✔ {task}"
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(i, fg="gray")
            else:
                display_text = f"✗ {task}"
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(i, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    