from tkinter import *
from tkinter import messagebox
import sqlite3
import os
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)


#-----------------------------Funciones-----------------------------

def conexionBBDD():
    
    miConexion=sqlite3.connect("Curso\PithonN1\MyBDApp\MiUsuarios.sqlite3")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
                CREATE TABLE DATAUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMMENTARIOS VARCHAR(100)
                )''')
        messagebox.showinfo("BBDD","BBDD creada")
    except:
        messagebox.showwarning("ERROR,", "La BBDD ya existe")
    miConexion.close()



def BorraBBDD():
    
    if (os.path.exists('Curso\PithonN1\MyBDApp\MiUsuarios.sqlite3'))==True:
        ok=messagebox.askokcancel("Borrar BD", "Esta accion borrara toda la BD, desea continuar?")
        if ok is True:
            os.remove('Curso\PithonN1\MyBDApp\MiUsuarios.sqlite3')        
            messagebox.showinfo("BBDD","BBDD borrada")
    else:
        messagebox.showwarning("BBDD","No existe BD activa")    


def salirApp():
    valor=messagebox.askquestion("Salir","¿Desea salir?")
    if valor=="yes":
        root.destroy()


def limpiarCampos():
    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0,END)#para texto se usa delete. 1.0= punto de partida

def Crear():
    miConexion=sqlite3.connect("Curso\PithonN1\MyBDApp\MiUsuarios.sqlite3")
    miCursor=miConexion.cursor()
    #Usamos NULL xq es autonumerico
    miCursor.execute("INSERT INTO DATAUSUARIOS VALUES(NULL,'"
                     +miNombre.get()+"','"
                     +miPass.get()+"','"
                     +miApellido.get()+"','"
                     +miDireccion.get()+"','"
                     +textoComentario.get("1.0",END)+"')")
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro Asignaod")
    miConexion.close()

#-----------------------------Barra menu-----------------------------
BDMenu=Menu(barraMenu,tearoff=0)
BDMenu.add_command(label="Conectar",command=conexionBBDD)
BDMenu.add_command(label="BorrarBD",command=BorraBBDD)
BDMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=Crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licensia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD",menu=BDMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#----------------------------------CAMPOS#----------------------------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------------LABELS------------------------------

idLabel=Label(miFrame,text="ID:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

NombreLabel=Label(miFrame,text="Nombre:")
NombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

PassLabel=Label(miFrame,text="Password:")
PassLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

ApellidoLabel=Label(miFrame,text="Apellido:")
ApellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

DireccionLabel=Label(miFrame,text="Direccion:")
DireccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

CommentLabel=Label(miFrame,text="Comentarios:")
CommentLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)


#-----------------Botones------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Create",command=Crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer")
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar")
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Borrar")
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)


root.mainloop()