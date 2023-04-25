"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
2.	Un programa que determina si un número es par o impar. Utilizar el mod o %. 
"""
# import MiModulo
import MiModulo as MiM
def VerificaNumero(Dato):
    """
    funcion que pide un dato y verifica si el numero
    es par o impar segun el remanente de la división
    """    
    if(Dato%2==0):
        print(f"El numero ",Dato," es par")
    else:
        print(f"El numero ",Dato," es impar")

 #Llama la funcion IngresaDatos de MiModulo      
def VerificaValores():
    Milist=((MiM.IngresaDAto(1,"el numero","","")))
    #Llama la funcion VerificaNumero
    VerificaNumero(Milist[0])


VerificaValores()
#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while MiM.Continuar():
    VerificaValores()