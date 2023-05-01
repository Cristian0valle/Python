import tkinter as tk

def search(event):
    content =search_box.get()
    resul= wikipedia.summary(content, sentences=1)

window = tk.Tk()
window.geometry("300x300")
search_box = tk.Entry(window)
search_box.place(x=0,y=0)
search_box.bind('<Return>', search)
T = tk.Text(window)
search_box.pack()
T.pack()
T.insert(tk.END, "test")