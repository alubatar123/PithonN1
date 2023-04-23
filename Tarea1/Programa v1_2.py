#Buenas Profesor,

# Como tuvimos varios dias libres y ocupaba ir practicando otros conceptos, aproveche la tarea para incluir otras opciones. 

General_Boolean=False
#Funcion para accesar al menu de operaciones
def Menu():
    global General_Boolean
    while General_Boolean==False:

        print(" ___________________________________________"'\n'
            "|    Operaciones disponibles:                |"'\n'
            "|                                            |"'\n'
            "| (1) Suma             (5) Exponente         |"'\n'
            "| (2) Resta            (6) Division          |"'\n'
            "| (3) Negacion         (7) Division Entera   |"'\n'
            "| (4) Multiplicacion   (8) Modulo            |"'\n'
            "|____________________________________________|"'\n')
        
        Seleccion=(input("¿Que operacion desea realizar?"'\n'))
        RevisaNumero(Seleccion,1,8)

    General_Boolean=False
 #dependiendo la seleccion se llama a la funcion correspondiente  
    if int(Seleccion)==1:print("\nEl resultado es: ",sumar())
    if int(Seleccion)==2:print("\nEl resultado es: ",restar())
    if int(Seleccion)==3:print("\nEl resultado es: ",Negacion())
    if int(Seleccion)==4:print("\nEl resultado es: ",Multiplica())
    if int(Seleccion)==5:print("\nEl resultado es: ",Exponer())
    if int(Seleccion)==6:print("\nEl resultado es: ",Division())
    if int(Seleccion)==7:print("\nEl resultado es: ",DivisionEntera()) 
    if int(Seleccion)==8:print("\nEl resultado es: ",Modulo())  
#Funcion para continuar con mas operaciones o finalizar el programa        
def Continuar():
    global General_Boolean
 #Crea una variable con la hora actual  
    from datetime import datetime
    now = datetime.now()
    HoraActual = now.strftime("%H:%M:%S")
    Cont_Boolean=False
#cancela el programa si se escoje N o n
    while Cont_Boolean==False:
        Seleccion=(input("¿Desea continuar? Y/N"'\n'))
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



#Funcion que revisar si el formato utilizado es valido
def RevisaNumero(MI_Seleccion,Mi_A,Mi_B):
    global General_Boolean
    Mi_Check=MI_Seleccion.isnumeric()
    if Mi_Check==False:
        print("\nFORMATO INCORRECTO, Trate de nuevo.\n")
        General_Boolean=False
        return General_Boolean   
    elif float(MI_Seleccion) < float(Mi_A) or  float(MI_Seleccion) > float(Mi_B):
        print('\n'"Selecion Invalida, Trate de nuevo."'\n')
        General_Boolean=False
        return General_Boolean   
    else:
        General_Boolean=True
        return General_Boolean 
        
 #funcion para sumar
def sumar ():
    global General_Boolean
    print('\n'"Sumaremos 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)+int(Seleccion2)     
    return resultado
 #funcion para restar
def restar ():
    global General_Boolean
    print('\n'"Restaremos 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)-int(Seleccion2)     
    return resultado
 #funcion para multiplicar
def Multiplica ():
    global General_Boolean
    print('\n'"Multiplicaremos 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)*int(Seleccion2)     
    return resultado
 #funcion para negar
def Negacion ():
    global General_Boolean
    print('\n'"Negaremos 1 numero enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False 
    resultado=-int(Seleccion1)     
    return resultado

 #funcion para dividir
def Division ():
    global General_Boolean
    print('\n'"Dividiremos 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)/int(Seleccion2)     
    return resultado
 #funcion para division entera
def DivisionEntera ():
    global General_Boolean
    print('\n'"Dividiremos de forma entera 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)//int(Seleccion2)     
    return resultado
 #funcion para Exponentes
def Exponer ():
    global General_Boolean
    print('\n'"Potenciaremos 1 numero entero unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Exponente: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)**int(Seleccion2)     
    return resultado

 #funcion para Modulos
def Modulo ():
    global General_Boolean
    print('\n'"Obtendremos el modulo de 2 numeros enteros unicamente:"'\n')
    
    while General_Boolean==False:
        Seleccion1=(input("Numero 1: "'\n'))
        RevisaNumero(Seleccion1,1,float('inf'))
    
    General_Boolean=False
    while General_Boolean==False:
        Seleccion2=(input("Numero 2: "'\n'))
        RevisaNumero(Seleccion2,1,float('inf'))  

    General_Boolean=False 
    resultado=int(Seleccion1)%int(Seleccion2)     
    return resultado

 #condicional para accesar al programa y/o finalizarlo
while General_Boolean==False:
    Menu()
    Continuar()