from tkinter import *
from tkinter import ttk
PAR_BITS = 4

def determinarError(n):
    if n == 1:
        return "Error"
    else:
        return "Correcto"

def valoresDeParidad(con_paridad, i):
    lista_numeros = list(con_paridad)
    for j in range(len(lista_numeros)):
        if(j & (2**i) == (2**i)):
            lista_numeros[j] = "-"
    return tuple(lista_numeros)

def tablaHamming(recibido, tests):
    ventana2 = Toplevel()
    ventana2.title("Tabla 2. Comprobación de los bits de paridad")
    ventana2.resizable(False,False)
    tablaHamming = ttk.Treeview(ventana2, columns=("vacio", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "p4", "d8", "d9", "d10", "p3", "d11", "p2", "p1", "prueba", "bit"), show="headings", height=5)
    tablaHamming.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
    tablaHamming.heading("vacio", text="")
    tablaHamming.heading("d1", text="d1")
    tablaHamming.heading("d2", text="d2")
    tablaHamming.heading("d3", text="d3")
    tablaHamming.heading("d4", text="d4")
    tablaHamming.heading("d5", text="d5")
    tablaHamming.heading("d6", text="d6")
    tablaHamming.heading("d7", text="d7")
    tablaHamming.heading("p4", text="p4")
    tablaHamming.heading("d8", text="d8")
    tablaHamming.heading("d9", text="d9")
    tablaHamming.heading("d10", text="d10")
    tablaHamming.heading("p3", text="p3")
    tablaHamming.heading("d11", text="d11")
    tablaHamming.heading("p2", text="p2")
    tablaHamming.heading("p1", text="p1")
    tablaHamming.heading("prueba", text="Prueba de paridad")
    tablaHamming.heading("bit", text="Bit de paridad")

    tablaHamming.column("vacio", width=140)
    tablaHamming.column("d1", width=60, anchor="center")
    tablaHamming.column("d2", width=60, anchor="center")
    tablaHamming.column("d3", width=60, anchor="center")
    tablaHamming.column("d4", width=60, anchor="center")
    tablaHamming.column("d5", width=60, anchor="center")
    tablaHamming.column("d6", width=60, anchor="center")
    tablaHamming.column("d7", width=60, anchor="center")
    tablaHamming.column("p4", width=60, anchor="center")
    tablaHamming.column("d8", width=60, anchor="center")
    tablaHamming.column("d9", width=60, anchor="center")
    tablaHamming.column("d10", width=60, anchor="center")
    tablaHamming.column("p3", width=60, anchor="center")
    tablaHamming.column("d11", width=60, anchor="center")
    tablaHamming.column("p2", width=60, anchor="center")
    tablaHamming.column("p1", width=60, anchor="center")
    tablaHamming.column("prueba", width=120, anchor="center")
    tablaHamming.column("bit", width=100, anchor="center")

    tablaHamming.tag_configure("separador", background="#DDD")

    tablaHamming.insert("", "end", values=("Palabra de datos recibida", ) + tuple(recibido), tags=("separador",))
    tablaHamming.tag_bind("separador", f"<<TreeviewSelect{0}>>", lambda e: "break")
    for i in range(1,5):
        tablaHamming.insert("", "end", values=("p{}".format(i), ) + valoresDeParidad(recibido, i-1) + (determinarError(tests[i-1]), tests[i-1]), tags=("separador",))
        tablaHamming.tag_bind("separador", f"<<TreeviewSelect{i}>>", lambda e: "break")

    ventana2.mainloop()  # Iniciamos el bucle de eventos

if __name__ == "__main__":
    tablaHamming("100110101001010")
    pass