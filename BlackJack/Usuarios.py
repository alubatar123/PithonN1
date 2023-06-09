import ast
import os

class Usuario:


#clase que almacena datos de usuario y funciones relacionadas
    def __init__(self): 
        self.DicUsuario={}
        self.NewDicUsuario={"NOMBRE":"","GANES":"","DERROTAS":"","EMPATES":""}
        self.path='C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt'



    def BuscaUsuario(self):        
        print("")
        counter=1
        TempDicUserID={}
        TempDicUserName={}
        #Crea un dic temporarl con el ID y Nombre del usuario        
        for Lv1Key,Lv2Key in self.ListaUsuario().items():            
            print(f"({counter})",Lv1Key,Lv2Key)        
            TempDicUserID[counter]=Lv1Key
            TempDicUserName[counter]=Lv2Key    
            counter+=1
        if len(TempDicUserID)>0:
            print("(R) Regresar")           
        
        return TempDicUserID,TempDicUserName

#funcion que regresa datos de usuario
    def StatUser(self,ElUsuario):
        self.Leer()
        stas=[]
        for e,k in self.DicUsuario[ElUsuario].items():
            stas.append(k)
        return stas    

#funcion que lee la Base de datos
    def Leer(self):
        with open(self.path,'r') as archivo:
            data = archivo.read() 
            #Revisa si el archivo esta vacio   
            if os.stat(self.path).st_size==0:
                self.DicUsuario={}                        
            #si existe contenido lo almacena en un dicccionario anidado
            else:                
                self.DicUsuario = ast.literal_eval(data)
            
    def Registrar(self):
        NuevoUser=(input("\nDigite el nombre del nuevo usuario: "))    
        
        Exist=True
        #Separa el Dic anidado por usuario para ser recorrido
        self.Leer()
            
        for e in self.DicUsuario.values():            
            #se hace un dic temporal con Valores en minisculas
            new_dict = dict((k, str(v).lower()) for k, v in e.items())
            #si el usuario ya existe en minuscula se muestra error
            if any(NuevoUser.lower() in d for d in new_dict.values()) ==True: 
                print("\nLo sentimos, ese usuario ya existe\n")
                Exist=False
                break
        if Exist:
            #Si no existe se registra el usuario
            UserID= "USUARIO"+str(len(self.DicUsuario.keys())+1)                 
            self.ActualizaDic(UserID,NuevoUser) 
            print("\nEl usuario '",NuevoUser,"' ha sido registrado bajo",UserID,"\n") 
        return (Exist),[UserID,NuevoUser]     
        
#funcion que permite crear una lista de los usuarios 
    def ListaUsuario(self):
        self.Leer()
        TempDicUserID={}    
        for Lv1Key,Lv2Key in self.DicUsuario.items():
            
            for k in Lv2Key:
                if k== "NOMBRE":
                    TempDicUserID[Lv1Key]=Lv2Key["NOMBRE"]
        return TempDicUserID            
#funcion que actualiza la BD
    def ActualizaDic(self,USER,Nombre,GANES=0,DERROTAS=0,EMPATES=0):        
        self.NewDicUsuario["NOMBRE"]=Nombre
        self.NewDicUsuario["GANES"]=GANES
        self.NewDicUsuario["DERROTAS"]=DERROTAS
        self.NewDicUsuario["EMPATES"]=EMPATES
        self.DicUsuario[USER]=self.NewDicUsuario
        self.__Escribir(self.DicUsuario)
        

#funcion que pase los datos actualizado al archivo
    def __Escribir(self,NewDic):        
        open(self.path, 'w').close()
        with open(self.path,'a') as archivo:            
            archivo.write(f"{str(NewDic)}")
            
                
           





#ob = Usuario()
#ob.Registrar()
# #ob.Escribir()
# #ob.Leer()
# #
# # print(ob.NewDicUsuario)
# ob.ActualizaDic(1,"Goku")
# ob.ActualizaDic(3,"Napa")
# ob.ActualizaDic(3,"Napa",100,50)
# print(ob.ListaUsuario())

