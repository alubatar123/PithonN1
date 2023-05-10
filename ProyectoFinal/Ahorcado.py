import os 
import random



Figura=["o=============o","||      |","||     _WW_ ","||    (°︿°)",
        "||   _/|︿|\_ ","||     ⅃  L","||____________","|             |"]

Figura2=["o=============o","||      |","||     _WW_ ","||    (ˣ_̲ ˣ)","||   ‾\|︿|/‾ ",
        "||     ⅃  L","||____________","|             |"]

Word="prueba"
Aciertos=1
ListaCompara=[]
def FuncionNormal2(e):
    global ListaCompara
    print(Word)
    ListaCompara=[]

    for x in Word:
        if x in e:
              print (x,end=" ")
              ListaCompara.append(x)
        else:
              print ("_",end=" ")

    Adivina(e)



# def RandomWord():
#     Palabras=[]
#     Archivo=open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/ProyectoFinal/Palabras.txt','r')
#     x=(Archivo.readlines())
#     for line in x:
#         Palabras.append(line.strip())    
#     FuncionNormal2(Palabras[random.randrange(0, 77)])

def Adivina(Letras=[],Gano=True):
        global Aciertos, ListaCompara
        if ListaCompara != Letras:
             Aciertos+=1
             print(ListaCompara)
             print(Letras)
        if Aciertos < 8:
             print(Aciertos)
             Letras.append(input("Letra"))
             FuncionNormal2(Letras)
        
       

     #FuncionNormal2("prueba",Letras)


Adivina([])





#RandomWord()


# for x in Figura:
#     print(x)
# for x in Figura2:
    
#     print(x)