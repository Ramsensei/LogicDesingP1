from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def convertir():
    numero_hex = entrada.get().upper()  # Obtenemos el número hexadecimal ingresado y lo convertimos a mayúsculas
    try:
        numero_int = int(numero_hex, 16)  # Convertimos el número hexadecimal a entero
        if 0 <= numero_int <= 2047:  # Verificamos que el número esté en el rango permitido (000 a 7FF)
            binario = bin(numero_int)[2:].zfill(11)  # Convertimos a binario y rellenamos con ceros a la izquierda hasta tener 11 bits
            octal = oct(numero_int)[2:].zfill(4)  # Convertimos a octal y rellenamos con ceros a la izquierda hasta tener 4 dígitos
            decimal = str(numero_int)  # Convertimos a decimal
            tabla.delete(*tabla.get_children())  # Limpiamos la tabla antes de mostrar los resultados
            tabla.insert("", "end", values=(numero_hex, binario, octal, decimal))
            nzri_plot(binario)
        
        else:
            messagebox.showerror("Error", "El número debe estar en el rango 000 a 7FF")
    except ValueError:
        messagebox.showerror("Error", "El número ingresado no es hexadecimal")

# Creamos la ventana principal
ventana = Tk()
ventana.title("Proyecto diseño logico")

# Creamos los widgets
Label(ventana, text="Ingrese un número hexadecimal de 11 bits (000 a 7FF)").grid(row=0, column=0, padx=5, pady=5)
entrada = Entry(ventana)
entrada.grid(row=0, column=1, padx=5, pady=5)
Button(ventana, text="Convertir", command=convertir).grid(row=0, column=2, padx=5, pady=5)
tabla = ttk.Treeview(ventana, columns=("hexadecimal", "binario", "octal", "decimal"), show="headings")
tabla.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
tabla.heading("hexadecimal", text="Hexadecimal")
tabla.heading("binario", text="Binario")
tabla.heading("octal", text="Octal")
tabla.heading("decimal", text="Decimal")
tabla.column("hexadecimal", width=100)
tabla.column("binario", width=100)
tabla.column("octal", width=100)
tabla.column("decimal", width=100)
tabla.tag_configure("separador", background="#DDD")
for i in range(5):
    tabla.insert("", "end", values=("-", "-", "-", "-"), tags=("separador",))
    tabla.tag_bind("separador", f"<<TreeviewSelect{i}>>", lambda e: "break")


def nzri_plot(bin_str):
    
    # Convierte la cadena binaria en una lista de enteros
    binary_list = [int(d) for d in bin_str]
    
    # Inicializa los ejes x e y
    x = []
    y = []
    
    # Inicializa la variable de polaridad
    polarity = 1
    
    # Recorre la lista binaria y agrega los valores de x e y
    for i in range(len(binary_list)):
        #print(i)
        #print(binary_list[i])
        if binary_list[i] == 1:
            # Si el bit es 1, invierte la polaridad y agrega una línea vertical
            polarity *= -1
            x.extend([i, i+1])
            y.extend([polarity, polarity])
        else:
            # Si el bit es 0, agrega una línea horizontal
            x.extend([i, i])
            y.extend([polarity, polarity])
    
    # Grafica la señal NZRI
    plt.plot(x, y, drawstyle='steps-pre')
    plt.ylim(-1.5, 1.5)
    plt.title('Gráfica NRZI para el número hexadecimal {}'.format(bin_str))
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Configura la escala del eje x
    plt.xticks(range(1, len(binary_list)+1))
    
    plt.show()

ventana.mainloop()  # Iniciamos el bucle de eventos