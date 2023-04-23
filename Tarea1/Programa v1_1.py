#Buenas Profesor,

 #Como tuvimos varios dias libres y ocupaba ir practicando otros conceptos, aproveche la tarea para incluir otras opciones. 

General_Boolean=False

DicEstu={}
#Menu principal del programa
def Menu():
    global General_Boolean
    global DicDatos
    while General_Boolean==False:
        print(" ______________________________________________"'\n'
               "|    Bienvenido a la Academia de Tecnologia    |"'\n'
               "|                                              |"'\n'               
               "| Seleccione una opcion:                       |"'\n'
               "|                                              |"'\n'
               "|   (1) Registrar Estudiante                   |"'\n'
               "|   (2) Revisar Estudiante                     |"'\n'
               "|______________________________________________|"'\n')
        
        Seleccion=(input("Seleccion: "))
        RevisaSeleccion(Seleccion,1,2)
#De acuerdo a la seleccion llama la funcion correspondiente
    General_Boolean=False  
    if int(Seleccion)==1: Registrar()
    if int(Seleccion)==2: RevisaRegistros()

#Funcion que revisar si el formato utilizado es valido para el Menu
def RevisaSeleccion(MI_Seleccion,Mi_A,Mi_B):
    global General_Boolean
    Mi_Check=MI_Seleccion.isnumeric()
#Solo permite numeros    
    if Mi_Check==False:
        print("\nFORMATO INCORRECTO, Trate de nuevo.\n")
        General_Boolean=False
        return General_Boolean   
#Imprime error si la seleccion no existe    
    elif float(MI_Seleccion) < float(Mi_A) or  float(MI_Seleccion) > float(Mi_B):
        print('\n'"Selecion Invalida, Trate de nuevo."'\n')
        General_Boolean=False
        return General_Boolean   
    else:
        General_Boolean=True
        return General_Boolean  

#Revisa si los datos para ingresar a los diccionarios son validos
def RevisaDatos(Tipo,Datos):
    global General_Boolean
    ListTemp=Datos.split()
    counter=0
#Separa Datos en lista para verificar su formato dependiendo el tipo de dato
    for eachelement in range(len(ListTemp)):
        if Tipo=="Alphabetic" and ListTemp[eachelement].isalpha():
            counter=counter+0

        elif Tipo=="AlphaNumeric" and ListTemp[eachelement].isalnum():
            counter=counter+0

        else:
            print("\nError. Caracteres invalidos\n")
            counter=counter+1

    if counter==0:
        General_Boolean=True
    

            
 
#confirma si se desea continuar o salir del programa
def Continuar():
    global General_Boolean

 #Crea una variable con la hora actual  
    from datetime import datetime
    now = datetime.now()
    HoraActual = now.strftime("%H:%M:%S")
    Cont_Boolean=False

#cancela el programa si se escoje N o n
    while Cont_Boolean==False:
        Seleccion=(input("\n¿Desea volver al menu principal? Y/N"'\n'))
        if Seleccion=="N" or Seleccion=="n":
            General_Boolean=True
            Cont_Boolean=True
            print('\n'"Gracias nos vemos pronto!"'\n',HoraActual)
            return General_Boolean
#continua el programa si se escoje Y o y        
        elif Seleccion=="Y" or Seleccion=="y":
            General_Boolean=False
            Cont_Boolean=True            
            return General_Boolean
        #Confirma que la opcion sea valida
        else:
            print('\n'"Ingrese unicamente 'Y' o 'N'"'\n')


#Toma datos para un nuevo registro
def Registrar():
    global DicDatos
    global General_Boolean
    print("\nParte 1 Ingrese los siguientes datos para un nuevo registro:\n")
    while General_Boolean==False:
        Apellido1=(input("Apellido 1: "))
        RevisaDatos("Alphabetic",Apellido1)

    General_Boolean=False
    while General_Boolean==False:    
        Apellido2=(input("Apellido 2: "))
        RevisaDatos("Alphabetic",Apellido2)

    General_Boolean=False
    while General_Boolean==False:
        Nombre=(input("Nombre: ")) 
        RevisaDatos("Alphabetic",Nombre) 

    print("\nParte 2 Ingrese los siguientes datos sobre la direccion fisica:\n")
    General_Boolean=False
    while General_Boolean==False:
        Provincia=(input("Provincia: "))
        RevisaDatos("Alphabetic",Provincia)

    General_Boolean=False
    while General_Boolean==False:
        Canton=(input("Canton: "))
        RevisaDatos("AlphaNumeric",Canton)

    General_Boolean=False
    while General_Boolean==False:
        Distrito=(input("Distrito: "))
        RevisaDatos("AlphaNumeric",Distrito)

    General_Boolean=False
    
    Direccion=(input("Direccion: "))
    

    print("\nParte 3 Datos extra\n")
    
    General_Boolean=False
    while General_Boolean==False:
        Profesion=(input("Profesion: "))
        RevisaDatos("Alphabetic",Profesion)

    General_Boolean=False
    while General_Boolean==False:
        Deporte=(input("Deporte Favorito: "))
        RevisaDatos("Alphabetic",Deporte)

    CrearRegistro(Nombre,Apellido1,Apellido2,Provincia,
                  Canton,Distrito,Direccion,Profesion,Deporte)

#toma los datos ingresados para crear entradas en el diccionarios de registro
def CrearRegistro(Nom,Ape1,Ape2,Prov,Cant,Dist,Dir,Prof,Dep):
        NumeroEstudiante=(int(len(DicEstu))+1)
        
        DicDatos ={"Nombre":Nom,"Apellido1":Ape1,"Apellido2":Ape2,
                     "Provincia":Prov,"Canton":Cant,"Distrito":Dist,
                     "Direccion":Dir,"Profesion":Prof,"Deporte":Dep}
        
        DicEstu[NumeroEstudiante]=DicDatos
        print("\nResgistro completo. ID estudiante: "+str(NumeroEstudiante),"\n")
#borra el Diccionario provisional para prevenir duplicados        
        del DicDatos

#Menu de acceso a estudiantes ya registrados
def RevisaRegistros():
    global General_Boolean
#Si el diccionario de Registro esta vacio, imprime error    
    Counter1=int(len(DicEstu))
    if Counter1 == 0:
        print("\nNo hay datos. Favor registrar estudiantes\n")
    else:
        print("\nRegistros disponibles: \n")
        y=0  
#Si existen datos imprime el ID del estudiante        
        while y < Counter1:
            milista = list(DicEstu.keys())[y]
            y=y+1
            print("ID ",str(milista),DicEstu[y]["Nombre"])
#opcion para ver mas detalles del estudiante            
        while General_Boolean==False:
            Selec=(input("\nDigite el ID del estudiante a revisar: "))
            if Selec.isnumeric()==False or (int(Selec)<0 or int(Selec)>Counter1):
                 print('\n'"Selecion Invalida, Trate de nuevo."'\n')
            else:                
                General_Boolean=True
                
        RevisaEstudiante(int(Selec))


#imprime las datos de registros existentes en un formato legible

def RevisaEstudiante(Sel):
    
    print("\nDatos del estudiante :",Sel,"\n" " Nombre: ",DicEstu[Sel]["Nombre"],
          DicEstu[Sel]["Apellido1"],DicEstu[Sel]["Apellido2"],"\n",
          "Direccion: ",DicEstu[Sel]["Direccion"],",",DicEstu[Sel]["Distrito"],","
          ,DicEstu[Sel]["Canton"],",",DicEstu[Sel]["Provincia"],"\n",
          "Profesion: ",DicEstu[Sel]["Profesion"],"\n",
          "Deporte: ",DicEstu[Sel]["Deporte"],"\n")

#loop que permite que el programa no se autocierre
while General_Boolean==False:
    Menu()
    Continuar()