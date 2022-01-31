from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

ventana = Tk()
ventana.title("Practica 1")
ventana.geometry("260x210")
ventana.config(bg = "black")

Texto = StringVar()
Operacion = ""
Texto.set(Operacion)

Pantalla = Label(ventana, justify = "center", textvariable = Texto, height = 1, width = 30).place(x=20, y=10)

def funcion_boton1():
    global Operacion 
    Operacion = Operacion + "1"
    Texto.set(Operacion)    
def funcion_boton2():
    global Operacion 
    Operacion = Operacion + "2"
    Texto.set(Operacion)    
def funcion_boton3():
    global Operacion 
    Operacion = Operacion + "3"
    Texto.set(Operacion)    
def funcion_boton4():
    global Operacion 
    Operacion = Operacion + "4"
    Texto.set(Operacion)    
def funcion_boton5():
    global Operacion 
    Operacion = Operacion + "5"
    Texto.set(Operacion)    
def funcion_boton6():
    global Operacion 
    Operacion = Operacion + "6"
    Texto.set(Operacion)    
def funcion_boton7():
    global Operacion 
    Operacion = Operacion + "7"
    Texto.set(Operacion)    
def funcion_boton8():
    global Operacion 
    Operacion = Operacion + "8"
    Texto.set(Operacion)    
def funcion_boton9():
    global Operacion 
    Operacion = Operacion + "9"
    Texto.set(Operacion)    
def funcion_boton0():
    global Operacion 
    Operacion = Operacion + "0"
    Texto.set(Operacion)
    
def funcion_botonSuma():
    global Operacion 
    Operacion = Operacion + "+"
    Texto.set(Operacion)
def funcion_botonResta():
    global Operacion 
    Operacion = Operacion + "-"
    Texto.set(Operacion)
def funcion_botonMulti():
    global Operacion 
    Operacion = Operacion + "*"
    Texto.set(Operacion)
def funcion_botonDiv():
    global Operacion 
    Operacion = Operacion + "/"
    Texto.set(Operacion)
def funcion_botonRes():
    global Operacion 
    Operacion = str(eval(Operacion))
    Texto.set(Operacion)
def funcion_botonCC():
    global Operacion 
    Operacion = ""
    Texto.set(Operacion)

boton1      = Button(ventana, text= "1",  command=funcion_boton1).place(x= 20, y=120)
boton2      = Button(ventana, text= "2",  command=funcion_boton2).place(x= 50, y=120)
boton3      = Button(ventana, text= "3",  command=funcion_boton3).place(x= 80, y=120)
boton4      = Button(ventana, text= "4",  command=funcion_boton4).place(x= 20, y= 80)
boton5      = Button(ventana, text= "5",  command=funcion_boton5).place(x= 50, y= 80)
boton6      = Button(ventana, text= "6",  command=funcion_boton6).place(x= 80, y= 80)
boton7      = Button(ventana, text= "7",  command=funcion_boton7).place(x= 20, y= 40)
boton8      = Button(ventana, text= "8",  command=funcion_boton8).place(x= 50, y= 40)
boton9      = Button(ventana, text= "9",  command=funcion_boton9).place(x= 80, y= 40)
boton0      = Button(ventana, text= "0",  command=funcion_boton0).place(x= 20, y=160)

botonSuma   = Button(ventana, text= "+",  command= funcion_botonSuma).  place(x=218, y= 40)
botonResta  = Button(ventana, text= " -", command= funcion_botonResta). place(x=218, y= 80)
botonMulti  = Button(ventana, text= " *", command= funcion_botonMulti). place(x=218, y=120)
botonDiv    = Button(ventana, text= " /", command= funcion_botonDiv).   place(x=218, y=160)
botonRes    = Button(ventana, text= " =", command= funcion_botonRes).   place(x=188, y=160)
botonCC     = Button(ventana, text= "CC", command= funcion_botonCC).    place(x=152, y=160)

ventana.mainloop()