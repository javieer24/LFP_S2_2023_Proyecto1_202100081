import tkinter as tk
from tkinter import ttk, filedialog
import json_handler

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Guardar como", command=self.guardar_como)
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        self.notebook = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='Analizar')
        self.text_area1 = tk.Text(self.tab1)
        self.text_area1.pack()

        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='Errores')
        self.text_area2 = tk.Text(self.tab2)
        self.text_area2.pack()

        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text='Reporte')
        self.text_area3 = tk.Text(self.tab3)
        self.text_area3.pack()

        self.notebook.pack(expand=1, fill='both')

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

