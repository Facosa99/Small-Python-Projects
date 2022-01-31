from array import *

global matrizor, w1, w2, umbral, factor
matrizor = [    [0,0,0],    [0,1,1],    [1,0,1],    [1,1,1]     ]

def Perceptron():  
    global matrizor, w1, w2, umbral, factor
    for x in range (4):
        x1 = matrizor[x][0]
        x2 = matrizor[x][1]
        a  = matrizor[x][2]                
        Z1 = (w1*x1) + (w2*x2) - umbral        
        if Z1 <= 0:
            Z2 = 0
        else:
            Z2 = 1            
    if Z2 != a:
        error = a-Z1
        umbral = -(factor*error)
        w1 = (factor*error*x1)
        w2 = (factor*error*x2)
        x-=1
        print( "A vale: " + a  )
        print( "Z vale: " + Z2 )

print("Ingresa valor 1")
w1     = float( input() )
print("Ingresa valor 2")
w2     = float( input() )
print("Ingresa el umbral")
umbral = float( input() )
nu = umbral
print("Ingresa el factor")
factor = float( input() )
    
print( "W1:     "   + str(w1)     )
print( "W2:     "   + str(w2)     )
print( "Umbral: "   + str(umbral) )
print( "Factor: "   + str(factor) )    
Perceptron()