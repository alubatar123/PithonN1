"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
6.	Un programa que imprima en pantalla el producto del multiplicador indicado,
hasta el multiplicando dado por el usuario. (Tabla de multiplicar).  
"""

import MiModulo as MiM

def CrearTabla(Multiplicador,Multiplicando):
    """
    Funcion que permite crear una tabla de multiplicar
    """
    if Multiplicando<0:
        print("Error, el multiplicador debe ser positivo")
    else:
         for i in range(Multiplicando):
             print(int(i)+1,"x",Multiplicador,"=",(int(i)+1)*Multiplicador)
        


def VerificaValores():
    Milist=((MiM.IngresaDAto(2,"Multiplicador","Cant Multiplicandos","")))
    #Llama la funcion CalcularDiscriminante
    (CrearTabla(int(Milist[0]),int(Milist[1])))

VerificaValores()
#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while MiM.Continuar():
    VerificaValores()