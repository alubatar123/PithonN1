from Mazo import Baraja
import random 

MiMazo= Baraja()
BarajaCompleta=MiMazo.CreaMazo()
UserMazoTemp=[]
CrupMazoTemp=[]
Seguir=1
NomUsuario=""



def BarajaCartas():    
    random.shuffle(BarajaCompleta)
    
def Cartas4User(count):
   
    try:   
        for e in range(count):
            UserMazoTemp.append(BarajaCompleta.pop(0))       
        ImprimeMazo()
    
        if count>0:
            HuboGane()    
    except:
        IndexError
        print("Fin del mazo")

     

def Cartas4Crupier(count):
    
    try:
        for e in range(count):
            CrupMazoTemp.append(BarajaCompleta.pop(0))  
        
       
    except:
        IndexError
        print("Fin del mazo")

def ImprimeMazo():
    print("===================================================\nMano Crupier")
    MiMazo.CartaAspecto(*CrupMazoTemp) 
    print(f"Mano de {NomUsuario}") 
    MiMazo.CartaAspecto(*UserMazoTemp)
    print("===================================================\n")



def Verifica(TipoMano):
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


def GaneUsuario(): 
    
    UserCounter=Verifica(UserMazoTemp)    
    if UserCounter==21:
        return "Gano"
              
    elif UserCounter>21:        
        return "Perdio"
         
    else:
        return "Cont",UserCounter        
       
def GaneCrupier():
    
    CrupierCounter=Verifica(CrupMazoTemp)
    
    if CrupierCounter==21:        
        return "Gano" ,CrupierCounter
        
    elif CrupierCounter>21:        
        
        return "Perdio",CrupierCounter
    elif CrupierCounter<21:
        return "Cont",CrupierCounter
                
        

def HuboGane():
    
    GC,CrupierCounter=GaneCrupier()
    GU,UserCounter=GaneUsuario()

    if GC=="Gano" and GU=="Gano":
        print("Empate\n")
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida()
    elif GC=="Perdio" and GU=="Perdio":
        print("Ambos pierden\n")
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida()         
    elif GC=="Gano" and (GU=="Cont" or GU=="Perdio"):
        print("La casa gana\n")
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida() 
    elif GC=="Cont" and GU=="Perdio":
        print("Lo sentimos, perdió")
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida()        
    elif (GC=="Cont" or GC=="Perdio") and GU=="Gano":
        print("Felicidades Ganó\n")
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida()
    elif GC=="Perdio" and GU=="Cont":
        print("La casa perdió\n") 
        print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        OtraPartida()                     
    elif GC=="Cont" and GU=="Cont":
        Repartirmas(CrupierCounter,UserCounter)


def Repartirmas(CrupierCounter,UserCounter):   
    global Seguir 
    if Seguir == 1:
        Select=input("¿Desea otra carta?Y/N ")
        if Select.upper() == "Y":
            Seguir=2                            
            Cartas4User(1)
        if Select.upper() == "N":
            Seguir=3
            HuboGane()
    elif Seguir == 2:
        if CrupierCounter<17:
            Seguir=1
            Cartas4Crupier(1)
            HuboGane()
        else:
            Seguir=1                               
            HuboGane()
    elif Seguir == 3:
        if CrupierCounter<17:
            Seguir=3
            Cartas4Crupier(1)
            HuboGane()
        else:
            Seguir=4                            
            HuboGane()    
    elif Seguir == 3:
        if CrupierCounter>UserCounter:
            print("La casa gana")
            print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")
        elif CrupierCounter>UserCounter:
            print("Felicidades Gano")    
            print(f"Casa total={CrupierCounter}\n{NomUsuario} total={UserCounter}")           
        else:
            print("Empate") 
    OtraPartida()
#A A 4 Q = 11 1 4 =16 26 = 16
#4 Q = 14 + A = 15
#print(BarajaCompleta)

def Comienza(Usuario):    
    global NomUsuario
    NomUsuario=Usuario
    BarajaCartas()

    Cartas4Crupier(2)
    Cartas4User(2)
    
def OtraPartida():
    global UserMazoTemp,CrupMazoTemp
    Select=input("¿Otra partida? Y/N")
    if Select.upper()=="Y":
        UserMazoTemp=[]
        CrupMazoTemp=[]
        Comienza(NomUsuario)
    elif Select.upper()=="N":

        Comienza(NomUsuario)
    else:
        print("Opcion Invaida")
        OtraPartida()    
#print(BarajaCompleta)
#Verifica()
