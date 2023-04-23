"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
1.	Un programa que determina si un número es positivo o negativo
"""

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

#Funcion que permite que el programa no se detenga hasta confirmar
def Continuar():
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("Desea tratar otro numero?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            Validar()
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
            #Si el usuario ingresa Otro dato, se muestra error           
        else:
            print("Opcion Invalida")
    
#Llamamos a ambas funciones
Validar()
Continuar()