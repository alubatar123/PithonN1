"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
1.Un programa que determina si un número es positivo o negativos
"""

#Importa el modulo Continuar
from MiModulo import Continuar as Cont

#boolean que nos permite detener el programa o ingresar mas numeros     
Validar=True

#funcion que pide ingresar el numero
def Validar():
    Numero=(input("Ingrese el numero: "))
    while True:
        #Ciclo que confirma si el dato es numerico
        try:
            #If que confirma si el numero es positivo o negativo
            if float(Numero)>0:
                print("Numero positivo")
                break
            
            else:
                print("Numero Negativo")
                break
        #Excepcion controlada en caso de ingresa un dato no numerico
        except ValueError:
            print("Valor invalido, intente de nuevo")
            Numero=input("Ingrese el numero: ")

#Ejecutamos la primer funcion del programa
Validar()

#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while Cont():
    Validar()

    
    
    