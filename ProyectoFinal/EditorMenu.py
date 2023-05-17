"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
Proyecto Final. Editor Texto

Confeccionar un pequeño editor de texto en el cual se puedan realizar las siguientes operaciones:
a.	Crear archivo de texto y guardar en disco duro. Valor 4 pts.
b.	Escribir n cantidad de línea de texto digitada por el usuario, mínimo 5 líneas digitadas. Valor 10 pts.
c.	Permitir crear título centrado. Valor 4 pts.
d.	Alineación a la izquierda y a la derecha. Valor 6 pts.
e.	Convertir una línea o el texto completo de mayúscula a minúscula y viceversa. Valor 6 pts.
f.	Buscar palabra especifica. Valor 5 pts.
g.	Cortar y pegar texto. Valor 6 pts.
h.	Eliminar texto.  Valor 4 pts.

"""
#Se importa el Modulo ModuloConexion para verificacion de archivo
# Se importa el modulo EditorOper quien realiza las funciones especificas
from ModuloConexion import RevisaArchivo
import EditorOper as EP

#Menu del usuario
def Menu():
    print(" _______________________________________"'\n'
        "|      Operaciones disponibles:         |"'\n'
        "|                                       |"'\n'
        "| (1) Formato Titulo   (5) Minusculas   |"'\n'
        "| (2) Alinear Izq      (6) Buscar       |"'\n'
        "| (3) Alinear Der      (7) Mover        |"'\n'
        "| (4) Mayúsculas       (8) Borrar       |"'\n'
        "|_______________________________________|"'\n')
#cada opcion llama a la  funcion especifica       
    Seleccion=(input("¿Que operación desea realizar? "))
    if Seleccion =="1":EP.CentrarTitulo()
    elif Seleccion =="2":EP.AlineaIzq()
    elif Seleccion =="3":EP.AlineaDer()
    elif Seleccion =="4":EP.MayusculaMenu()
    elif Seleccion =="5":EP.MinusculaMenu()
    elif Seleccion =="6":EP.Buscar()
    elif Seleccion =="7":EP.Mover()
    elif Seleccion =="8":EP.Borrar()  
    else: print ("Opción Invalida")

def Cont():
    """
    Funcion que permite cancelar o seguir el programa retorando True para Yes, False para No
    """
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("\nDesea volver al menu?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            return True
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
            #Si el usuario ingresa Otro dato, se muestra error           
        else:
            print("Opcion Invalida")

#Se llama la funcion que verifica si el archivo ya existe o si debe ser creado
RevisaArchivo()
Menu() 
#Ciclo infinito que permite que el programa no se detenga hasta que se le indique
while Cont():
    Menu()    
       