"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
4.	Fórmula para sacar el resultado de la raíz de la suma de A más B dividiendo 
el resultado por C, con base a los valores ingresados por pantalla. 
Nota utilizar la función sqrt. 
"""
# import math module y MiModulo
import math
import MiModulo as MiM

#Funcion que calcula ((Raiz[A+B])/c)
def Calcular(a,b,c):
    print(a,b,c)
    try:
      Result=("El resultado de ((Raiz[A+B])/c): "+str((math.sqrt(a+b))/c))
      yield Result
    # Controla error math.sqrt(x) no soporta numeros negativos       
    except ValueError:
        Error="Error. Revise formula: math.sqrt(x) donde x>= 0 "
        yield Error

#Llama la funcion IngresaDatos de MiModulo        
def VerificaValores():
    Milist=((MiM.IngresaDAto(3,"a","b","c")))
    #Llama la funcion Calcular
    print(next(Calcular(Milist[0],Milist[1],Milist[2])))


#Inicia el programa con la funcion VerificaValores
VerificaValores()

#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while MiM.Continuar():
    VerificaValores()
    