"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
5.	Confeccione un programa que muestre un menú, 
con las opciones de calcular distancia, calcular tiempo, 
calcular velocidad, basado en los parámetros requeridos por el sistema 
y que muestra el resultado respectivo. (Formulas, V= d/t)  
"""
# import MiModulo
import MiModulo as MiM

#funcion que muestra un Menu de opciones
def Menu():
        print(" ______________________________"'\n'
            "|  ¿ Que desea calcular?:     |"'\n'
            "|                             |"'\n'
            "| (1) Distancia               |"'\n'
            "| (2) Tiempo                  |"'\n'
            "| (3) Velocidad               |"'\n'
            "|_____________________________|"'\n')
        #pide una opcion al usuario
        Seleccion=(input("¿Que operacion desea realizar?"'\n'))
        #depende la opcion se llama siguiente funcion
        if Seleccion=="1":print("La distancia total es ",CalcuDistancia(),"m")
        elif Seleccion=="2":print("El tiempo total es ",CalcuTiempo(),"seg")
        elif Seleccion=="3":print("La velocidad total es ",CalcuVelocidad(),"seg")
        #manejo de opciones invalida
        else:print("Seleccion Invalida")
               


def CalcuDistancia():
        """
        funcion que calcula Distancia (D=V*T)
        """
        print("Calcularemos la Distancia (D=V*T)")
        #llama la funcion IngresaDato de MiModulo para verificar valores validos
        Milist=((MiM.IngresaDAto(2,"Velocidad(m/s)","Tiempo(seg)","")))
        resultado=Milist[0]*Milist[1]
        return resultado


def CalcuTiempo():
        """
        funcion que calcula Tiempo (T=D/V)
        """
        print("Calcularemos el Tiempo (T=D/V)")
        #llama la funcion IngresaDato de MiModulo para verificar valores validos
        Milist=((MiM.IngresaDAto(2,"Distancia(metros)","Velocidad(m/s)","")))
        resultado=Milist[0]/Milist[1]
        return resultado


def CalcuVelocidad():
        """
        funcion que calcula Velocidad (V=D/T)
        """
        print("Calcularemos la Velocidad (V=D/T)")
        #llama la funcion IngresaDato de MiModulo para verificar valores validos
        Milist=((MiM.IngresaDAto(2,"Distancia(metros)","Tiempo(seg)","")))
        resultado=Milist[0]/Milist[1]
        return resultado

Menu()
while MiM.Continuar():
    Menu()
                