from Mazo import Baraja
import random 
import time
from Usuarios import Usuario

MiMazo= Baraja()
BarajaCompleta=[]
UserMazoTemp=[]
CrupMazoTemp=[]
Seguir=1
ListUser=[]

#funcion que crea una baraja nueva
def NuevaBaraja():
    global BarajaCompleta    
    BarajaCompleta=MiMazo.CreaMazo()

#funcion que baraja las cartas
def BarajaCartas():    
    random.shuffle(BarajaCompleta)
    
#funcion que da cartas al usuario    
def Cartas4User(count):    
    try:   
        for e in range(count):
            UserMazoTemp.append(BarajaCompleta.pop(0))       
        ImprimeMazo()
    
        if count>0:
            HuboGane()    
    except:
        IndexError
        print("Fin del mazo, no hay mas cartas para repartir. Inicie de nuevo")
        Reiniciar()

     
#funcion que da cartas al crupier   
def Cartas4Crupier(count):    
    try:
        for e in range(count):
            CrupMazoTemp.append(BarajaCompleta.pop(0))
    except:
        IndexError
        print("Fin del mazo, no hay mas cartas para repartir. Inicie de nuevo")
        Reiniciar()

#funcion que imprime los mazos de ambos jugadores
def ImprimeMazo():
    print("Repartiendo\n"),time.sleep(2)
    print("===================================================\nMano Crupier")    
    MiMazo.CartaAspectoCrupier(*CrupMazoTemp)
    print(f"Mano de {ListUser[1]}") 
    MiMazo.CartaAspecto(*UserMazoTemp) 
    
    print("===================================================\n")

#funcion que revela la mano del crupier
def RevelaMano():
    print("Se detectó un Gane, Derrota o Empate\nRevelando mano del crupier\n"),time.sleep(2)
    print("===================================================\nMano Crupier") 
    MiMazo.CartaAspecto(*CrupMazoTemp) 
    print(f"Mano de {ListUser[1]}") 
    MiMazo.CartaAspecto(*UserMazoTemp) 
    
    print("===================================================\n")

#funcion que da valores a cada carta
def DaValor(TipoMano):
    GaneCounter=0
      
    for e in TipoMano:        
        Valor=(e.translate({ord(i): None for i in ' ♥| ♦| ♠| ♣'})) 
        if Valor in "JQK":
            GaneCounter+=10            
        elif Valor.isdigit():            
            GaneCounter+=int(Valor)  
    for m in TipoMano:                
        Valor=(m.translate({ord(i): None for i in ' ♥| ♦| ♠| ♣'}))                
        if Valor in "A" and GaneCounter+11<22:
            GaneCounter+=11
        elif Valor in "A" and GaneCounter+11>21:            
            GaneCounter+=1
    
    return GaneCounter          

#funcion que verifica si el usuario gano
def GaneUsuario():     
    UserCounter=DaValor(UserMazoTemp)    
    if UserCounter==21:
        return "Gano",UserCounter                
    elif UserCounter>21:        
        return "Perdio",UserCounter         
    else:
        return "Cont",UserCounter        

#funcion que verifica si el crupier gano       
def GaneCrupier():
    
    CrupierCounter=DaValor(CrupMazoTemp)    
    if CrupierCounter==21:        
        return "Gano" ,CrupierCounter        
    elif CrupierCounter>21: 
        return "Perdio",CrupierCounter
    elif CrupierCounter<21:
        return "Cont",CrupierCounter
                
        
#funcion que compara ambas manos y determina Gane
def HuboGane():
    
    GC,CrupierCounter=GaneCrupier()
    GU,UserCounter=GaneUsuario()

    if GC=="Gano" and GU=="Gano":
        RevelaMano()
        print("Empate\n")
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        ActualizaTablas(ListUser[0],ListUser[1],0,0,1)
        OtraPartida()
    elif GC=="Perdio" and GU=="Perdio":
        RevelaMano()
        print("Ambos pierden\n")
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        
        OtraPartida()         
    elif GC=="Gano" and (GU=="Cont" or GU=="Perdio"):
        RevelaMano()
        print("La casa gana\n")
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        ActualizaTablas(ListUser[0],ListUser[1],0,1,0)
        OtraPartida() 
    elif GC=="Cont" and GU=="Perdio":
        RevelaMano()
        print("Lo sentimos, perdió")
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        ActualizaTablas(ListUser[0],ListUser[1],0,1,0)
        OtraPartida()        
    elif (GC=="Cont" or GC=="Perdio") and GU=="Gano":
        RevelaMano()
        print("Felicidades Ganó\n")
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        ActualizaTablas(ListUser[0],ListUser[1],1,0,0)
        OtraPartida()
    elif GC=="Perdio" and GU=="Cont":
        RevelaMano()
        print("La casa perdió, Usted Ganó\n") 
        print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
        ActualizaTablas(ListUser[0],ListUser[1],1,0,0)
        OtraPartida()                     
    elif GC=="Cont" and GU=="Cont":
        Repartirmas(CrupierCounter,UserCounter)

#Si aun no hay gane, se reparte mas cartas
def Repartirmas(CrupierCounter,UserCounter):   
    global Seguir 
    try:
        if Seguir == 1:
            Select=input("¿Desea otra carta? Y/N ")
            if Select.upper() == "Y":
                Seguir=2                            
                Cartas4User(1)
            if Select.upper() == "N":
                Seguir=3
                HuboGane()
        #el crupier solo puede pedir cartas si no ha pasado ya 17 pts 
        # Seguir = 2 significa que el usuario pidio otra carta, sigue el crupier       
        elif Seguir == 2:
            if CrupierCounter<17:
                Seguir=1
                Cartas4Crupier(1)
                ImprimeMazo()
                HuboGane()
            else:
                Seguir=1                               
                HuboGane()
        # Seguir = 3 significa que el usuario  no pidio otra carta, sigue el crupier            
        elif Seguir == 3:
            if CrupierCounter<17:
                Seguir=3
                Cartas4Crupier(1)
                ImprimeMazo()
                HuboGane()
            else:
                Seguir=4                            
                HuboGane()  
        #Si seguir es 4 significa que ningun jugador desea ya mas cartas          
        elif Seguir == 4:
            if CrupierCounter>UserCounter:
                RevelaMano()
                print("La casa gana\n")
                print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
                ActualizaTablas(ListUser[0],ListUser[1],0,1,0)
            elif CrupierCounter<UserCounter:
                RevelaMano()
                print("Felicidades Gano\n")    
                print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
                ActualizaTablas(ListUser[0],ListUser[1],1,0,0)           
            else:
                RevelaMano()
                print("Empate") 
                print(f"Casa total={CrupierCounter}\n{ListUser[1]} total={UserCounter}")
                ActualizaTablas(ListUser[0],ListUser[1],0,0,1)
            OtraPartida()   
    except: 
        print("Opcion incorrecta.")
        Repartirmas(CrupierCounter,UserCounter)

 #se actualiza la BD con el resultado   
def ActualizaTablas(USER,Nombre,GANES,DERROTAS,EMPATES):
    OB=Usuario()   
    List=(OB.StatUser(ListUser[0]))
    OB.ActualizaDic(USER,Nombre,
                    GANES+int(List[1]),
                    DERROTAS+int(List[2]),
                    EMPATES+int(List[3]))
    

#funcion que comienza el Modulo Jugar
def Comienza(Usuario):    
    global ListUser
    ListUser=Usuario
    Reiniciar()
    BarajaCartas()
    Cartas4Crupier(2)
    Cartas4User(2)

#se pregunta si se desea jugar de nuevo    
def OtraPartida():
    global UserMazoTemp,CrupMazoTemp
    try:
        Select=input("\n¿Otra partida? Y/N ")
        if Select.upper()=="Y":
            print("Nueva mano")
            Reiniciar()
            Comienza(ListUser)
        elif Select.upper()=="N":
            print("\nGracias por jugar\n")
            Reiniciar()
            print("\n===========================================\nRegresando al menu principal..."),time.sleep(2)        
        else:
            print("Opcion Invaida")
    except:
        print("Opcion incorrecta.")
        OtraPartida()

#Se reinician contadores antes del juego
def Reiniciar():
        global Seguir,UserMazoTemp,CrupMazoTemp
        UserMazoTemp.clear()
        CrupMazoTemp.clear()
        Seguir = 1 
