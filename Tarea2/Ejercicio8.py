"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
8.	Realice un programa que administre una lista en la cual pueda ingresar los nombres
de personas y que se pueda eliminar el primero o el último de la lista
"""
import time
#variable global de lista de personas
PersList=[]

def Menu():
        """
        Menu de opciones de registro o borrado
        """
        while True:
            print(" ______________________________"'\n'
                "| (1) Registrar               |"'\n'
                "| (2) Borrar Primero          |"'\n'
                "| (3) Borrar Ultimo           |"'\n'
                "| (4) Salir                   |"'\n'
                "|_____________________________|"'\n')
            #pide una opcion al usuario
            Seleccion=(input("¿Que operacion desea realizar?"'\n'))
            #depende la opcion se llama siguiente funcion
            if Seleccion=="1":
                Registro() 
                break
            elif Seleccion=="3":
                BorrarUltimo()
                break
            elif Seleccion=="2":
                BorrarPrimero()
                break
            elif Seleccion=="4":
                print("Vuelva pronto!")
                break
            #manejo de opciones invalida
            else:print("Seleccion Invalida")


def Registro():
    """
    Funcion que permite registra un usuario nuevo
    """
    Siguiente=True
    while Siguiente:
        #Agrega nuevo valor a lista
        PersList.append(input("Digite el nombre a registrar: "))
                 
        while (True):   
            Confirmar=input("Registrar otro nombre?(y/n) ")  
            #confirma si se desea hacer otro registro   
            if Confirmar=="y" or Confirmar=="Y":
                Siguiente=True
                break #break que cierra while anidado
            elif Confirmar=="n" or Confirmar=="N":
                Siguiente=False
                break #break que cierra while anidado
                #Si el usuario ingresa Otro dato, se muestra error           
            else:
                print("Opcion Invalida")
             
    print("Lista actual:\n",PersList)
    Menu() 

def BorrarUltimo():
    """
    funcion que permite borrar ultimo valor de la lista
    """
    try:
        print("El elemento ",PersList[-1]," fue borrado")
        PersList.pop()
        print("Lista actual:\n",PersList) 
    except IndexError: #manejo de errores para listas vacias
        print("No hay datos que borrar. Regresando al Menu Principal")
        print("2s"),time.sleep(1),print("1s"),time.sleep(1)     
    Menu() 

def BorrarPrimero():
    """
    funcion que permite borrar primer valor de la lista
    """
    try:
        print("El elemento ",PersList[0]," fue borrado")
        PersList.pop(0)
        print("Lista actual:\n",PersList)
          
    except IndexError: #manejo de errores para listas vacias
        print("No hay datos que borrar. Regresando al Menu Principal") 
        print("2s"),time.sleep(1),print("1s"),time.sleep(1)    
    Menu()

Menu() #inicia programa
