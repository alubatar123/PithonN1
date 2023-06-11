def confirm(UserList,AvailList):
    print(UserList,AvailList)
    if UserList[1]==UserList[2]=="X" and "3" in AvailList:
        return "3"
    elif UserList[1]==UserList[3]=="X" and "2" in AvailList:
        return "2"
    elif UserList[2]==UserList[3]=="X" and "1" in AvailList:
        return "1"    
    elif UserList[4]==UserList[5]=="X" and "6" in AvailList:
        return "6"
    elif UserList[4]==UserList[6]=="X" and "5" in AvailList:
        return "5"
    elif UserList[6]==UserList[5]=="X" and "4" in AvailList:
        return "4"
    elif UserList[7]==UserList[8]=="X" and "9" in AvailList:
        return "9"
    elif UserList[7]==UserList[9]=="X" and "8" in AvailList:
        return "8"
    elif UserList[8]==UserList[9]=="X" and "7" in AvailList:
        return "7"     
    elif UserList[1]==UserList[4]=="X" and "7" in AvailList:
        return "7"
    elif UserList[1]==UserList[7]=="X" and "4" in AvailList:
        return "4"
    elif UserList[4]==UserList[7]=="X" and "1" in AvailList:
        return "1"      
    elif UserList[3]==UserList[6]=="X" and "9" in AvailList:
        return "9"
    elif UserList[3]==UserList[9]=="X" and "6" in AvailList:
        return "6"
    elif UserList[6]==UserList[9]=="X" and "3" in AvailList:
        return "3" 
    elif UserList[2]==UserList[5]=="X" and "8" in AvailList:
        return "8"
    elif UserList[2]==UserList[8]=="X" and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[8]=="X" and "2" in AvailList:
        return "2"      
    elif UserList[1]==UserList[5]=="X" and "9" in AvailList:
        return "9"
    elif UserList[1]==UserList[9]=="X" and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[9]=="X" and "1" in AvailList:
        return "1"  
    elif UserList[3]==UserList[5]=="X" and "7" in AvailList:
        return "7"
    elif UserList[3]==UserList[7]=="X" and "5" in AvailList:
        return "5"
    elif UserList[5]==UserList[7]=="X" and "3" in AvailList:
        return "3"    