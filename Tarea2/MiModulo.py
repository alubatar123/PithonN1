
def Continuar():
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("Desea tratar otro numero?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            return True
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
            #Si el usuario ingresa Otro dato, se muestra error           
        else:
            print("Opcion Invalida")

def IngresaDAto():
    
    Valores=[]
    Datos=["a","b","c"]
    i=0
    #funcion que pide el dato a verificar
    
    while i<3:
        Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
        while True:
            #Llama VerificaNumero siempre que el dato ser numerico
            try:
                Valores.append(float(Numero))           
                i+=1
            #Excepcion controlada en caso de ingresar un dato no numerico
                break
            except ValueError:
                print("Valor invalido, intente de nuevo")
                Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
    #Almacenamos el resultado del generador en el iterador Migenerador   
    return Valores[0],Valores[1],Valores[2]              

    #print(Migenerador)