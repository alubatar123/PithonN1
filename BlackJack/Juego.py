from Mazo import Baraja
import random 

MiMazo= Baraja()
BarajaCompleta=MiMazo.CreaMazo()
MazoTemp=[]




def BarajaCartas():    
    random.shuffle(BarajaCompleta)
    
def TiraCartas():
    MazoTemp.append(BarajaCompleta.pop(0))    
    MiMazo.CartaAspecto(*MazoTemp)
    Select=input("¿Desea otra carta?Y/N ")
    if Select == "y" or Select == "Y":
        TiraCartas()



BarajaCartas()
print(BarajaCompleta)
TiraCartas()
print(BarajaCompleta)