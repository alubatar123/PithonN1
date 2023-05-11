import os 
import random

Figura=["o=============o","||      ","||     ","||  ",
        "||    ","||  ","||____________","|_____________|"]

Figura1=["o=============o","||      |","||     _WW_ ","||    (°︿°)",
        "||     |︿| ","||     |︿|\_ ","||   _/|︿|\_ ","||     ⅃  L","||     ⅃  L"]

FiguraPerdio=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|_____________|"]

FiguraGano=["|￣￣￣￣￣￣| ","|  Ganaste!  |","|____________|","(\__/) ||","(•ㅅ•) || ",
            "/   づ"]


Aciertos=8
LetrasFallidas=["Letras Fallidas: "]
Error=""

def MuestraLetras(NewLetter,Word):    
        #global Gano
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
                #while True:
                        
                        Gano=FiguraInicial(Letras,Word)
                        
                                              
                        if Gano:
                                ImprimeGano(Word)
                                
                                                          
                        else:
                                NewLetter=(input("\nDigite una letra: ")) 
                                                        
                                if RevisaLetra(NewLetter,Letras):
                                        #MuestraLetras(Letras,Word)
                                        print("\n\n\n\n",Error,"Trate de nuevo")
                                        print(f"Le quedan {Aciertos} intentos!")
                                        Adivina(Word)
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
                                                #break                               
                                        else:
                                                print("\n\n\n\n"
                                                f"Correcto. Posee {Aciertos} intentos más!")
                                                
                                                Adivina(Word)
                                                
                      
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
        
def FiguraInicial(Letras,Word):
        ImprimeFigura()
        Gane=MuestraLetras(Letras,Word)
        for x in LetrasFallidas:
                print (x,end=" ")
        #NewLetter=(input("\nDigite una letra: "))
        return Gane        

def ImprimeFigura():
        for x in Figura:
                print(x)

def ImprimeGano(Word):
        print("\n\n\n\n")
        for x in FiguraGano:
            print(x)
        print("Felicidades!! La palabra era:",Word.upper())       

def ImprimePerdio(Word):
        print("\n\n\n\n")
        for x in FiguraPerdio:
                print(x)
        print("\nMaximo intentos fallidos,lo sentimos. La palabra era:",Word.upper())

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
      


#RandomWord()
Adivina("sucio")





