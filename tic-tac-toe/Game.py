import time
import random
import Possibilities as PO
cat=(
"""
          /)
  /\___/\ ((
  \`@_@'/  ))
  {_:Y:.}_//
 _{_}^-'{_}_
""")

table=[["|__G_A_T_O__|"],
       ["|_7_","|_8_","|_9_","|"],
       ["|_4_","|_5_","|_6_","|"],
       ["|_1_","|_2_","|_3_","|"]]

Avail=[str(x) for x in range(1,10)]
realtable=Avail.copy()
realtable.insert(0,"0")
def display_board(board):
    print(cat,end="")
    for line in board:
        for element in line:
            print("\u0332".join(element).upper(),end="")
        print()
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    


def enter_move(key,Move):
    global table, Avail,realtable 
    for line in range(len(table)):
        for element in range(len(table[line])):
            for character in table[line][element]:
                if Move in character:
                    table[line][element]="|_"+key+"_"
                    Avail.remove(Move)
                    realtable = list(map(lambda x: x.replace(character, key), realtable))
                
                            
    display_board(table)
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass

def Next_User_Move(PCmove):  
    Move=input("Turno del Usuario\nDigite numero de casilla: ")  
    if Move not in Avail:
        print("Numero o opcion no disponible")
        Next_User_Move()       
    else:
        enter_move("X",Move)
        draw_move(PCmove)



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass

def draw_move(move_number):
    
    if move_number==1:
        print("Turno PC"),time.sleep(1)         
        enter_move("⥀",PO.FirstMove(Avail))
        Next_User_Move(2)
    elif move_number==2:
        print("Turno PC"),time.sleep(1)        
        enter_move("⥀",PO.ContraUser(realtable,Avail))
        Next_User_Move(3)
    elif move_number==3:
        print("Turno PC"),time.sleep(1)        
        enter_move("⥀",PO.FinalMove(realtable,Avail))
        Next_User_Move(3)  

    

display_board(table)
Next_User_Move(1)
