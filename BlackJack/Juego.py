from Mazo import Baraja
import random 

MiMazo= Baraja()
BarajaCompleta=MiMazo.CreaMazo()
UserMazoTemp=[]
CrupMazoTemp=[]
Seguir=1



def BarajaCartas():    
    random.shuffle(BarajaCompleta)
    
def Cartas4User(count):
    print("Mano Usuario") 
    try:   
        for e in range(count):
            UserMazoTemp.append(BarajaCompleta.pop(0))    
        MiMazo.CartaAspecto(*UserMazoTemp)
        print("===================================================\n")
        if count>0:
            HuboGane()    
    except:
         IndexError
         print("Fin del mazo")

     

def Cartas4Crupier(count):
    print("===================================================\nMano Crupier")
    try:
        for e in range(count):
            CrupMazoTemp.append(BarajaCompleta.pop(0))    
        MiMazo.CartaAspecto(*CrupMazoTemp) 
        
    except:
        IndexError
        print("Fin del mazo")
        
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
        return "Cont"        
       
def GaneCrupier():
    
    CrupierCounter=Verifica(CrupMazoTemp)
    
    if CrupierCounter==21:        
        return "Gano" ,CrupierCounter
        
    elif CrupierCounter>21:        
        print("perdio")
        return "Perdio",CrupierCounter
    elif CrupierCounter<21:
        return "Cont",CrupierCounter
                
        

def HuboGane():
    global Seguir
    GC,CrupierCounter=GaneCrupier()
    GU=GaneUsuario()
    print(GC)
    print(GU)
    if GC=="Gano" and GU=="Gano":
        print("Empate\n")
    elif GC=="Perdio" and GU=="Perdio":
        print("Ambos pierden\n")         
    elif GC=="Gano" and (GU=="Cont" or GU=="Perdio"):
        print("La casa gana\n") 
    elif GC=="Cont" and GU=="Perdio":
        print("Lo sentimos, perdió")        
    elif (GC=="Cont" or GC=="Perdio") and GU=="Gano":
        print("Felicidades Ganó\n")
    elif GC=="Perdio" and GU=="Cont":
        print("La casa perdió\n")                      
    elif GC=="Cont" and GU=="Cont":
        if Seguir == 1:
            Select=input("¿Desea otra carta?Y/N ")
            if Select == "y" or Select == "Y":
                Seguir=2    
                Cartas4Crupier(0)         
                Cartas4User(1)                 
        elif Seguir == 2:
            if CrupierCounter<17:
                Seguir=1
                Cartas4Crupier(1)
                HuboGane()
            else:
                Seguir=1
                Cartas4Crupier(1)
                Cartas4User(0)
                HuboGane()

#A A 4 Q = 11 1 4 =16 26 = 16
#4 Q = 14 + A = 15
#print(BarajaCompleta)
BarajaCartas()
Cartas4Crupier(2)
Cartas4User(2)
#print(BarajaCompleta)
#Verifica()