"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
Proyecto Final. Ahorcado

Confeccionar el juego del horcado el cual debe de cumplir con lo siguiente:
a.	Ocho Intentos máximo o vida antes de finalizar el juego. Valor 5 pts.
b.	Las palabras que se va adivinar tiene que ser tomadas al azar, ya sea de una lista
        o de un archivo de texto y tiene que mostrar una referencia de la cantidad de letras
        que las compone. Valor 15 pts.
c.	Indicar las letras acertadas de la palabra por adivinar como guía. Valor 6 pts.
d.	En caso de no acertar la letra, indicar letra no acertada y los intentos restantes. Valor 8 pts.
e.	Al finalizar si no acertó las letras que conforma la palabra por adivinar,
        como resumen indicar los aciertos, las fallas y la palabra que era. Valor 6 pts.

"""

import os 
import random
#importar Libreria OS para manejo de archivos y Random para crear numeros al azar

#posibles figuras del juego
Figura=["o=============o","||      ","||     ","||  ",
        "||    ","||  ","||____________","|_____________|"]

Figura1=["o=============o","||      |","||     _WW_ ","||    (°︿°)",
        "||     |︿| ","||     |︿|\_ ","||   _/|︿|\_ ","||     ⅃  L","||     ⅃  L"]

FiguraPerdio=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|_____________|"]

FiguraGano=["|￣￣￣￣￣￣| ","|  Ganaste!  |","|____________|","(\__/) ||","(•ㅅ•) || ",
            "/   づ"]

#contador de numero de aciertos y letras fallidas
Aciertos=8
LetrasFallidas=["Letras Fallidas: "]
Error=""

#Funcion que confirma si gano. Y esconde o muestra las letras acertadas  
def MuestraLetras(NewLetter,Word):  
        ListaGano=[]
        Gano=False
        for x in Word:
                if x in NewLetter:
                     print (x,end=" ")              
                else:
                        print ("_",end=" ")
                        ListaGano.append(x) 
        print("")           
        if len(ListaGano)== 0:                
                Gano=True
        
        return Gano      
#funcion que permite escojer una palabra de la lista
def RandomWord():
        Palabras=[]
        Archivo=open('C:/PithonN1/ProyectoFinal/Palabras.txt','r')
        x=(Archivo.readlines())
        for line in x:
                Palabras.append(line.strip())  
        #se pasa la palabra a la funcion principal del juego               
        Adivina(Palabras[random.randrange(0, len(Palabras))])

#funcion principal que pregunta por letras y llama otras para la validacion
def Adivina(Word,Letras=[]):
        global Aciertos,LetrasFallidas,Gano 
        if Aciertos > 0:
                Gano=FiguraDefecto(Letras,Word)                
                #si Gano es True el juego termina                       
                if Gano:
                        ImprimeGano(Word)               
                else:
                        NewLetter=(input("\nDigite una letra: ")) 
                        #Si el resultado de RevisaLetra() es True, quiere decir que se
                        # ingreso un caracter invalido                                                
                        if RevisaLetra(NewLetter,Letras):                                        
                                print("\n\n\n\n",Error,"Trate de nuevo")
                                print(f"Le quedan {Aciertos} intentos!")
                                Adivina(Word)
                        #De lo contrario si valida si se adivino la letra o no        
                        else:
                                Letras.append(NewLetter.lower())
                                if NewLetter.lower() not in Word:
                                        LetrasFallidas.append(NewLetter) 
                                        #si se falla se resta un intento                               
                                        Aciertos-=1
                                        if Aciertos> 0:
                                                print("\n\n\n\n"
                                                f"Incorecto.Le quedan {Aciertos} intentos!")
                                        #se actualiza la figura con cada fallo        
                                        CambiaFigura(-Aciertos)        
                                        Adivina(Word)           
                                else:
                                        #Si acierta se le indica al jugador
                                        print("\n\n\n\n"
                                        f"Correcto. Posee {Aciertos} intentos más!")                                        
                                        Adivina(Word)
        else:
                #si perdio se llama a la funcion correspondiente para terminar
                ImprimePerdio(Word)
 
#funcion que permite actualizar la figura              
def CambiaFigura(index):
        global Figura       
        if index == -7:Figura[index]=Figura1[1]
        if index == -6:Figura[index]=Figura1[2]
        if index == -5:Figura[index]=Figura1[3]
        if index == -4:Figura[index]=Figura1[4]
        if index == -3:Figura[-4]=Figura1[5]
        if index == -2:Figura[-4]=Figura1[6]
        if index == -1:Figura[-3]=Figura1[7]
        if index ==  0:Figura[-3]=Figura1[8]

#funcion que muestra una figura por defecto       
def FiguraDefecto(Letras,Word):
        ImprimeFigura()
        Gane=MuestraLetras(Letras,Word)
        for x in LetrasFallidas:
                print (x,end=" ")
        return Gane        
#funcion que imprime la figura actual
def ImprimeFigura():
        for x in Figura:
                print(x)

#funcion que imprime el Gane
def ImprimeGano(Word):
        print("\n\n\n\n")
        for x in FiguraGano:
            print(x)
        print("\nFelicidades!! La palabra era:",Word.upper(),"\n")       
#funcion que imprime Perdida
def ImprimePerdio(Word):
        print("\n\n\n\n")
        for x in FiguraPerdio:
                print(x)
        print("\nMaximo intentos fallidos,lo sentimos. La palabra era:",Word.upper())

#Funcion que confirma que las letras sean validas
def RevisaLetra(NuevaLetra,Lista):
        global Error
        if len(NuevaLetra) > 1:
                Error="Solo se permite una letra a la vez"
                return True
        elif NuevaLetra.isalpha() == False:
                Error="Caracter Invalido"
                return True          
        elif NuevaLetra.lower() in Lista:
                Error="'"+NuevaLetra.upper()+"'"+ " ya fue utilizada"
                return True    
        else:
                return False

#Se llama a la funcion que crear palabras random y empieze el juego
RandomWord()






