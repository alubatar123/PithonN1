import ast

class Usuario:
 
    def __init__(self):
        self.Nombre=None
        self.Ganes=0
        self.DERROTAS=0
        self.DicUsuario={}
        self.NewDicUsuario={"NOMBRE":"","GANES":"","DERROTAS":""}


    def BuscaUsuario(self):        
        print("")
        counter=1
        TempDic={}
        #Crea un dic temporarl con el ID y Nombre del usuario
        for Lv1Key,Lv2Key in self.ListaUsuario().items():            
            print(f"({counter})",Lv1Key,Lv2Key)        
            TempDic[counter]=Lv1Key        
            counter+=1
        print("(R) Regresar")    
        
        return TempDic

    def StatUser(self,ElUsuario):
        self.Leer()
        #Reporta los ganes y derrotas de cada usuario, y remueve corchete y simbolos        
        print(*[str(k) + ' = ' + str(v) for k,v in self.DicUsuario[ElUsuario].items()], sep='\n')

    def Leer(self):
        with open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt','r') as archivo:
            data = archivo.read()        
            self.DicUsuario = ast.literal_eval(data)
            
    def Registrar(self):
        NuevoUser=(input("\nDigite el nombre del nuevo usuario: "))    
        self.Leer()
        Exist=True
        #Separa el Dic anidado por usuario para ser recorrido
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
            self.ActualizaDic(len(self.DicUsuario.keys())+1,NuevoUser) 
            print("\nEl usuario '",NuevoUser,"' ha sido registrado\n") 
        return (Exist)     
    

    def ListaUsuario(self):
        self.Leer()
        TempDic={}    
        for Lv1Key,Lv2Key in self.DicUsuario.items():
            
            for k in Lv2Key:
                if k== "NOMBRE":
                    TempDic[Lv1Key]=Lv2Key["NOMBRE"]
        return TempDic            

    def ActualizaDic(self,ID,Nombre,GANES=0,DERROTAS=0):        
        self.NewDicUsuario["NOMBRE"]=Nombre
        self.NewDicUsuario["GANES"]=GANES
        self.NewDicUsuario["DERROTAS"]=DERROTAS
        self.DicUsuario["USUARIO"+str(ID)]=self.NewDicUsuario
        self.__Escribir(self.DicUsuario)
        


    def __Escribir(self,NewDic):
        
        open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt', 'w').close()
        with open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt','a') as archivo:
            
            archivo.write(str(NewDic))
                
           





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

