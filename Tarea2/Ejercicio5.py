"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
5.	Confeccione un programa que muestre un menú, 
con las opciones de calcular distancia, calcular tiempo, 
calcular velocidad, basado en los parámetros requeridos por el sistema 
y que muestra el resultado respectivo. (Formulas, V= d/t)  
"""
import MiModulo as MiM

def Menu():
        print(" ______________________________"'\n'
            "|  ¿ Que desea calcular?:     |"'\n'
            "|                             |"'\n'
            "| (1) Distancia               |"'\n'
            "| (2) Tiempo                  |"'\n'
            "| (3) Velocidad               |"'\n'
            "|_____________________________|"'\n')
        
        Seleccion=(input("¿Que operacion desea realizar?"'\n'))
        if Seleccion=="1":print("La distancia total es ",CalcuDistancia(),"m")
        elif Seleccion=="2":print("El tiempo total es ",CalcuTiempo(),"seg")
        elif Seleccion=="3":print("La velocidad total es ",CalcuVelocidad(),"seg")
        else:print("Seleccion Invalida")
               


def CalcuDistancia():
        print("Calcularemos la Distancia (D=V*T)")
        Milist=((MiM.IngresaDAto(2,"Velocidad(m/s)","Tiempo(seg)","")))
        resultado=Milist[0]*Milist[1]
        return resultado

def CalcuTiempo():
        print("Calcularemos el Tiempo (T=D/V)")
        Milist=((MiM.IngresaDAto(2,"Distancia(metros)","Velocidad(m/s)","")))
        resultado=Milist[0]/Milist[1]
        return resultado

def CalcuVelocidad():
        print("Calcularemos la Velocidad (V=D/T)")
        Milist=((MiM.IngresaDAto(2,"Distancia(metros)","Tiempo(seg)","")))
        resultado=Milist[0]/Milist[1]
        return resultado
Menu()

while MiM.Continuar():
    Menu()
                