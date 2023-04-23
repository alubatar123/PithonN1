"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
2.	Un programa que determina si un número es par o impar. Utilizar el mod o %. 
"""

def VerificaNumero(Dato):
    #funcion que pide un dato y verifica si el numero
    #  es par o impar segun el remanente de la división
    if(Dato%2==0):
        print(f"El numero ",Dato," es par")
    else:
        print(f"El numero ",Dato," es impar")

def IngresaDAto():
    #funcion que pide el dato a verificar
    Numero=(input("Ingrese el numero: "))
    while True:
        #Llama VerificaNumero siempre que el dato ser numerico
        try:
            VerificaNumero(float(Numero))
        #Excepcion controlada en caso de ingresar un dato no numerico
            break
        except ValueError:
            print("Valor invalido, intente de nuevo")
            Numero=input("Ingrese el numero: ")        

def Continuar():
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("Desea tratar otro numero?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            IngresaDAto()
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
    #Si el usuario ingresa Otro dato, se muestra error         
        else:
            print("Opcion Invalida")

IngresaDAto()
Continuar()