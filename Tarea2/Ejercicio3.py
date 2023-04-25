"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
2.	3.	Realice un programa para obtener el resultado de la fórmula del discriminante,
según los datos dados por el usuario. Formula b2 - 4 a*c 
"""
# import MiModulo
import MiModulo as MiM

def CalcularDiscriminante(a,b,c):
    """
    Generador para calcular el discriminante
    """
    dis=("El resultado de la fórmula del discriminante es: "+str((b**2)-4*a*c))
    yield dis


def VerificaValores():
    Milist=((MiM.IngresaDAto(3,"a","b","c")))
    #Llama la funcion CalcularDiscriminante
    print(next(CalcularDiscriminante(Milist[0],Milist[1],Milist[2])))

VerificaValores()
#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while MiM.Continuar():
    VerificaValores()

          