from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

def imgMostrar():
    x = filedialog.askopenfilename(title = "Seleccionar Imagen", filetypes=[("img files","*.jpg; *.jpeg; *.png")]) 
    img = Image.open(x)
    img.save("Imagen - Original.jpg")
    img = img.resize(( 345 , 345 ), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place(x = 150, y = 30)

def imgBN(): #BN = Blanco/Negro
    img = Image.open("Imagen - Original.jpg")
    width, height = img.size
    print(width)
    print(height)
    for x in range(width):
        for y in range(height):
            r,g,b = img.getpixel((x,y))
            BN = int( r * 0.299) + int( g * 0.587 ) + int( b * 0.124 )
            pixelg = tuple( [ BN, BN, BN])
            img.putpixel( (x,y), pixelg)
    img.save("Imagen - Escala de Grises.jpg")
    img = img.resize( ( 345, 345), Image.ANTIALIAS )
    
    Histograma( img, "Escala de Grises")
    
    img = ImageTk.PhotoImage(img)
    panel = Label( ventana, image = img)
    panel.image = img
    panel.place( x = 500, y = 30)
    panel.image = img
 
def imgColor():
    img = Image.open("Imagen - Original.jpg")
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            r, g, b, = img.getpixel((x, y))
            rgb = tuple( [ r, g, b ] )
            if rgb >= tuple([ 127, 127, 127]):
                img.putpixel( (x,y),  (0,0,0))
    
    img.save("Imagen - Remplazar Color.jpg")
    img = img.resize( ( 345, 345), Image.ANTIALIAS)
    img3 = Image.open("Imagen - Remplazar Color.jpg")
    HistogramaLum( img3, "Binarizacion")
    
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img
    
def imgBinaria():
    img = Image.open("Imagen - Original.jpg")
    width, height = img.size    
    for x in range(width):
        for y in range(height):
            r,  g,  b,  = img.getpixel((x, y))
            Luminosidad = ( r + g + b ) / 3
            rgb = tuple( [ r, g, b ] )
            if Luminosidad >= 128:
                img.putpixel( (x,y),  (255,255,255))
            else:
                img.putpixel( (x,y),  (  0,  0,  0))
    
    img.save("Imagen - Binaria.jpg")
    img3 = Image.open("Imagen - Binaria.jpg")
    HistogramaLum( img3, "Binarizacion")
    img = img.resize( ( 345, 345), Image.ANTIALIAS)
    
    
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img
    
def imgBordes():
    img = Image.open("Imagen - Original.jpg")
    img2 = Image.open("Imagen - Original.jpg")
    width, height = img.size
            
    for x in range( 1, (width - 1) ):
        for y in range( 1, (height - 1) ):            
            R1, G1, B1 = img2.getpixel(( x-1, y-1 ))
            R2, G2, B2 = img2.getpixel(( x,   y-1 ))
            R3, G3, B3 = img2.getpixel(( x+1, y-1 ))            
            R4, G4, B4 = img2.getpixel(( x-1, y   ))
            R5, G5, B5 = img2.getpixel(( x,   y   ))
            R6, G6, B6 = img2.getpixel(( x+1, y   ))            
            R7, G7, B7 = img2.getpixel(( x-1, y+1 ))
            R8, G8, B8 = img2.getpixel(( x,   y+1 ))
            R9, G9, B9 = img2.getpixel(( x+1, y+1 ))            
            MR = np.array( [ R1,R2,R3,  R4,R5,R6,   R7,R8,R9 ]) #Matriz de Rojos
            MG = np.array( [ G1,G2,G3,  G4,G5,G6,   G7,G8,G9 ]) #Matriz de Verdes
            MB = np.array( [ B1,B2,B3,  B4,B5,B6,   B7,B8,B9 ]) #Matriz de Azules
            
            MH = (  1, 2, 1,     0, 0, 0,   -1,-2,-1)           #Matriz de Convolucion Horizontal
            MV = ( -1, 0, 1,    -2, 0, 2,   -1, 0, 1)           #Matriz de Convolucion Vertical
            
            RV = np.dot(MR, MV)                                 #Bordes Rojos Verticales
            GV = np.dot(MG, MV)                                 #Bordes Rojos Verticales
            BV = np.dot(MB, MV)                                 #Bordes Rojos Verticales
            
            RH = np.dot(MR, MH)                                 #Bordes Rojos Horizontales
            GH = np.dot(MG, MH)                                 #Bordes Rojos Horizontales
            BH = np.dot(MB, MH)                                 #Bordes Rojos Horizontales
            
            RT = RV + RH                                        #Total de Rojos
            GT = GV + GH                                        #Total de Verdes
            BT = BV + BH                                        #Total de Azules
            img.putpixel( (x,y),  (RT, GT, BT))                        
    img.save("Imagen - Detección de Bordes.jpg")
    
    img3 = Image.open("Imagen - Detección de Bordes.jpg")
    Histograma( img3, "Detección de Bordes")
    
    img = img.resize( ( 345, 345), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img

def imgInvert():
    img = Image.open("Imagen - Original.jpg")
    width, height = img.size    
    for x in range(width):
        for y in range(height):
            r,  g,  b,  = img.getpixel((x, y))            
            r = (255 - r)
            g = (255 - g)
            b = (255 - b)
            img.putpixel( (x,y),  (r,g,b))
    img.save("Imagen - Colores Invertidos.jpg")
    
    img3 = Image.open("Imagen - Colores Invertidos.jpg")
    Histograma( img3, "Colores Invertidos")
    
    img = img.resize( ( 345, 345 ), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img
    
def imgLaplac():
    img = Image.open("Imagen - Original.jpg")
    img2 = Image.open("Imagen - Original.jpg")
    width, height = img.size
            
    for x in range( 1, (width - 1) ):
        for y in range( 1, (height - 1) ):            
            R1, G1, B1 = img2.getpixel(( x-1, y-1 ))
            R2, G2, B2 = img2.getpixel(( x,   y-1 ))
            R3, G3, B3 = img2.getpixel(( x+1, y-1 ))            
            R4, G4, B4 = img2.getpixel(( x-1, y   ))
            R5, G5, B5 = img2.getpixel(( x,   y   ))
            R6, G6, B6 = img2.getpixel(( x+1, y   ))            
            R7, G7, B7 = img2.getpixel(( x-1, y+1 ))
            R8, G8, B8 = img2.getpixel(( x,   y+1 ))
            R9, G9, B9 = img2.getpixel(( x+1, y+1 ))            
            MR = np.array( [ R1,R2,R3,  R4,R5,R6,   R7,R8,R9 ]) #Matriz de Rojos
            MG = np.array( [ G1,G2,G3,  G4,G5,G6,   G7,G8,G9 ]) #Matriz de Verdes
            MB = np.array( [ B1,B2,B3,  B4,B5,B6,   B7,B8,B9 ]) #Matriz de Azules
            
            ML = (  0, 1, 0,     1,-4, 1,    0, 1, 0 )          #Matriz Laplaciana
            
            RL = np.dot(MR, ML)                                 #Laplace Rojos
            GL = np.dot(MG, ML)                                 #Laplace Rojos
            BL = np.dot(MB, ML)                                 #Laplace Rojos

            img.putpixel( (x,y),  (RL, GL, BL))
                        
    img.save("Imagen - Filtro de Laplace.jpg")
    img3 = Image.open("Imagen - Filtro de Laplace.jpg")
    Histograma( img3, "Filtro de Laplace")
    
    img = img.resize( ( 345, 345), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img    
    
def imgGauss():
    img = Image.open("Imagen - Original.jpg")
    img2 = Image.open("Imagen - Original.jpg")
    width, height = img.size
            
    for x in range( 1, (width - 1) ):
        for y in range( 1, (height - 1) ):            
            R1, G1, B1 = img2.getpixel(( x-1, y-1 ))
            R2, G2, B2 = img2.getpixel(( x,   y-1 ))
            R3, G3, B3 = img2.getpixel(( x+1, y-1 ))            
            R4, G4, B4 = img2.getpixel(( x-1, y   ))
            R5, G5, B5 = img2.getpixel(( x,   y   ))
            R6, G6, B6 = img2.getpixel(( x+1, y   ))            
            R7, G7, B7 = img2.getpixel(( x-1, y+1 ))
            R8, G8, B8 = img2.getpixel(( x,   y+1 ))
            R9, G9, B9 = img2.getpixel(( x+1, y+1 ))            
            MR = np.array( [ R1,R2,R3,  R4,R5,R6,   R7,R8,R9 ]) #Matriz de Rojos
            MG = np.array( [ G1,G2,G3,  G4,G5,G6,   G7,G8,G9 ]) #Matriz de Verdes
            MB = np.array( [ B1,B2,B3,  B4,B5,B6,   B7,B8,B9 ]) #Matriz de Azules
            
            MS = (  21, 31, 21,     31, 48, 31,    21, 31, 21)   #Matriz Suavizado
            
            RL = np.dot(MR, MS)                                 #Suavizado Rojos
            GL = np.dot(MG, MS)                                 #Suavizado Rojos
            BL = np.dot(MB, MS)                                 #Suavizado Rojos
            
            RL = int (RL * (1/256) )
            GL = int (GL * (1/256) )
            BL = int (BL * (1/256) )
            img.putpixel( (x,y),  (RL, GL, BL))
                        
    img.save("Imagen - Suavizado de Gauss.jpg")
    img3 = Image.open("Imagen - Suavizado de Gauss.jpg")
    Histograma( img3, "Suavizado de Gauss")
    
    img = img.resize( ( 345, 345), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30)
    panel.image = img    

def imgSuaLin():
    img = Image.open("Imagen - Original.jpg")
    img2 = Image.open("Imagen - Original.jpg")
    width, height = img.size
            
    for x in range( 1, (width - 1) ):
        for y in range( 1, (height - 1) ):            
            R1, G1, B1 = img2.getpixel(( x-1, y-1 ))
            R2, G2, B2 = img2.getpixel(( x,   y-1 ))
            R3, G3, B3 = img2.getpixel(( x+1, y-1 ))            
            R4, G4, B4 = img2.getpixel(( x-1, y   ))
            R5, G5, B5 = img2.getpixel(( x,   y   ))
            R6, G6, B6 = img2.getpixel(( x+1, y   ))            
            R7, G7, B7 = img2.getpixel(( x-1, y+1 ))
            R8, G8, B8 = img2.getpixel(( x,   y+1 ))
            R9, G9, B9 = img2.getpixel(( x+1, y+1 ))            
            TR = int ( (R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8 + R9)/9 )     #Total Rojo
            TG = int ( (G1 + G2 + G3 + G4 + G5 + G6 + G7 + G8 + G9)/9 )     #Total Verde
            TB = int ( (B1 + B2 + B3 + B4 + B5 + B6 + B7 + B8 + B9)/9 )     #Total Azul

            img.putpixel( (x,y),  (TR, TG, TB))
    
    img.save("Imagen - Suavizado Lineal.jpg")
    img3 = Image.open("Imagen - Suavizado Lineal.jpg")
    Histograma( img3, "Suavizado Lineal")
    
    img = img.resize( ( 345, 345 ), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place( x= 500, y=30 )
    panel.image = img 

def Histograma( imagen , titulo ):
    img3 = imagen    
    plt.clf()
    stats = []
    width, height = img3.size
    print(width)
    print(height)
    for x in range(width):
        for y in range(height):
            r,g,b = img3.getpixel((x,y))
            BN = int( r * 0.299) + int( g * 0.587 ) + int( b * 0.124 )
            pixelg = tuple( [ BN, BN, BN])
            stats.append( BN )
    img3 = img3.resize( ( 1, 1), Image.ANTIALIAS )
    Inicio  = 0
    Final   = 255    
    Espacio = np.linspace(Inicio, Final, round(1 + (Final - Inicio) / 5))
    plt.hist(stats, Espacio)    
    plt.savefig("Histograma - " + titulo + ".jpg")
    
    img2 = Image.open("Histograma - " + titulo + ".jpg")
    img2 = img2.resize( ( 345, 345), Image.ANTIALIAS )
    img2 = ImageTk.PhotoImage(img2)
    panel = Label( ventana, image = img2)
    panel.image = img2
    panel.place( x = 850, y = 30)
    panel.image = img2

def HistogramaLum( imagen , titulo ):
    img3 = imagen    
    plt.clf()
    stats = []
    width, height = img3.size
    print(width)
    print(height)
    for x in range(width):
        for y in range(height):
            r,g,b = img3.getpixel((x,y))
            BN = int( (r+g+b)/3 )
            stats.append( BN )
    img3 = img3.resize( ( 1, 1), Image.ANTIALIAS )
    Inicio  = 0
    Final   = 255    
    Espacio = np.linspace(Inicio, Final, round(1 + (Final - Inicio) / 5))
    plt.hist(stats, Espacio)    
    plt.savefig("Histograma - " + titulo + ".jpg")
    
    img2 = Image.open("Histograma - " + titulo + ".jpg")
    img2 = img2.resize( ( 345, 345), Image.ANTIALIAS )
    img2 = ImageTk.PhotoImage(img2)
    panel = Label( ventana, image = img2)
    panel.image = img2
    panel.place( x = 850, y = 30)
    panel.image = img2

ventana = Tk()
ventana.title(    "Practica 6")
ventana.geometry( "1225x410")
ventana.config(   bg = "black")

boton_Cargar = Button(ventana, text= "Seleccionar Imagen",  width = 16, command=imgMostrar ).place(x= 20, y= 30)
boton_BN     = Button(ventana, text= "Convertir a grises",  width = 16, command=imgBN      ).place(x= 20, y= 70)
boton_Color  = Button(ventana, text= "Remplazar color",     width = 16, command=imgColor   ).place(x= 20, y=110)
boton_Binar  = Button(ventana, text= "Convertir a binaria", width = 16, command=imgBinaria ).place(x= 20, y=150)
boton_Bordes = Button(ventana, text= "Detectar Bordes",     width = 16, command=imgBordes  ).place(x= 20, y=190)
boton_Invert = Button(ventana, text= "Invertir Colores",    width = 16, command=imgInvert  ).place(x= 20, y=230)   
boton_Laplac = Button(ventana, text= "Filtro Laplaciano",   width = 16, command=imgLaplac  ).place(x= 20, y=271) 
boton_SuaGau = Button(ventana, text= "Suavizado Gaussiano", width = 16, command=imgGauss   ).place(x= 20, y=312) 
boton_Sualin = Button(ventana, text= "Suavizado Linear",    width = 16, command=imgSuaLin  ).place(x= 20, y=353) 

ventana.mainloop()    