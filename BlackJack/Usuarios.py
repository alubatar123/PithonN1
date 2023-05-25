import ast
import json
class Usuario:
    import ast 
    import json  
    def __init__(self):
        self.Nombre=None
        self.Ganes=0
        self.Perdidas=0
        self.DicUsuario={}
        self.NewDicUsuario={"NOMBRE":"","GANES":"","PERDIDAS":""}


    #def Actualizar(self,Nombre,Gane,Derrota):


    def Leer(self):
        with open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt','r') as archivo:
            data = archivo.read()        
            self.DicUsuario = ast.literal_eval(data)
            print("hola",self.DicUsuario)


    def ListaUsuario(self):
        self.Leer()
        
        
        for Lv1Key,Lv2Key in self.DicUsuario.items():
            
            for k in Lv2Key:
                if k== "NOMBRE":
                    print(Lv1Key,Lv2Key["NOMBRE"])

    def AgregaUser(self,ID,Nombre):        
        self.NewDicUsuario["NOMBRE"]=Nombre
        self.NewDicUsuario["GANES"]=0
        self.NewDicUsuario["PERDIDAS"]=0
        self.DicUsuario["USUARIO"+str(ID)]=self.NewDicUsuario
        self.__Escribir(self.DicUsuario)
        


    def __Escribir(self,NewDic):
        
        open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt', 'w').close()
        with open('C:/Users/Chango/Desktop/Python/Curso/PithonN1/BlackJack/BD.txt','a') as archivo:
            #for e in NewDic.keys():
            archivo.write(str(NewDic))
                #print(str(e)+"\n")
           





ob = Usuario()
#ob.Escribir()
#ob.Leer()
#
# print(ob.NewDicUsuario)
ob.AgregaUser(1,"Goku")
ob.AgregaUser(3,"Napa")

ob.ListaUsuario()

