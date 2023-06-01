class Baraja:

    def __init__(self):
        self.__simbolo = ('♥','♦','♠','♣')
        self.__cartas= ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
        self.baraja= []

#Funcion que crear el mazo           
    def CreaMazo(self):
        self.baraja.clear()
        for e in self.__simbolo:
            for x in self.__cartas:
                self.baraja.append(x+" "+e)
        return self.baraja

#Funcion que da aspecto a las cartas boca arriba
    def CartaAspecto(self,*Cartas):
        
        MiCartas=["","","",""]  
        for x in Cartas:
            ListaSplit=x.split()
            if ListaSplit[0] == "10":  
                MiCartas[0]=MiCartas[0]+"  _____  "          
                MiCartas[1]=MiCartas[1]+"|"+ListaSplit[0]+"   |  "
                MiCartas[2]=MiCartas[2]+"|  "+ListaSplit[1]+"  |  "
                MiCartas[3]=MiCartas[3]+"\u0332".join("|   "+ListaSplit[0])+"|  "
            else:
                MiCartas[0]=MiCartas[0]+"  _____  "          
                MiCartas[1]=MiCartas[1]+"|"+ListaSplit[0]+"    |  "
                MiCartas[2]=MiCartas[2]+"|  "+ListaSplit[1]+"  |  "
                MiCartas[3]=MiCartas[3]+"\u0332".join("|    "+ListaSplit[0])+"|  "    

        print(MiCartas[0],"\n",MiCartas[1],"\n",MiCartas[2],"\n",MiCartas[3],"\n")

#Funcion que da aspecto con una carta boca abajo
    def CartaAspectoCrupier(self,*Cartas):
        
        MiCartas=["","","",""]  
        counter=0  
        for x in Cartas:
            ListaSplit=x.split()
            if counter == 0:
                MiCartas[0]=MiCartas[0]+"  _____  "          
                MiCartas[1]=MiCartas[1]+"|B    |  "
                MiCartas[2]=MiCartas[2]+"|  &  |  "
                MiCartas[3]=MiCartas[3]+"\u0332".join("|    J")+"|  " 
                counter= 1

            elif counter == 1 and ListaSplit[0] == "10":  
                MiCartas[0]=MiCartas[0]+"  _____  "          
                MiCartas[1]=MiCartas[1]+"|"+ListaSplit[0]+"   |  "
                MiCartas[2]=MiCartas[2]+"|  "+ListaSplit[1]+"  |  "
                MiCartas[3]=MiCartas[3]+"\u0332".join("|   "+ListaSplit[0])+"|  "
            else:
                MiCartas[0]=MiCartas[0]+"  _____  "          
                MiCartas[1]=MiCartas[1]+"|"+ListaSplit[0]+"    |  "
                MiCartas[2]=MiCartas[2]+"|  "+ListaSplit[1]+"  |  "
                MiCartas[3]=MiCartas[3]+"\u0332".join("|    "+ListaSplit[0])+"|  "    

        print(MiCartas[0],"\n",MiCartas[1],"\n",MiCartas[2],"\n",MiCartas[3],"\n")        


