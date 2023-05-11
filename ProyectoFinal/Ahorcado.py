import os 
import random

Figura=["o=============o","||      ","||     ","||  ",
        "||    ","||  ","||____________","|_____________|"]

Figura1=["o=============o","||      |","||     _WW_ ","||    (°︿°)",
        "||     |︿| ","||     |︿|\_ ","||   _/|︿|\_ ","||     ⅃  ","||     ⅃  L"]

FiguraPerdio=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|_____________|"]

FiguraGano=["|￣￣￣￣￣￣| ","|  Ganaste!  |","|____________|","(\__/) ||","(•ㅅ•) || ",
            "/   づ"]


Aciertos=8
LetrasFallidas=["Letras Fallidas: "]
Gano=False

def MuestraLetras(NewLetter,Word):    
        global Gano
        ListaGano=[]
        Gano=False
        for x in Word:
                if x in NewLetter:
                     print (x,end=" ")              
                else:
                        print ("_",end=" ")
                        ListaGano.append(x) 
        print("")           
        if len(ListaGano)== 1:                
                Gano=True
             

def RandomWord():
        Palabras=[]
        Archivo=open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/ProyectoFinal/Palabras.txt','r')
        x=(Archivo.readlines())
        for line in x:
                Palabras.append(line.strip())         
        Adivina(Palabras[random.randrange(0, len(Palabras))])

def Adivina(Word,Letras=[]):
        global Aciertos,LetrasFallidas,Gano

        if Aciertos > 0:                
                while True:                        
                        if Gano:
                                ImprimeGano(Word)
                                break
                        ImprimeFigura()
                        MuestraLetras(Letras,Word)
                        for x in LetrasFallidas:
                                print (x,end=" ")
                        NewLetter=(input("\nDigite una letra: "))
                                
                        if RevisaLetra(NewLetter,Letras):
                                MuestraLetras(Letras,Word)
                                print("\n\n\n\nVAlOR INVALIDO, Trate de nuevo")
                                print(f"Le quedan {Aciertos} intentos!")
                        else:
                                Letras.append(NewLetter.lower())
                                if NewLetter.lower() not in Word:
                                        LetrasFallidas.append(NewLetter)                                
                                        Aciertos-=1
                                        if Aciertos> 0:
                                                print("\n\n\n\n"
                                                      f"Incorecto.Le quedan {Aciertos} intentos!")
                                        CambiaFigura(-Aciertos)        
                                        Adivina(Word)                                
                                        break
                               
                                else:
                                        print("\n\n\n\n"
                                              f"Correcto. Posee {Aciertos} intentos más!")
                                        
        else:
                ImprimePerdio(Word)

                
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
        

def ImprimeFigura():
        for x in Figura:
                print(x)

def ImprimeGano(Word):
        print("\n\n\n\n")
        for x in FiguraGano:
            print(x)
        print("Felicidades!! La palabra era ",Word)       

def ImprimePerdio(Word):
        print("\n\n\n\n")
        for x in FiguraPerdio:
                print(x)
        print("\nMaximo intentos fallidos,lo sentimos. La palabra era:",Word.upper())

def RevisaLetra(NuevaLetra,Lista):
        if len(NuevaLetra) > 1:
                return True
        elif NuevaLetra.isalpha() == False:
                return True          
        elif NuevaLetra in Lista:
                return True    
        else:
                return False
      


RandomWord()





