#Se importa modulo ModuloConexion para actualizar el archivo de texto
#Se importa time para mostrar pausas al correr cada funcion
import ModuloConexion as MC
import time


#Funcion que Imprime el texto actual
def ImprimeTexto(Lista):
    print("======================================TEXTO ACTUAL========================================")
    print(Lista[0])    
    for x in (Lista[2:(len(Lista)+1)]):                   
        print(x,end="") 
    print("\n=======================================FIN DE TEXTO========================================")

#Funcion que actualiza el texto actual
def PedirActual(Lista):
    print("\nEfectuando cambios. Favor espere") 
    print("2seg"),time.sleep(1),print("1seg"),time.sleep(1)    
    MC.Actualiza(Lista)
    Lista=MC.LeeArchivo()             
    ImprimeTexto(Lista)
    
#funcion que aplica centra y aplica formato titulo
def CentrarTitulo():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    Lista[0]=Lista[0].strip()   
    
    Lista[0]=Lista[0].title().center((len(Lista[0]))+49)+"\n"  
    PedirActual(Lista) 

  
#funcion que permite alinear a la izquierda
def AlineaIzq():
    Lista=MC.LeeArchivo()  
    Counter=1
    #se muestra las posibles lineas a alinear
    print("\n=====================================LINEAS DISPONIBLES==================================== ")
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    print("\n===========================================================================================")
    try:    
        Linea=int(input("\n\nNOTA: Se usará el simbolo '<' para indicar el alineamiento izquiero\n¿Cúal linea desea alinear a la izquierda? "))
        #se pregunta por el parrafo a alinear
        if "<" in Lista[Linea+1]:
            print(f"Linea {Linea} ya fue alineada a la izquierada")
        elif Linea==0:print("Valor Invalido")
        else:
            Lista[Linea+1]=Lista[Linea+1].strip().replace(">","")
            Lista[Linea+1]=Lista[Linea+1].ljust(7+len(Lista[Linea+1]),"<")+"\n"  
            PedirActual(Lista)      
  
    except:
        print("Valor Invalido")

#funcion que permite alinear a la izquierda
def AlineaDer():
    Lista=MC.LeeArchivo()  
    Counter=1
    #se muestra las posibles lineas a alinear
    print("\n=====================================LINEAS DISPONIBLES====================================")
    for x in (Lista[2:(len(Lista)+1)]):                   
        print(f"Párrafo[{Counter}]\n",x,end="")
        Counter+=1 
    print("\n============================================================================================")
    try:    
        Linea=int(input("\n\nNOTA: Se usará el simbolo '>' para indicar el alineamiento derecho\n¿Cúal linea desea alinear a la derecha? "))
        #se pregunta por el parrafo a alinear
        if ">" in Lista[Linea+1]:
            print(f"Linea {Linea} ya fue alineada a la derecha")
        elif Linea==0:print("Valor Invalido")     
        else:
            Lista[Linea+1]=Lista[Linea+1].strip().replace("<","")
            Lista[Linea+1]=Lista[Linea+1].rjust(7+len(Lista[Linea+1]),">")+"\n" 
            PedirActual(Lista)       

    except:
        print("Valor Invalido")

#funcion que pregunta que se desea cambiar a mayusculas
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
            print(f"* Párrafo [{Counter}]\n",x,end="")
            Counter+=1 
        try:    
            Linea=int(input("\n\n¿Cúal párrafo desea pasar a Mayúscula? "))
            if Linea+2>len(Lista):
                print("Valor Invalido")
            else:Mayuscula(Lista,Linea+1,(Linea+2),Linea+1)               
        except:
            print("Valor Invalido")                 
    else: print("Valor Invalido")

#funcion que pasa a mayusculas lo indicado en la funcion anterior
def Mayuscula(Lista,A,B,Counter):
    
    for x in (Lista[A:B]):                   
        Lista[Counter]=Lista[Counter].upper()
        Counter+=1
    PedirActual(Lista) 

#funcion que pregunta que se desea cambiar a minusculas
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
            print("* Párrafo [",Counter,"]\n",x,end="")
            Counter+=1 
        try:    
            Linea=int(input("\n\n¿Cúal párrafo desea pasar a Minúsculas? "))
            if Linea+2>len(Lista):
                print("Valor Invalido")
            else:Minuscula(Lista,Linea+1,(Linea+2),Linea+1)   
        except:
            print("Valor Invalido")                 
    else: print("Valor Invalido")

#funcion que pasa a minusculas lo indicado en la funcion anterior
def Minuscula(Lista,A,B,Counter):
    
    for x in (Lista[A:B]):                   
        Lista[Counter]=Lista[Counter].lower()
        Counter+=1
    PedirActual(Lista)


#funcion que permite buscar letras o palabras
def Buscar(accion="encontrar"):
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    print(" ")    
    Select=input(f"¿Cúal palabra/cadena de letras desea {accion}? ")
    Count=1
    Acierto=0
    AciertoLista=[]
    #se pasa a minusculas la seleccion para prevenir errores
    if Select.lower() in Lista[0].lower():        
        print('La palabra "',Select,'" se encuentra en el titulo del texto')
        AciertoLista.append(0)
        Acierto=1
    #se indica en que linea se encuentra
    for x in Lista[2:(len(Lista)+1)]:
        if Select.lower() in x.lower():            
            print('La palabra "',Select,'" es parte del párrafo',Count)
            AciertoLista.append(Count+1)
            Acierto=1
        Count+=1
    
    if Acierto == 0: print('La palabra "',Select,'" no se encontra en el texto')
    return Select,Acierto,AciertoLista

#funcion que permite cortar y pegar texto.
def Mover():
    Lista=MC.LeeArchivo() 
    ImprimeTexto(Lista)
    Counter=1
    #se muestra parrafos disponibles a mover
    print("\n=====================================LINEAS DISPONIBLES==================================== ")
    for x in (Lista[2:(len(Lista)+1)]):                   
        print("Linea[",Counter,"]",x,end="")
        Counter+=1 
    print("\n===========================================================================================")
    #se cambia la posicion del texto segun lo escogido
    try:
        Select=int(input("\n¿Cúal linea desea cortar?\nSelección: "))
        if Select>0 and Select< len(Lista)-1:
            Select2=int(input("\n¿Cúal linea desea pegarla?\nSelección: "))
            if Select2>0 and Select2< len(Lista)-1:
                Lista.insert(Select2+1,Lista.pop(Select+1))
                PedirActual(Lista) 
            else:print("Valor invalido")     
        else:print("Valor invalido")         
    except:
        print("Valor invalido")    

#funcion que permite borrar letras o palabras
def Borrar():
    #se recicla la funcion Buscar para este fin
    Palabra,Acierto,AciertoLista=Buscar("borrar")  
    Lista=MC.LeeArchivo()  
    if Acierto == 1:
        print("\nQue acción desea efectuar: \n\n [1]Borrar todas las instancias\n [2]Borrar instancia de linea en particular\n")
        Select=input("Selección: ")
        if Select == "1":
        #de escoger 1, se borran todas las instancias encontradas en el texto  
            count=0
            for x in Lista:
                Lista[count]=Lista[count].lower().replace(Palabra.lower(),"")
                count+=1
            PedirActual(Lista)    
        elif Select == "2":
        #se ofrece borrar solamente resultado de un parrafo    
            print(f"¿De cúal linea desea borrar'{Palabra}' ?")
            for x in AciertoLista:
                if x == 0:print("(0) - Del Título")
                else: print(f"({x-1}) - Párrafo[{x-1}]")
            try:
                Select=int(input("\nSelección: "))
            #depende de la seleccion se borra la palabra del titulo o de un parrafo                
                if Select==0:
                    Lista[0]=Lista[0].lower().replace(Palabra.lower(),"")
                    PedirActual(Lista)

                elif Select+1 in AciertoLista:                
                    Lista[Select+1]=Lista[Select+1].lower().replace(Palabra.lower(),"")
                    PedirActual(Lista)
                else: print("Opcion invalida")  
                
            except:
                print("Opcion Invalida")    
        else: print("Opcion invalida")       
         
