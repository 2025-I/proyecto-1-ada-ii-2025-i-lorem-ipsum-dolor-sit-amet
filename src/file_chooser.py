import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    archivo = filedialog.askopenfilename(
        title="Seleccione el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    return archivo
