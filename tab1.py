from tkinter import *
from tkinter import ttk


def enumSinParidad(sin_paridad):
    lista_numeros = ["Sin_paridad"] + [sin_paridad[i] for i in range(len(sin_paridad))]
    lista_numeros.insert(len(sin_paridad)+1, "-")
    lista_numeros.insert(-1, "-")
    lista_numeros.insert(-3, "-")
    lista_numeros.insert(-7, "-")
    return tuple(lista_numeros)

def valoresDeParidad(con_paridad, i):
    lista_numeros = list(con_paridad)
    for j in range(len(lista_numeros)):
        if(j & (2**i) == (2**i)):
            lista_numeros[j] = "-"
    return tuple(lista_numeros)

def tablaBitsParidad(sin_paridad, con_paridad,paridad):
    ventana = Toplevel()
    ventana.title("Tabla para encontrar los bits de paridad")
    ventana.resizable(False, False)
    tablaBitsParidad = ttk.Treeview(ventana, columns=("vacio","d1", "d2","d3","d4","d5","d6","d7","p4","d8","d9","d10", "p3","d11", "p2","p1"), show="headings", height=6)
    tablaBitsParidad.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    tablaBitsParidad.heading("vacio",text="")
    tablaBitsParidad.heading("d1", text="d1")
    tablaBitsParidad.heading("d2", text="d2")
    tablaBitsParidad.heading("d3", text="d3")
    tablaBitsParidad.heading("d4", text="d4")
    tablaBitsParidad.heading("d5", text="d5")
    tablaBitsParidad.heading("d6", text="d6")
    tablaBitsParidad.heading("d7", text="d7")
    tablaBitsParidad.heading("p4", text="p4")
    tablaBitsParidad.heading("d8", text="d8")
    tablaBitsParidad.heading("d9", text="d9")
    tablaBitsParidad.heading("d10", text="d10")
    tablaBitsParidad.heading("p3", text="p3")
    tablaBitsParidad.heading("d11", text="d11")
    tablaBitsParidad.heading("p2", text="p2")
    tablaBitsParidad.heading("p1", text="p1")

    tablaBitsParidad.column("vacio", width=100, anchor="center", )
    tablaBitsParidad.column("d1", width=60, anchor="center")
    tablaBitsParidad.column("d2", width=60, anchor="center")
    tablaBitsParidad.column("d3", width=60, anchor="center")
    tablaBitsParidad.column("d4", width=60, anchor="center")
    tablaBitsParidad.column("d5", width=60, anchor="center")
    tablaBitsParidad.column("d6", width=60, anchor="center")
    tablaBitsParidad.column("d7", width=60, anchor="center")
    tablaBitsParidad.column("p4", width=60, anchor="center")
    tablaBitsParidad.column("d8", width=60, anchor="center")
    tablaBitsParidad.column("d9", width=60, anchor="center")
    tablaBitsParidad.column("d10", width=60, anchor="center")
    tablaBitsParidad.column("p3", width=60, anchor="center")
    tablaBitsParidad.column("d11", width=60, anchor="center")
    tablaBitsParidad.column("p2", width=60, anchor="center")
    tablaBitsParidad.column("p1", width=60, anchor="center")
    tablaBitsParidad.tag_configure("separador", background="#DDD")

    tablaBitsParidad.insert("", "end", values=enumSinParidad(sin_paridad),tags=("separador",))
    tablaBitsParidad.tag_bind("separador", f"<<TreeviewSelect{0}>>", lambda e: "break")

    for i in range(4):
        tablaBitsParidad.insert("", "end", values=("p{}".format(i+1),) + valoresDeParidad(con_paridad, i), tags=("separador",))
        tablaBitsParidad.tag_bind("separador", f"<<TreeviewSelect{i}>>", lambda e: "break")

    tablaBitsParidad.insert("", "end", values=("Con_paridad:",)+tuple(con_paridad),tags=("separador",))
    tablaBitsParidad.tag_bind("separador", f"<<TreeviewSelect{0}>>", lambda e: "break")

    resultadoFinal = Label(ventana, text=f"Numero Final: {con_paridad}")
    resultadoFinal.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    paridadFinal = Label(ventana, text=f"Paridad: {paridad}")
    paridadFinal.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    ventana.mainloop()  # Iniciamos el bucle de eventos

if __name__ == "__main__":
    tablaBitsParidad('10011011000', "100110101001010")