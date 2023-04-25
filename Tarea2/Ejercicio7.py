"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
7.	Programa que muestre el registro de los días de la semana, 
iniciando por Lunes y luego que los muestre nuevamente iniciando por domingo
y que a su vez señale los días laborales y los que no
"""
#importa la collection OrderedDict y MiModulo
from collections import OrderedDict as ReOrder
from MiModulo import Continuar as Cont


def VerificaLibres():
    """
    Funcion que verifica cuales dias el usuario tendra libre
    """
    Semana={"|  Lunes    |":"1","|  Martes   |":"2","| Miercoles |":"3","|  Jueves   |":"4",
        "|  Viernes  |":"5","|  Sabado   |":"6","|  Domingo  |":"7"}
    dia=1
    #Ciclo que nos permite escojer 2 dias libres
    while dia<3:
        #Pone en Menu los dias NoLibres para escojer
        for keys in Semana.keys(): 
            if Semana[keys]!="|  Libre**  |":
                print(keys.replace('|',''),"(",Semana[keys],")")
        
        Seleccion=input(f"Escoja su {dia}° libre: ")
        #Reemplaza el valor del diccionario por "Libre"
        for key, value in Semana.items():
             if value ==Seleccion:
                Semana[key]="|  Libre**  |"
                dia+=1
    #Una vez escogido 2 dias libres, los demas valores del dic cambiara a "Trabaja"
    for key, value in Semana.items():
        if value != "|  Libre**  |":
            Semana[key]="|  Trabaja  |"
    #Llama la funcion que imprime la semana
    ImprimeCalendario(Semana)
   
def ImprimeCalendario(Semana):
    """
    Funcion que imprime ambas versiones del calendario
    """
    o=0

    while o<2:
        print("Calendario ",o+1)
        #Imprime la version de L a D
        for keys in Semana.keys(): #print only keys
            print(keys,end="")    
        print()
        for keys in Semana.values(): #print only keys
            print(keys,end="") 
        print()    
        o+=1
        if o==1:
            #Imprime la version de D a S al pasar Domingo de primero
            MiNuevoDic = ReOrder(Semana)
            MiNuevoDic.move_to_end("|  Domingo  |",False) #El False la convierte a move_to_begin
            Semana=MiNuevoDic

            

 
#Funcion que empieza el programa
VerificaLibres()

#Llamamos a la Funcion Continuar del MiModulo para verificar si desea otra operacion
while Cont():
    VerificaLibres()