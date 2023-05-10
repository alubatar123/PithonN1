import os 
import random

Figura=["o=============o","||      ","||     ","||  ",
        "||    ","||  ","||____________","|             |"]

Figura1=["o=============o","||      |","||     _WW_ ","||    (°︿°)",
        "||     |︿| ","||     |︿|\_ ","||   _/|︿|\_ ","||     ⅃  ","||     ⅃  L"]

Figura2=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|             |"]

Figura3=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|             |"]

Word="prueba"
Aciertos=8

def FuncionNormal2(e):    
    print(Word)
    ListaGano=[]
    Gano=False
    for x in Word:
        if x in e:
              print (x,end=" ")
              
        else:
              print ("_",end=" ")
              ListaGano.append("_")
    if len(ListaGano)== 0:
         Gano=True
             
    Adivina(e,Gano)



# def RandomWord():
#     Palabras=[]
#     Archivo=open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/ProyectoFinal/Palabras.txt','r')
#     x=(Archivo.readlines())
#     for line in x:
#         Palabras.append(line.strip())    
#     FuncionNormal2(Palabras[random.randrange(0, 77)])

def Adivina(Letras=[],Gano=False):
    global Aciertos,Word
    print(Aciertos)
    if Gano == False:
          if Aciertos > 0:
                print(Aciertos)
                NewLetter=(input("Letra"))
                Letras.append(NewLetter)
                if NewLetter not in Word:
                        Aciertos-=1
                        print(f"Le quedan {Aciertos} intentos!\n")
                CambiaFigura(-Aciertos)        
                FuncionNormal2(Letras)
          else:
                print("Maximo intentos fallidos, lo sentimos")
                for x in Figura2:
                     print(x)
               
    else:
        print("Felicidades adivinó!!!!")                

                
def CambiaFigura(index):
     print("indice",index)
     if index == -7:Figura[index]=Figura1[1]
     if index == -6:Figura[index]=Figura1[2]
     if index == -5:Figura[index]=Figura1[3]
     if index == -4:Figura[index]=Figura1[4]
     if index == -3:Figura[-4]=Figura1[5]
     if index == -2:Figura[-4]=Figura1[6]
     if index == -1:Figura[-3]=Figura1[7]
     if index == 0:Figura[-3]=Figura1[8]
     for x in Figura:
        print(x)


       

     #FuncionNormal2("prueba",Letras)


Adivina()





#RandomWord()


