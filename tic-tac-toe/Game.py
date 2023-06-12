import time
import random
import Possibilities as PO
cat=(
"""
             /)
     /\___/\ ((
     \`@_@'/  ))
     {_:Y:.}_//
 ____{_}^-'{_}____
""")

table=[["|  TIC  TAC  TOE  |"],
       ["|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|"],       
       ["|  7  ","|  8  ","|  9  ","|"],
       ["|     |     |     |"], 
       ["|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|"],                     
       ["|  4  ","|  5  ","|  6  ","|"],
       ["|     |     |     |"], 
       ["|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|"],               
       ["|  1  ","|  2  ","|  3  ","|"],
       ["|_____|_____|_____|"]]

Avail=[str(x) for x in range(1,10)]
realtable=Avail.copy()
realtable.insert(0,"0")
def display_board(board):
    print(cat,end="")
    for line in board:
        for element in line:
            print(element,end="")
        print()

    


def enter_move(key,Move):
    
    global table, Avail,realtable 
    for line in range(len(table)):
        for element in range(len(table[line])):
            for character in table[line][element]:
                if Move in character:
                    table[line][element]="|  "+key+"  "
                    Avail.remove(Move)
                    realtable = list(map(lambda x: x.replace(character, key), realtable))
                
                            
    display_board(table)


def Next_User_Move(PCmove):  
    Move=input("-TURNO DEL USUARIO-\nDigite numero de casilla: ")  
    if Move not in Avail:
        print("Numero o opcion no disponible")
        Next_User_Move(PCmove)       
    else:
        enter_move("X",Move)
        if Final() is False:            
            draw_move(PCmove)



def ConfirmVictory():
    if realtable[1]==realtable[2]==realtable[3]:
        return realtable[1]
    elif realtable[1]==realtable[4]==realtable[7]:
        return realtable[1]
    elif realtable[1]==realtable[5]==realtable[9]:
        return realtable[1]
    elif realtable[2]==realtable[5]==realtable[8]:
        return realtable[2]
    elif realtable[3]==realtable[5]==realtable[7]:
        return realtable[3]    
    elif realtable[3]==realtable[6]==realtable[9]:
        return realtable[3] 
    elif realtable[4]==realtable[5]==realtable[6]:
        return realtable[4]    
    elif realtable[7]==realtable[8]==realtable[9]:
        return realtable[7]        
    

def Over():
    temp=[]
    for e in realtable:
        if e.isnumeric():
            temp.append(e)                
    return len(temp)            

def Final():
    result=ConfirmVictory()      
    if result is None:        
        if Over()== 1:
            print("No HAY MAS CASILLAS DISPONIBLES. NO HUBO GANADOR")
            return True
        else:            
            return False
    elif result == "X":
        print("FELICIDADES, USTED GANÓ")
        return True
    elif result == "⊙": 
        print("LO SENTIMOS, HA PERDIDO")
        return True  

def draw_move(move_number):
    print("--TURNO DE LA PC--"),time.sleep(1)  
    if move_number==1:               
        enter_move("⊙",PO.FirstMove(Avail))
        if Final() is False:
            Next_User_Move(2)
    elif move_number==2:             
        enter_move("⊙",PO.SecondMove(realtable,Avail))
        if Final() is False:
            Next_User_Move(3)
    elif move_number==3:            
        enter_move("⊙",PO.FinalMove(realtable,Avail))
        if Final() is False:
            Next_User_Move(3)  

    
while True:
    print()
    for x in range (0,5):  
        b = " **CARGANDO-NUEVA-PARTIDA"+ "." * x
        print (b, end="\r")
        time.sleep(0.8)      
    print("\n"*18)
    display_board(table)
    Next_User_Move(1)
