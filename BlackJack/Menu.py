import time
from Usuarios import Usuario
from Juego import Comienza, NuevaBaraja

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
    print("\n===========================================\n")     
    TempDicUser,TempDicNom=User.BuscaUsuario()     
    if len(TempDicUser)==0:
        print("No aun registros. Regresando al menu"),time.sleep(1)
        Menu()
    else:       
        try:           
            Seleccion=(input("\n===========================================\nSeleccion el ID del usuario? "))
            if Seleccion.upper() == "R":
                Menu()             
            elif int(Seleccion) in TempDicUser:
                NuevaBaraja()
                Comienza([TempDicUser[int(Seleccion)],TempDicNom[int(Seleccion)]])
                Menu()        
        except SyntaxError:
            print("Opcion invalida. Regresando al menu principal..."),time.sleep(2)
            Menu()  

           
def VerRegistros():
    OB=Usuario()
    TempDicUser,TempDicNom=OB.BuscaUsuario() 
    
    if len(TempDicNom)==0:
        print("No aun registros. Regresando al menu"),time.sleep(1)
        Menu() 
    else:      
        try:
            Seleccion=(input("\n===========================================\nSeleccion el ID del usuario? "))
            if Seleccion.upper() == "R":
                Menu()             
            elif int(Seleccion) in TempDicUser:        
                print("\n===========================================\nEstadisticas de Usuario\n")        
                Stats=OB.StatUser(TempDicUser[int(Seleccion)])
                print(" Nombre =",Stats[0],"\n",
                    "GANES =",Stats[1],"\n",
                    "DERROTAS =",Stats[2],"\n",
                    "EMPATES =",Stats[3])  
                print("\n===========================================\nRegresando al menu principal..."),time.sleep(3)
                Menu()    
        except: 
            print("\nOpcion invalida. Regresando al menu"),time.sleep(1)
            Menu()      
        
def Registrar():
    OB=Usuario()
    existe, NuevoUserList=OB.Registrar()
    if existe == False:
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
        NuevaBaraja()
        Comienza(NuevoUserList)
        Menu()

    

     
Menu()     