"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
4.	Fórmula para sacar el resultado de la raíz de la suma de A más B dividiendo 
el resultado por C, con base a los valores ingresados por pantalla. 
Nota utilizar la función sqrt. 
"""
# import math module
import math

#Funcion que calcula ((Raiz[A+B])/c)
def Calcular(a,b,c):
    try:
      Result=("El resultado de ((Raiz[A+B])/c): "+str((math.sqrt(a+b))/c))
      yield Result
    # Controla error math.sqrt(x) no soporta numeros negativos       
    except ValueError:
        Error="Error. Revise formula: math.sqrt(x) donde x>= 0 "
        yield Error
        
def IngresaDAto():
    
    Valores=[]
    Datos=["a","b","c"]
    i=0
    #funcion que pide el dato a verificar
    
    while i<3:
        Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
        while True:
            #Llama VerificaNumero siempre que el dato ser numerico
            try:
                Valores.append(float(Numero))           
                i+=1
            #Excepcion controlada en caso de ingresar un dato no numerico
                break
            except ValueError:
                print("Valor invalido, intente de nuevo")
                Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
    #Almacenamos el resultado del generador en el iterador Migenerador                 
    Migenerador=(Calcular(Valores[0],Valores[1],Valores[2]))
    print(next(Migenerador))
    #print(Migenerador)

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
    