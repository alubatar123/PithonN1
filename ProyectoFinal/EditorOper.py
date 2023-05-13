
ArchivoLista=[]

import ModuloConexion as MC




def ImprimeTexto(Lista):
    print("===============================TEXTO ACTUAL=================================")
    print(Lista[0])    
    for x in (Lista[2:(len(Lista)+1)]):                   
        print(x,end="") 
    print("\n================================FIN DE TEXTO=================================")


def CentrarTitulo():
    Lista=MC.LeeArchivo()  
    Lista[0]=Lista[0].title()
    ImprimeTexto(Lista)
    MC.Actualiza(Lista)
  

def AlineaIzq():
    Lista=MC.LeeArchivo()  
    Counter=1
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    try:    
        Linea=int(input("\n\n¿Cúal linea desea alinear a la izquierda? "))
        Lista[Linea+1]=Lista[Linea+1].ljust(5+len(Lista[Linea+1]),"*")        
        MC.Actualiza(Lista)
        Lista=MC.LeeArchivo() 
        ImprimeTexto(Lista)
    except:
        print("Valor Invalido")

def AlineaDer():
    Lista=MC.LeeArchivo()  
    Counter=1
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    try:    
        Linea=int(input("\n\n¿Cúal linea desea alinear a la derecha? "))
        Lista[Linea+1]=Lista[Linea+1].rjust(5+len(Lista[Linea+1]),"*")        
        MC.Actualiza(Lista)
        Lista=MC.LeeArchivo() 
        ImprimeTexto(Lista)
    except:
        print("Valor Invalido")


def MayusculaMenu():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")
    print("  Opciones Para Mayúsculas\n\n[1] Todo el texto\n[2] El Título\n"
            "[3] Solo los párrafos\n[4] Solo una linea\n")
    Select=input("Seleccione una opción: ")
    
    if Select=="1":Mayuscula(Lista,0,(len(Lista)+1),0)
    elif Select=="2":Mayuscula(Lista,0,1,0)
    elif Select=="3":Mayuscula(Lista,2,(len(Lista)+1),2)
    elif Select=="4":
        Counter=1
        for x in (Lista[2:(len(Lista)+1)]):                   
            print("Linea[",Counter,"]",x,end="")
            Counter+=1 
        try:    
            Linea=int(input("\n\n¿Cúal linea desea pasar a Mayúscula? "))
            if Linea+2>len(Lista):
                print("Valor Invalido")
            else:Mayuscula(Lista,Linea+1,(Linea+2),Linea+1)               
        except:
            print("Valor Invalido")                 
    else: print("Valor Invalido")

def Mayuscula(Lista,A,B,Counter):
    
    for x in (Lista[A:B]):                   
        Lista[Counter]=Lista[Counter].upper()
        Counter+=1
    MC.Actualiza(Lista)
    Lista=MC.LeeArchivo()
    ImprimeTexto(Lista)

def MinusculaMenu():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")
    print("  Opciones Para Minúsculas\n\n[1] Todo el texto\n[2] El Título\n"
            "[3] Solo los párrafos\n[4] Solo una linea\n")
    Select=input("Seleccione una opción: ")
    
    if Select=="1":Minuscula(Lista,0,(len(Lista)+1),0)
    elif Select=="2":Minuscula(Lista,0,1,0)
    elif Select=="3":Minuscula(Lista,2,(len(Lista)+1),2)
    elif Select=="4":
        Counter=1
        for x in (Lista[2:(len(Lista)+1)]):                   
            print("Linea[",Counter,"]",x,end="")
            Counter+=1 
        try:    
            Linea=int(input("\n\n¿Cúal linea desea pasar a Minúsculas? "))
            if Linea+2>len(Lista):
                print("Valor Invalido")
            else:Minuscula(Lista,Linea+1,(Linea+2),Linea+1)   
        except:
            print("Valor Invalido")                 
    else: print("Valor Invalido")
def Minuscula(Lista,A,B,Counter):
    
    for x in (Lista[A:B]):                   
        Lista[Counter]=Lista[Counter].lower()
        Counter+=1
    MC.Actualiza(Lista)
    Lista=MC.LeeArchivo()
    ImprimeTexto(Lista)


