from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tab1 import tablaBitsParidad
from tabla2 import tablaHamming
from hamming import *
import matplotlib.pyplot as plt
PAR_BITS = 4 

datos_binario = ""
def nzri_plot(bin_str):
    
    # Convierte la cadena binaria en una lista de enteros
    binary_list = [int(d) for d in bin_str]
    
    # Inicializa los ejes x e y
    x = [0,1]
    y = [-1,-1]
    
    # Inicializa la variable de polaridad
    polarity = -1

    # Recorre la lista binaria y agrega los valores de x e y
    for i in range(len(binary_list)):
        #print(i)
        #print(binary_list[i])
        if binary_list[i] == 1:
            # Si el bit es 1, invierte la polaridad y agrega una línea vertical
            polarity *= -1
            x.extend([i+2])
            y.extend([polarity])
        else:
            # Si el bit es 0, agrega una línea horizontal
            x.extend([i+2])
            y.extend([polarity])
    
    # Grafica la señal NZRI
    print(x)
    print(y)
    plt.clf()
    plt.plot(x, y, drawstyle='steps-pre')
    plt.ylim(-1.5, 1.5)
    plt.title('Gráfica NRZI para el número hexadecimal {}'.format(bin_str))
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Configura la escala del eje x
    plt.xticks(range(1, len(binary_list)+1))
    
    plt.show()

def mostrarTablaBitsParidad(data):
    # Calculate the no of Redundant Bits Required
    m = len(data)
    r = calcRedundantBits(m)
    
    # Determine the positions of Redundant Bits
    arr = posRedundantBits(data, r)
    
    # Determine the parity bits
    arr = calcParityBits(arr, r)

    tablaBitsParidad(data, arr)

def mostrarTablaHamming(data):
    pass

def convertir():
    global datos_binario
    numero_hex = entrada.get().upper()  # Obtenemos el número hexadecimal ingresado y lo convertimos a mayúsculas
    try:
        numero_int = int(numero_hex, 16)  # Convertimos el número hexadecimal a entero
        if 0 <= numero_int <= 2047:  # Verificamos que el número esté en el rango permitido (000 a 7FF)
            binario = bin(numero_int)[2:].zfill(11)  # Convertimos a binario y rellenamos con ceros a la izquierda hasta tener 11 bits
            octal = oct(numero_int)[2:].zfill(4)  # Convertimos a octal y rellenamos con ceros a la izquierda hasta tener 4 dígitos
            decimal = str(numero_int)  # Convertimos a decimal
            tablaConversiones.delete(*tablaConversiones.get_children())  # Limpiamos la tabla antes de mostrar los resultados
            tablaConversiones.insert("", "end", values=(numero_hex, binario, octal, decimal))
            datos_binario = binario
        else:
            messagebox.showerror("Error", "El número debe estar en el rango 000 a 7FF")
    except ValueError:
        messagebox.showerror("Error", "El número ingresado no es hexadecimal")

# Creamos la ventana principal
ventana = Tk()
ventana.title("Proyecto diseño logico")
ventana.resizable(False, False)

# Creamos los widgets
Label(ventana, text="Ingrese un número hexadecimal de 11 bits (000 a 7FF)").grid(row=0, column=0, padx=5, pady=5)
entrada = Entry(ventana)
entrada.grid(row=0, column=1, padx=5, pady=5)
Button(ventana, text="Convertir", command=convertir).grid(row=0, column=2, padx=5, pady=5)
Button(ventana, text="Mostrar NZRI", command=lambda:nzri_plot(datos_binario)).grid(row=2, column=0, padx=5, pady=5)
Button(ventana, text="Tabla Bits de Paridad", command=lambda:mostrarTablaBitsParidad(datos_binario)).grid(row=2, column=1, padx=5, pady=5)
Button(ventana, text="Tabla Bits de Hamming", command=lambda:mostrarTablaHamming(datos_binario)).grid(row=2, column=2, padx=5, pady=5)



#tabla conversiones
tablaConversiones = ttk.Treeview(ventana, columns=("hexadecimal", "binario", "octal", "decimal"), show="headings", height=1)
tablaConversiones.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
tablaConversiones.heading("hexadecimal", text="Hexadecimal")
tablaConversiones.heading("binario", text="Binario")
tablaConversiones.heading("octal", text="Octal")
tablaConversiones.heading("decimal", text="Decimal")
tablaConversiones.column("hexadecimal", width=100)
tablaConversiones.column("binario", width=100)
tablaConversiones.column("octal", width=100)
tablaConversiones.column("decimal", width=100)
tablaConversiones.tag_configure("separador", background="#DDD")

for i in range(5):
    tablaConversiones.insert("", "end", values=("-", "-", "-", "-"), tags=("separador",))
    tablaConversiones.tag_bind("separador", f"<<TreeviewSelect{i}>>", lambda e: "break")




ventana.mainloop()  # Iniciamos el bucle de eventos