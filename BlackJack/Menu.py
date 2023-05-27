import time
from Usuarios import Usuario

#menu principal del juego
def Menu():
    print(" _________________________________"'\n'
        "|    Bienvenido a BlackJack:      |"'\n'
        "|                                 |"'\n'
        "| (1) Jugar                       |"'\n'
        "| (2) Ver registros               |"'\n'
        "| (3) Salir                       |"'\n'
        "|_________________________________|"'\n')
    
#cada opcion llama a la  funcion especifica       
    Seleccion=(input("¿Que operación desea realizar? "))
    if Seleccion =="1":ValidarUsuario()
    elif Seleccion =="2":VerRegistros()
    elif Seleccion =="3":print("\nGracias vuelva pronto\n")
    else:
        print("Opcion Invalida") 
        Menu()
         
    
#menu de validcion de usuarios
def ValidarUsuario():
        print(" _______________________________"'\n'
        "| (1) Usuario Existente         |"'\n'
        "| (2) Nuevo Usuario             |"'\n'
        "| (3) Volver al Menu            |"'\n'
        "|_______________________________|"'\n')
        Seleccion=(input("¿Que operación desea realizar? "))
        if Seleccion =="1":ListarUsuario()
        elif Seleccion =="2":Registrar()
        elif Seleccion =="3":Menu()
        else:
            print("Opcion Invalida") 
            Menu()
         

#crea una lista de los usuarios existentes    
def ListarUsuario(): 
    User=Usuario()       
    TempDic=User.BuscaUsuario() 
    Seleccion=(input("\nSeleccion el ID del usuario? "))
    if Seleccion.upper() == "R":
         Menu()             
    elif int(Seleccion) in TempDic:
         print("yes") 

           
def VerRegistros():
    User=Usuario()
    TempDic=User.BuscaUsuario()
    Seleccion=(input("\nSeleccion el ID del usuario? "))
    OB=Usuario()
    try:
        if Seleccion.upper() == "R":
            Menu()             
        elif int(Seleccion) in TempDic:
            print("\nEstadisticas de Usuario\n")        
            OB.StatUser(TempDic[int(Seleccion)])  
            print("\nRegresando al menu principal..."),time.sleep(3)
            Menu()    
    except: 
        print("\nOpcion invalida. Regresando al menu"),time.sleep(1)
        Menu()      
     
def Registrar():
    OB=Usuario()
    if OB.Registrar() == False:
        Select=input("¿Desea tratar de nuevo? Y/N ")
        if Select.lower() == "y":
            Registrar()
        elif Select.lower() == "n":
            print("\nRegresando al menu principal..."),time.sleep(3)
            Menu() 
        else:
            print("\nOpcion invalida. Regresando al menu"),time.sleep(1)
            Menu()     
    else:
        print("fine")

    

     
Menu()     