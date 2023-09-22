import tkinter as tk
from tkinter import filedialog
import json_handler

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root)
        self.text_area.pack()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Guardar como", command=self.guardar_como)
        self.file_menu.add_command(label="Salir", command=self.root.quit)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename()
        self.data = json_handler.load_json(file_path)
        # Aquí puedes procesar los datos JSON

    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        json_handler.save_json(self.data, file_path)

    def guardar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        json_handler.save_json(self.data, file_path)

if __name__ == "__main__":
    app = App()
    app.root.mainloop()

