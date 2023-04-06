from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Proyecto diseño logico")
tabla = ttk.Treeview(ventana, columns=("vacio","d1", "d2","d3","d4","d5","d6","d7","p4","d8","d9","d10", "p3","d11", "p2","p1"), show="headings")
tabla.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
tabla.heading("vacio",text="")
tabla.heading("d1", text="d1")
tabla.heading("d2", text="d2")
tabla.heading("d3", text="d3")
tabla.heading("d4", text="d4")
tabla.heading("d5", text="d5")
tabla.heading("d6", text="d6")
tabla.heading("d7", text="d7")
tabla.heading("p4", text="p4")
tabla.heading("d8", text="d8")
tabla.heading("d9", text="d9")
tabla.heading("d10", text="d10")
tabla.heading("p3", text="p3")
tabla.heading("d11", text="d11")
tabla.heading("p2", text="p2")
tabla.heading("p1", text="p1")

tabla.column("vacio", width=100)
tabla.column("d1", width=60)
tabla.column("d2", width=60)
tabla.column("d3", width=60)
tabla.column("d4", width=60)
tabla.column("d5", width=60)
tabla.column("d6", width=60)
tabla.column("d7", width=60)
tabla.column("p4", width=60)
tabla.column("d8", width=60)
tabla.column("d9", width=60)
tabla.column("d10", width=60)
tabla.column("p3", width=60)
tabla.column("d11", width=60)
tabla.column("p2", width=60)
tabla.column("p1", width=60)
tabla.tag_configure("separador", background="#DDD")

tabla.insert("", "end", values=("Palabra_de_datos:"),tags=("separador",))
tabla.tag_bind("separador", f"<<TreeviewSelect{0}>>", lambda e: "break")

for i in range(4):
    tabla.insert("", "end", values=("p{}".format(i+1)), tags=("separador",))
    tabla.tag_bind("separador", f"<<TreeviewSelect{i}>>", lambda e: "break")

tabla.insert("", "end", values=("Palabra_de_datos:"),tags=("separador",))
tabla.tag_bind("separador", f"<<TreeviewSelect{0}>>", lambda e: "break")

ventana.mainloop()  # Iniciamos el bucle de eventos