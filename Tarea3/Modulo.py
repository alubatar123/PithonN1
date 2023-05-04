"""
Practica de evaluación corta 2
Curso Python Nivel 1
Autor Esteban Garro Echevarria

2.	Un programa que almacene en un archivo de texto las operaciones con los 
resultados del punto anterior y que se puede leer lo guardado en el archivo.

"""

import os
import errno
from datetime import datetime
    
def Continuar():
    """
    Funcion que permite cancelar o seguir el programa retorando True para Yes, False para No
    """
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("¿Desea realizar otra operación?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            return True
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
            #Si el usuario ingresa Otro dato, se muestra error           
        else:
            print("Opcion Invalida")

def Escribir(Resultado):  
    now = datetime.now()
    HoraActual = now.strftime("%H:%M:%S") 
    with open ("C:/Users/Chango/Desktop/Python/Curso/PithonN1/Tarea3/Resultados.txt","a+") as archivo:        
        archivo.write(HoraActual+" "+Resultado+"\n")
