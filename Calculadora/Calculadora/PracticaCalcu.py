from tkinter import *
import Calculos as Cal

raiz=Tk()
raiz.title("Calculadora Chukito")
raiz.resizable(False,False)
raiz.geometry("350x389")
miFrame=Frame(raiz)
miFrame.pack()
path="Curso\InterfacesGrafica\Calculadora"########Cambiar con el path actual

raiz.iconbitmap(path+"\Dragonball-Goku.ico")
numeroPantalla0=StringVar()
numeroPantalla=StringVar()


#______ PANTALLA ______
pantalla0=Entry(miFrame,textvariable=numeroPantalla0,bd=-2)
pantalla0.grid(row=0,column=1,columnspan=4)
pantalla0.config(cursor="none",background="black",width="22",fg="#03f943",font=("Helvetica", 21), justify="right")

pantalla=Entry(miFrame,textvariable=numeroPantalla,bd=-2)
pantalla.grid(row=1,column=1,columnspan=4)
pantalla.config(cursor="none",background="black",width="16",fg="#03f943",font=("Helvetica", 29), justify="right")



#______Teclando______

def Operar(Oper):
    #Si hay ya valor en Pantalla0, se actualiza con el resultado de la operacion
    if numeroPantalla.get()=="" and numeroPantalla0.get()!="" and Cal.operacion=="":        
        numeroPantalla0.set(numeroPantalla0.get()+" "+Oper)  
        Cal.operacion=Oper
    #Permite cambiar la operacion si se indico la incorrecta    
    elif numeroPantalla.get()=="" and numeroPantalla0.get()!="" and Cal.operacion!=Oper:  
        numeroPantalla0.set(numeroPantalla0.get()[:-2])       
        numeroPantalla0.set(numeroPantalla0.get()+" "+Oper)  
        Cal.operacion=Oper
    #Si ya existe valor en pantalla principal se actualiza la pantalla0
    elif numeroPantalla.get()!="":        
        if Cal.operacion=="":                 
            Cal.operacion=Oper
            numeroPantalla0.set(str(Cal.Operate(float(numeroPantalla.get())))+" "+Oper)
            Cal.First=False
        else:            
            numeroPantalla0.set(str(Cal.Operate(float(numeroPantalla.get())))+" "+Oper)
            Cal.First=False
            Cal.operacion=Oper
        numeroPantalla.set("")
        
def FuncionIgual():  
    #No cambia nada si aun no se ha indicado que operacion realizar
    if numeroPantalla.get()!="" and numeroPantalla0.get()=="" and Cal.operacion=="": 
        pass  
    #No cambia nada si aun no se ha indicado que operacion realizar
    elif numeroPantalla.get()=="" and numeroPantalla0.get()!="" and Cal.operacion=="": 
        pass
    else:
        if numeroPantalla.get()!="":                        
            numeroPantalla0.set(str(Cal.Operate(float(numeroPantalla.get()))))
            numeroPantalla.set("")
            Cal.operacion=""
            

def BorrarTodo():
    numeroPantalla0.set("")
    numeroPantalla.set("")
    Cal.Limpiar()

def BorrarUltimoNUM():  
    #borra el ultimo numero completo  
    numeroPantalla.set("")

def BorrarUltimoDig(): 
    #borra el solo ultimo digito del ultimo numero
    numeroPantalla.set(numeroPantalla.get()[:-1])      

def numeroPulsado(num): 
    #Previene digitar mas de un "." or digitarlo antes de un numero
    if (num=="." and numeroPantalla.get()=="") or (num=="." and "." in numeroPantalla.get()):
        pass
    #Borrar valores anteriores si no se espefico una operacion
    elif Cal.operacion=="" and numeroPantalla0.get()!="":
        BorrarTodo() 
        numeroPantalla.set(numeroPantalla.get()+num)
    #Si no hay valor anterior, se actualiza  
    elif Cal.operacion=="" and numeroPantalla0.get()=="":
        numeroPantalla.set(numeroPantalla.get()+num)  
    #Si ya la operacion se indico, se opera el nuevo numero     
    elif Cal.operacion !="":        
        numeroPantalla.set(numeroPantalla.get()+num)  
        
  

#______ FILA 3 ______

buton7=Button(miFrame,text="7",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("7"))
buton7.grid(row=3,column=1)
buton8=Button(miFrame,text="8",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("8"))
buton8.grid(row=3,column=2)
buton9=Button(miFrame,text="9",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("9"))
buton9.grid(row=3,column=3)


#______ FILA 4 ______

buton4=Button(miFrame,text="4",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("4"))
buton4.grid(row=4,column=1)
buton5=Button(miFrame,text="5",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("5"))
buton5.grid(row=4,column=2)
buton6=Button(miFrame,text="6",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("6"))
buton6.grid(row=4,column=3)



#______ FILA 5 ______

buton1=Button(miFrame,text="1",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("1"))
buton1.grid(row=5,column=1)
buton2=Button(miFrame,text="2",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("2"))
buton2.grid(row=5,column=2)
buton3=Button(miFrame,text="3",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("3"))
buton3.grid(row=5,column=3)


#______ FILA 6 ______

buton0=Button(miFrame,text="0",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("0"))
buton0.grid(row=6,column=2)
butonPunto=Button(miFrame,text=".",width=4,height=1,font=('Console 24'),foreground="white",background="#2E8A99",command=lambda:numeroPulsado("."))
butonPunto.grid(row=6,column=3)


#______ Operaciones ______
#SUMA
butonSum=Button(miFrame,text="+",width=4,height=1,font=('Console 24'),foreground="white",background="gray",command=lambda:Operar("+"))
butonSum.grid(row=6,column=4,padx=2,sticky="e")
#Resta
butonRes=Button(miFrame,text="-",width=4,height=1,font=('Console 24'),foreground="white",background="gray",command=lambda:Operar("-"))

butonRes.grid(row=5,column=4,padx=2,sticky="e")
#Multiplicacion
butonMul=Button(miFrame,text="*",width=4,height=1,font=('Console 24'),foreground="white",background="gray",command=lambda:Operar("*"))
butonMul.grid(row=4,column=4,padx=2,sticky="e")
#Division
butonDiv=Button(miFrame,text="/",width=4,height=1,font=('Console 24'),foreground="white",background="gray",command=lambda:Operar("/"))
butonDiv.grid(row=3,column=4,padx=2,sticky="e")
#Igual
butonIgual=Button(miFrame,text="=",width=4,height=1,font=('Console 24'),foreground="white",background="#0163FA",command=lambda:FuncionIgual())
butonIgual.grid(row=6,column=1)
#Porcentaje
butonPorcen=Button(miFrame,text="%",width=4,height=1,font=('Console 24'),foreground="white",background="gray",command=lambda:Operar("%"))
butonPorcen.grid(row=2,column=4)
#CE
butonCE=Button(miFrame,text="CE",width=4,height=1,font=('Console 24'),foreground="white",background="#0163FA",command=lambda:BorrarUltimoNUM())
butonCE.grid(row=2,column=2)
#C
butonC=Button(miFrame,text="C",width=4,height=1,font=('Console 24'),foreground="white",background="#0163FA",command=lambda:BorrarTodo())
butonC.grid(row=2,column=3)
#Blank
imagen = PhotoImage(file=path+"\delete.png")
photoimage = imagen.subsample(9, 7)

butonBlank=Button(miFrame,image=photoimage,highlightthickness=12,height=35,background="#0163FA",command=lambda:BorrarUltimoDig())
butonBlank.grid(row=2,column=1)



 

 

raiz.mainloop()