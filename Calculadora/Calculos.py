
operacion=""
valor1=0
First=True
#2.4/3
def Limpiar():
    global First,valor1,operacion
    First=True
    valor1=0
    operacion=""

def Operate(valor2):
    resultado=0    
    try:
        if operacion=="+":
            resultado= suma(valor2)
        elif operacion=="-":
            resultado= resta(valor2)    
        elif operacion=="*":
            resultado= Multi(valor2)
        elif operacion=="/":
            resultado= Division(valor2)       
        elif operacion=="%":
            resultado= Porcentaje(valor2)  

        if resultado == "Err ":
            Limpiar()
            return resultado
        elif resultado==0.00:
            return 0
        elif resultado/int(resultado)==1:
            return int(resultado)              
        else:
            return ("%.2f" % round(resultado, 2)) 
    except ZeroDivisionError:
        return ("%.2f" % round(resultado, 2)) 

def suma(valor2):
    global valor1
    valor1+=valor2    
    return valor1

def resta(valor2):
    global valor1
    if First is True:    
        valor1=valor2    
    else:
        valor1-=valor2
    return valor1

def Multi(valor2):
    global valor1
    if First is True:    
        valor1=valor2    
    else:
        valor1*=valor2
    return valor1

def Division(valor2):
    global valor1
    try:
        if First is True:    
            valor1=valor2    
        else:
            valor1/=valor2
        return valor1
    except ZeroDivisionError:
        return "Err "


def Porcentaje(valor2):
    global valor1
    try:
        if First is True:    
            valor1=valor2    
        else:
            valor1/=valor2
        return valor1
    except ZeroDivisionError:
        return "Err "