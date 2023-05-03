import math

def Menu():
    #global General_Boolean
    #while General_Boolean==False:

    print(" ________________________________________"'\n'
        "|    Operaciones disponibles:            |"'\n'
        "|                                        |"'\n'
        "| (1) Suma             (5) Potencia      |"'\n'
        "| (2) Resta            (6) Raiz          |"'\n'
        "| (3) Multiplicacion   (7) Porcentaje    |"'\n'
        "| (4) Division                           |"'\n'
        "|________________________________________|"'\n')
    
    Seleccion=(input("¿Que operacion desea realizar?"'\n'))
        

    #General_Boolean=False
 #dependiendo la seleccion se llama a la funcion correspondiente  
    if int(Seleccion)==1:Cantidad("sumar",1)
    if int(Seleccion)==2:Cantidad("restar",2)
    if int(Seleccion)==3:Cantidad("multiplicar",3)
    if int(Seleccion)==4:Cantidad("dividir",4)
    if int(Seleccion)==5:Potencia()
    if int(Seleccion)==6:Raiz()
    if int(Seleccion)==7:Porcentaje()
 

def Cantidad(operacion,Selec):
    print()
    while True:
        try:
            Cant=int(input("¿Cuantos numeros desea "+operacion+"? "))
            if Cant==1:
                print("El minimo son 2 numeros")
                Cantidad(operacion,Selec)
            else:
                if Selec == 1: Sumar(Cant)
                if Selec == 2: Restar(Cant)
                if Selec == 3: Multip(Cant)
                if Selec == 4: Dividir(Cant)
            break    
        except ValueError:  
            print("Valor incorrecto")  


def Sumar(Cant,Total=0,i=1):
    if Cant!=0:
            while True:
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))                      
                    Sumar(Cant-1,(Total+Num),i+1)
                    break
                except ValueError:
                    print("Valor incorrecto")    
    else:
        print ("El total de la suma es",Total)
            
def Restar(Cant,Total=0,i=1):
    
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Restar(Cant-1,(Num),i+1)             
                    else: Restar(Cant-1,(Total-Num),i+1)
                    break
                except ValueError:
                    print("Valor incorrecto")    
    else:
        print ("El total de la resta es",Total)

def Multip(Cant,Total=0,i=1):
    
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Multip(Cant-1,(Num),i+1)             
                    else: Multip(Cant-1,(Total*Num),i+1)
                    break
                except ValueError:
                    print("Valor incorrecto")    
    else:
        print ("El total de la multiplicación es",Total)   

def Dividir(Cant,Total=0,i=1):
    
    if Cant!=0:
            while True:                
                try:
                    Num=float(input("Digite el numero "+str(i)+": "))  
                    if i==1: Dividir(Cant-1,(Num),i+1) 
                    elif i!=1 and Num == 0:print("No se puede dividir entre cero")            
                    else:
                        Dividir(Cant-1,(Total/Num),i+1) 
                        break
                except ValueError:
                    print("Valor incorrecto")    
    else:
        print ("El total de la division es",Total)   


def Potencia():
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Exp=float(input("Digite el exponente: "))                      
            break
        except ValueError:
            print("Valor incorrecto")    
    
    print ("El total es ",Num**Exp)


def Raiz():
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Rad=float(input("Digite el radical: "))    
            print ("El raiz total es ",math.pow(Num,1/Rad))                  
            break
        except ValueError:
            print("Error. Revise formula: math.pow(x) donde x>= 0 ")    
    
    
def Porcentaje():
    while True:
        try:
            Num=float(input("Digite el numero: "))
            Por=float(input("Digite el % deseado: "))    
            print (f"El {Por}% de {Num} es ",Num/100*Por,"%")                  
            break
        except ValueError:
            print("Valor incorrecto")              


Menu()       