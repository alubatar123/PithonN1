def CheckNextMove(UserList,AvailList,key):
    
    if UserList[1]==UserList[2]==key and "3" in AvailList:
        return "3"
    elif UserList[1]==UserList[3]==key and "2" in AvailList:
        return "2"
    elif UserList[2]==UserList[3]==key and "1" in AvailList:
        return "1"    
    elif UserList[4]==UserList[5]==key and "6" in AvailList:
        return "6"
    elif UserList[4]==UserList[6]==key and "5" in AvailList:
        return "5"
    elif UserList[6]==UserList[5]==key and "4" in AvailList:
        return "4"
    elif UserList[7]==UserList[8]==key and "9" in AvailList:
        return "9"
    elif UserList[7]==UserList[9]==key and "8" in AvailList:
        return "8"
    elif UserList[8]==UserList[9]==key and "7" in AvailList:
        return "7"     
    elif UserList[1]==UserList[4]==key and "7" in AvailList:
        return "7"
    elif UserList[1]==UserList[7]==key and "4" in AvailList:
        return "4"
    elif UserList[4]==UserList[7]==key and "1" in AvailList:
        return "1"      
    elif UserList[3]==UserList[6]==key and "9" in AvailList:
        return "9"
    elif UserList[3]==UserList[9]==key and "6" in AvailList:
        return "6"
    elif UserList[6]==UserList[9]==key and "3" in AvailList:
        return "3" 
    elif UserList[2]==UserList[5]==key and "8" in AvailList:
        return "8"
    elif UserList[2]==UserList[8]==key and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[8]==key and "2" in AvailList:
        return "2"      
    elif UserList[1]==UserList[5]==key and "9" in AvailList:
        return "9"
    elif UserList[1]==UserList[9]==key and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[9]==key and "1" in AvailList:
        return "1"  
    elif UserList[3]==UserList[5]==key and "7" in AvailList:
        return "7"
    elif UserList[3]==UserList[7]==key and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[7]==key and "3" in AvailList:
        return "3"  

    
def FirstMove(AvailList):
    return CreateList(AvailList,["1","3","7","9"])


def SecondMove(UserList,AvailList):
    result=CheckNextMove(UserList,AvailList,"X")
    if  result is not None:
        return result
    else:
        return NextCorner(UserList,AvailList)

def NextCorner(UserList,AvailList):    
    if UserList[1]=="⊙" and (all(i in AvailList for i in ["3","2"])):        
        return "3"
    elif UserList[1]=="⊙" and (all(i in AvailList for i in ["5","9"])):        
        return "9"
    elif UserList[1]=="⊙" and (all(i in AvailList for i in ["4","7"])):        
        return "7"
    elif UserList[3]=="⊙" and (all(i in AvailList for i in ["6","9"])):        
        return "9"    
    elif UserList[3]=="⊙" and (all(i in AvailList for i in ["5","7"])):        
        return "7" 
    elif UserList[7]=="⊙" and (all(i in AvailList for i in ["8","9"])):        
        return "9"
    elif UserList[9]=="⊙" and (all(i in AvailList for i in ["7","8"])):        
        return "7"


def FinalMove(UserList,AvailList):
    result=CheckNextMove(UserList,AvailList,"⊙")
    if  result is not None:
        return result
    else:
        result= CheckNextMove(UserList,AvailList,"X")
        if  result is not None:
            return result
        else:
            return NextCorner(UserList,AvailList)


def CreateList(AvailList,List):
    templist=[]
    for e in List:
        if e in AvailList:
            templist.append(e)
    return templist[0]        

