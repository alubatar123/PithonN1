import os


ruta='C:/Users/Chango/Desktop/Python/Curso/PithonN1/ProyectoFinal/'

def RevisaArchivo():
    if (os.path.exists('archivo.txt'))==True: #revisa si existe
        os.remove(ruta+'archivo.txt')
        CrearArchivo()
    else:
        CrearArchivo()

def CrearArchivo():
    archivo_texto=open(ruta+'archivo.txt','w') 
    archivo_texto.write("Titulo\n\nEsta es la linea 1\nEsta es la linea 2\nEsta es la linea 3\nEsta es la linea 4\nEsta es la linea 5")    
    archivo_texto.close()
    

def LeeArchivo():
    
    with open (ruta + "archivo.txt","r") as archivo: 
        Lista=list(archivo.readlines())  
    return Lista


def Actualiza(Lista):
    with open (ruta + "archivo.txt","w") as archivo:
        for x in Lista:
            archivo.write(x) 
