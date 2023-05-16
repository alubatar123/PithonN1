


import ModuloConexion as MC
import time



def ImprimeTexto(Lista):
    print("======================================TEXTO ACTUAL========================================")
    print(Lista[0])    
    for x in (Lista[2:(len(Lista)+1)]):                   
        print(x,end="") 
    print("\n=======================================FIN DE TEXTO========================================")

def Cargando():
    print("\nEfectuando cambios. Favor espere") 
    print("2seg"),time.sleep(1),print("1seg"),time.sleep(1)    

def CentrarTitulo():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    Cargando()     
    
    Lista[0]=Lista[0].strip().title().center((len(Lista[0]))+49)+"\n\n"    
    ImprimeTexto(Lista)
    MC.Actualiza(Lista)
  

def AlineaIzq():
    Lista=MC.LeeArchivo()  
    Counter=1
    print("\n=====================================LINEAS DISPONIBLES==================================== ")
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    print("\n===========================================================================================")
    try:    
        Linea=int(input("\n\nNOTA: Se usará el simbolo '<' para indicar el alineamiento izquiero\n¿Cúal linea desea alinear a la izquierda? "))
        if "<" in Lista[Linea+1]:
            print(f"Linea {Linea} ya fue alineada a la izquierada")
        else:
            Lista[Linea+1]=Lista[Linea+1].strip().replace(">","")
            Lista[Linea+1]=Lista[Linea+1].ljust(7+len(Lista[Linea+1]),"<")+"\n"        
            MC.Actualiza(Lista)
            Lista=MC.LeeArchivo() 
            Cargando()
            ImprimeTexto(Lista)
    except:
        print("Valor Invalido")

def AlineaDer():
    Lista=MC.LeeArchivo()  
    Counter=1
    print("\n=====================================LINEAS DISPONIBLES====================================")
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    print("\n============================================================================================")
    try:    
        Linea=int(input("\n\nNOTA: Se usará el simbolo '>' para indicar el alineamiento derecho\n¿Cúal linea desea alinear a la derecha? "))
        if ">" in Lista[Linea+1]:
            print(f"Linea {Linea} ya fue alineada a la derecha")
        else:
            Lista[Linea+1]=Lista[Linea+1].strip().replace("<","")
            Lista[Linea+1]=Lista[Linea+1].rjust(7+len(Lista[Linea+1]),">")+"\n"        
            MC.Actualiza(Lista)
            Lista=MC.LeeArchivo() 
            Cargando()
            ImprimeTexto(Lista)
    except:
        print("Valor Invalido")


def MayusculaMenu():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")
    print("  Opciones Para Mayúsculas\n\n[1] Todo el texto\n[2] Solo el título\n"
            "[3] Todos los párrafos\n[4] Solo un párrafo\n")
    Select=input("Seleccione una opción: ")
    
    if Select=="1":Mayuscula(Lista,0,(len(Lista)+1),0)
    elif Select=="2":Mayuscula(Lista,0,1,0)
    elif Select=="3":Mayuscula(Lista,2,(len(Lista)+1),2)
    elif Select=="4":
        Counter=1
        for x in (Lista[2:(len(Lista)+1)]):                   
            print("Linea[",Counter,"]\n",x,end="")
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
    Cargando()
    ImprimeTexto(Lista)

def MinusculaMenu():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")
    print("  Opciones Para Minúsculas\n\n[1] Todo el texto\n[2] Solo el título\n"
            "[3] Todos los párrafos\n[4] Solo un párrafo\n")
    Select=input("Seleccione una opción: ")
    
    if Select=="1":Minuscula(Lista,0,(len(Lista)+1),0)
    elif Select=="2":Minuscula(Lista,0,1,0)
    elif Select=="3":Minuscula(Lista,2,(len(Lista)+1),2)
    elif Select=="4":
        Counter=1
        for x in (Lista[2:(len(Lista)+1)]):                   
            print("Linea[",Counter,"]\n",x,end="")
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
    Cargando()
    ImprimeTexto(Lista)


def Buscar():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")    
    Select=input("¿Cúal palabra desea encontar? ")
    Count=1
    Acierto=0
    if Select.lower() in Lista[0].lower():        
        print('La palabra "',Select,'" se encuentra en el titulo del texto')
        Acierto=1
    for x in Lista[2:(len(Lista)+1)]:
        if Select.lower() in x.lower():            
            print('La palabra "',Select,'" es parte del párrafo',Count)
            Acierto=1
        Count+=1
    if Acierto == 0: print('La palabra "',Select,'" no se encontra en el texto')


def Buscar(accion="encontrar"):
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")    
    Select=input(f"¿Cúal palabra desea {accion}? ")
    Count=1
    Acierto=0
    if Select.lower() in Lista[0].lower():        
        print('La palabra "',Select,'" se encuentra en el titulo del texto')
        Acierto=1
    for x in Lista[2:(len(Lista)+1)]:
        if Select.lower() in x.lower():            
            print('La palabra "',Select,'" es parte del párrafo',Count)
            Acierto=1
        Count+=1
    
    if Acierto == 0: print('La palabra "',Select,'" no se encontra en el texto')
    return Select,Acierto





def Borrar():
    Palabra,Acierto=Buscar("borrar")
    print(Palabra,Acierto)
    # print("Que acción desea efectuar: 'n[1]Borrar todas las instancias\n[2]Borrar instancia de linea en particular")
    # Select=input("Selección: ")
    # if Select == "1":
    #     Lista=MC.LeeArchivo()
    #     count=0
    #     for x in Lista:
    #         Lista[count]=Lista[count].replace(Palabra,"")
    # elif        
    # MC.Actualiza(Lista)
    # Lista=MC.LeeArchivo()
    # Cargando()
    # ImprimeTexto(Lista)

