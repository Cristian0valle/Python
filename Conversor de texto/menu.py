import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os 
root = tk.Tk()
root.withdraw() file_path = filedialog.askopenfilename() # Leer el archivo de texto y separarlo en lÃ­neas
with open(file_path) as f:
    lines = f.readlines() # Eliminar las lÃ­neas innecesarias y dividir las lÃ­neas en celdas

data = []
for line in lines:
    if not line.startswith(" "):
        continue
    cells = line.strip().split("  ")
    data.append([cell for cell in cells if cell]) # Crear el DataFrame y escribirlo en un archivo Excel

df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False) os.startfile("output.xlsx")