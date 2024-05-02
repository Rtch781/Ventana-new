import tkinter as tk

def mostrar_datos():
    nombre = entrynombre.get()
    apellido = entryapellido.get()
    sexo = obtener_seleccion()
    ciudad_seleccionada = obtener_seleccion_Ciudad()
    
    # Limpiar el Frame antes de agregar nuevos datos
    for widget in Datos.winfo_children():
        widget.destroy()
    
    tk.Label(Datos, text="Nombre: " + nombre).pack()
    tk.Label(Datos, text="Apellido: " + apellido).pack()
    tk.Label(Datos, text="Sexo: " + sexo).pack()
    tk.Label(Datos, text="Ciudad: " + ciudad_seleccionada).pack()
     
def obtener_seleccion():
    seleccion = rsexo.get()
    if seleccion == 1:
        return "Femenino"
    elif seleccion == 2:
        return "Masculino"
    
def obtener_seleccion_Ciudad():
    seleccionados = ciudades.curselection()
    for index in seleccionados:
        elemento = ciudades.get(index)
        return elemento

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("1024x960")

lnombre = tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0)

entrynombre = tk.Entry(ventana)
entrynombre.grid(row=0, column=1)

lapellido = tk.Label(ventana, text="Apellido:")
lapellido.grid(row=1, column=0)

entryapellido = tk.Entry(ventana)
entryapellido.grid(row=1, column=1)

rsexo = tk.IntVar() 

rsexo_label = tk.Label(ventana, text="Sexo:")
rsexo_label.grid(row=2, column=0)

rb_femenino = tk.Radiobutton(ventana, text="Femenino", variable=rsexo, value=1)
rb_femenino.grid(row=2, column=1)

rb_masculino = tk.Radiobutton(ventana, text="Masculino", variable=rsexo, value=2)
rb_masculino.grid(row=2, column=2)

lciudades = tk.Label(ventana, text="Ciudad:")
lciudades.grid(row=3, column=0)

ciudades = tk.Listbox(ventana)
ciudades.grid(row=3, column=1)
ciudades.insert(1, "Cartagena")
ciudades.insert(2, "Caracas")

button = tk.Button(ventana, text="Enviar", command=mostrar_datos)
button.grid(row=4, column=1)

Datos = tk.Frame(ventana, width=400, height=200, bd=2, relief="raised")
Datos.grid(row=5, column=1)

ventana.mainloop()
