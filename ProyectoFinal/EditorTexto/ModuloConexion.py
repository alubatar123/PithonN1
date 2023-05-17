#importa la libreria OS para conexiones de archivos
import os

#ruta donde se almacena el archivo de texto
ruta='C:/Users/Chango/Desktop/Python/Curso/PithonN1/ProyectoFinal/EditorTexto/'

#funcion que confirma si el archivo ya existe. De existir ya, este sera borrado y recreado desde 0
def RevisaArchivo():
    if (os.path.exists('archivo.txt'))==True: #revisa si existe
        os.remove(ruta+'archivo.txt')
        CrearArchivo()
    else:
        CrearArchivo()

#funcion que permite crear el archivo
def CrearArchivo():
    archivo_texto=open(ruta+'archivo.txt','w') 
    archivo_texto.write("What Is Artificial Intelligence (Ai)?\n\n"
                        "Artificial intelligence (AI) refers to the simulation of human intelligence by software-coded heuristics. Nowadays this code is prevalent in everything enterprise and firmware\n"
                        "Nowadays this code is prevalent in everything from cloud-based, enterprise applications to consumer apps and even embedded firmware.\n"
                        "The year 2022 brought AI into the mainstream through widespread familiarity with applications of Generative Pre-Training Transformer.\n"
                        "The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal.\n"
                        "Deep learning techniques enable this automatic learning through the absorption of huge amounts of unstructured data such as text, images, or video.\n")    
    archivo_texto.close()
    
#funcion que permite pasar el texto a una lista
def LeeArchivo():
    
    with open (ruta + "archivo.txt","r") as archivo: 
        Lista=list(archivo.readlines())  
    return Lista

#funcion que permite actualizar el texto
def Actualiza(Lista):
    with open (ruta + "archivo.txt","w") as archivo:
        for x in Lista:
            archivo.write(x) 
