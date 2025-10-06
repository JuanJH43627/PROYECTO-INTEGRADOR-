# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x370")


style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)

style.configure("salir.TButton", background="#E4E2E2", foreground="#000")
style.map("salir.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

salir = ttk.Button(master=main, text="Salir", style="salir.TButton")
salir.place(x=495, y=224, width=130, height=30)

style.configure("completarpalabras.TButton", background="#E4E2E2", foreground="#000")
style.map("completarpalabras.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

completarpalabras = ttk.Button(master=main, text="Completar Palabras", style="completarpalabras.TButton")
completarpalabras.place(x=499, y=60, width=130, height=40)

style.configure("puntajes.TButton", background="#E4E2E2", foreground="#000")
style.map("puntajes.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

puntajes = ttk.Button(master=main, text="Puntajes", style="puntajes.TButton")
puntajes.place(x=137, y=226, width=113, height=30)

style.configure("abecedario.TButton", background="#E4E2E2", foreground="#000")
style.map("abecedario.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

abecedario = ttk.Button(master=main, text="Abecedario", style="abecedario.TButton")
abecedario.place(x=125, y=61, width=130, height=30)


main.mainloop()