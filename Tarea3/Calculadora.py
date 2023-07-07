"""
Practica de evaluación corta 2
Curso Python Nivel 1
Autor Esteban Garro Echevarria

1.	Efectuar  un programa que efectué cálculos básicos de una calculadora
 con las siguientes operaciones recibiendo dos parámetros y el tipo de operación a realizar:
1.1.	Sumar       1.2.	Restar      1.3.	Multiplicar 1.4.	Dividir
1.5.	Potencia    1.6.	Raíz cuadrada   1.7.	Porcentaje

"""
#Importa modulo math y modulo creado Modulo
import math
import Modulo as MiM

def Menu():


    print(" ________________________________________"'\n'
        "|    Operaciones disponibles:            |"'\n'
        "|                                        |"'\n'
        "| (1) Suma             (5) Potencia      |"'\n'
        "| (2) Resta            (6) Raiz          |"'\n'
        "| (3) Multiplicacion   (7) Porcentaje    |"'\n'
        "| (4) Division                           |"'\n'
        "|________________________________________|"'\n')
    
    Seleccion=(input("¿Que operacion desea realizar?"'\n'))
    #Ofrece Menu que llama otras funciones  
    # Para Sumar, Restar, Multiplicar y Dividir se ofrece operacion con multiples num  
    if int(Seleccion)==1:Cantidad("sumar",1)
    if int(Seleccion)==2:Cantidad("restar",2)
    if int(Seleccion)==3:Cantidad("multiplicar",3)
    if int(Seleccion)==4:Cantidad("dividir",4)
    if int(Seleccion)==5:Potencia()
    if int(Seleccion)==6:Raiz()
    if int(Seleccion)==7:Porcentaje()
 
#Funcion que pregunta cuantas numeros va operar
def Cantidad(operacion,Selec):
    print()
    while True:
        try:
            Cant=int(input("¿Cuantos numeros desea "+operacion+"? "))
            if Cant<2:
                print("El minimo son 2 numeros")
                Cantidad(operacion,Selec)
            else:
                #Si se escogieron mas de 2 num, se llama a la siguiente funcion
                #dependiendo lo seleccionado en el Menu
                if Selec == 1: Sumar(Cant)
                if Selec == 2: Restar(Cant)
                if Selec == 3: Multip(Cant)
                if Selec == 4: Dividir(Cant)
            break    
        #try/except para prevenir formatos incorrectos
        except ValueError:  
            print("Valor incorrecto")  


def Sumar(Cant,Total=0,i=1):
    """
    Funcion que suma minimo 2 numeros
    Cant= Cant de numeros establecidos en la funcion Cantidad()
    Total=almacena el total sumado
    i= contador 
    """
    if Cant!=0:
            while True:
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))
                    #funcion recursiva para actualizar el total y volver a sumar                      
                    Sumar(Cant-1,(Total+Num),i+1)
                    break
                except ValueError:
                    print("Valor incorrecto")    
    else:
        #Se llama a la funcion Escribir para agregar resultados a un archivo .txt
        Result= ("El total de la suma es "+str(Total))
        print(Result)
        MiM.Escribir(Result)
            
def Restar(Cant,Total=0,i=1):
    """
    Funcion que resta minimo 2 numeros
    Cant= Cant de numeros establecidos en la funcion Cantidad()
    Total=almacena el total restado
    i= contador 
    """    
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Restar(Cant-1,(Num),i+1)             
                    else: Restar(Cant-1,(Total-Num),i+1)
                    break
                #try/except para prevenir formatos incorrectos
                except ValueError:
                    print("Valor incorrecto")    
    else: 
    #Se llama a la funcion Escribir para agregar resultados a un archivo .txt       
        Result= ("El total de la resta es "+str(Total))
        print(Result)
        MiM.Escribir(Result)
def Multip(Cant,Total=0,i=1):
    """
    Funcion que multiplica minimo 2 numeros
    Cant= Cant de numeros establecidos en la funcion Cantidad()
    Total=almacena el total mmultiplicado
    i= contador 
    """           
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Multip(Cant-1,(Num),i+1)             
                    else: Multip(Cant-1,(Total*Num),i+1)
                    break
                #try/except para prevenir formatos incorrectos
                except ValueError:
                    print("Valor incorrecto")    
    else:
         #Se llama a la funcion Escribir para agregar resultados a un archivo .txt
        Result= ("El total de la multiplicación es "+str(Total))
        print(Result)
        MiM.Escribir(Result)

def Dividir(Cant,Total=0,i=1):
    """
    Funcion que dvidie minimo 2 numeros
    Cant= Cant de numeros establecidos en la funcion Cantidad()
    Total=almacena el total dividido
    i= contador 
    """      
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Dividir(Cant-1,(Num),i+1) 
                #No se permite dividir entre 0
                    elif i!=1 and Num == 0:print("No se puede dividir entre cero")            
                    else:
                        Dividir(Cant-1,(Total/Num),i+1) 
                    break
                #try/except para prevenir formatos incorrectos
                except ValueError:
                    print("Valor incorrecto")    
    else: 
        #Se llama a la funcion Escribir para agregar resultados a un archivo .txt
        Result= ("El total de la division es "+str(Total))
        print(Result)
        MiM.Escribir(Result)

def Potencia():
    """
    Funcion que permite potenciar un numero a X exponente
    """
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Exp=float(input("Digite el exponente: "))                      
            break
        except ValueError:
            print("Valor incorrecto")    
    
    #Se llama a la funcion Escribir para agregar resultados a un archivo .txt   
    Result= ("El total de la potencia es "+str(Num**Exp))
    print(Result)
    MiM.Escribir(Result)

def Raiz():
    """
    Funcion que permite sacar la raiz de cualquier numero
    """
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Rad=float(input("Digite el radical: "))               
           #Se llama a la funcion Escribir para agregar resultados a un archivo .txt
            Result= ("La raiz total es "+str(math.pow(Num,1/Rad)))
            print(Result)
            MiM.Escribir(Result)                
            break
        except ValueError:
            print("Error. Revise formula: math.pow(x) donde x>= 0 ")    
    
    
def Porcentaje():
    """
    Funcion que permite sacar cualquier porcentaje de cualquier numero
    """
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Por=float(input("Digite el % deseado: ")) 
              #Se llama a la funcion Escribir para agregar resultados a un archivo .txt
            Result= (f"El {Por}% de {Num} es "+str(Num/100*Por)+"%")
            print(Result)
            MiM.Escribir(Result)                   
            break
        except ValueError:
            print("Valor incorrecto")              


Menu()
#Se llama a la funcion Continuar para seguir operando o cerrar programa
while MiM.Continuar():
    Menu()       