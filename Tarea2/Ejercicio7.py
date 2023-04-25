"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
7.	Programa que muestre el registro de los días de la semana, 
iniciando por Lunes y luego que los muestre nuevamente iniciando por domingo
y que a su vez señale los días laborales y los que no
"""
from collections import OrderedDict
from MiModulo import Continuar as Cont


def VerificaLibres():
    Semana={"|  Lunes    |":"1","|  Martes   |":"2","| Miercoles |":"3","|  Jueves   |":"4",
        "|  Viernes  |":"5","|  Sabado   |":"6","|  Domingo  |":"7"}
    dia=1
    while dia<3:
        for keys in Semana.keys(): #print only keys
            if Semana[keys]!="|  Libre**  |":
                print(keys.replace('|',''),"(",Semana[keys],")")
        
        Seleccion=input(f"Escoja su {dia}° libre: ")
        for key, value in Semana.items():
             if value ==Seleccion:
                Semana[key]="|  Libre**  |"
                dia+=1

    for key, value in Semana.items():
        if value != "|  Libre**  |":
            Semana[key]="|  Trabaja  |"
    ImprimeCalendario(Semana)
   
def ImprimeCalendario(Semana):
    
    o=0
    while o<2:
        print("Calendario ",o+1)
        for keys in Semana.keys(): #print only keys
            print(keys,end="")    
        print()
        for keys in Semana.values(): #print only keys
            print(keys,end="") 
        print()    
        o+=1
        if o==1:
            MiNuevoDic = OrderedDict(Semana)
            MiNuevoDic.move_to_end("|  Domingo  |",False)
            Semana=MiNuevoDic

            

 

VerificaLibres()
while Cont():
    VerificaLibres()