
def Continuar():
    """
    Funcion que permite cancelar o seguir el programa retorando True para Yes, False para No
    """
    Conti=True
    #Solicita al usuario confirmar con Y o N si desea ingrear mas numeros
    while Conti:
        Confirmar=(input("Desea tratar de nuevo?:y/n "))
        if Confirmar=="y" or Confirmar=="Y":
            return True
        elif Confirmar=="n" or Confirmar=="N":
             Conti=False
            #Si el usuario ingresa Otro dato, se muestra error           
        else:
            print("Opcion Invalida")

def IngresaDAto(max,param1,param2,param3):
    """
    Esta funcion valida que los datos sean del formato adecuado\n
    Max= cantidad de valores necesarios para los calculos\n
    Param1= Nombre de parametro 1\n
    Param2= Nombre de parametro 2\n
    Param3= Nombre de parametro 3
    """
    Valores=[0,0,0]
    Datos=[param1,param2,param3]
    i=0
    #funcion que pide el dato a verificar
    
    while i<max:
        Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
        while True:
            #Llama VerificaNumero siempre que el dato ser numerico
            try:
                Valores[i]=(float(Numero))           
                i+=1
            #Excepcion controlada en caso de ingresar un dato no numerico
                break
            except ValueError:
                print("Valor invalido, intente de nuevo")
                Numero=(input(f"Ingrese el valor de {Datos[i]} :"))
    #Almacenamos el resultado del generador en el iterador Migenerador   
    return Valores[0],Valores[1],Valores[2]              

