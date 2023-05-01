import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


with open(file_path) as f:
    lines = f.readlines()

data = []		
			# Eliminar las líneas innecesarias y dividir las líneas en celdas
for line in lines:
    if not line.startswith(" "):
        continue
    cells = line.strip().split("  ")
    data.append([cell for cell in cells if cell])

# escribirlo en archivo Excel
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)

os.startfile("output.xlsx")