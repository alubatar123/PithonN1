"""
Curso Python Nivel 1
Autor Esteban Garro Echevarria
2.	4.	Fórmula para sacar el resultado de la raíz de la suma de A más B dividiendo 
el resultado por C, con base a los valores ingresados por pantalla. 
Nota utilizar la función sqrt. 
"""
num=int(input("Ingrese un numero mayor a 0: \n"))

if num > 0:
   for row in range(1,num+1):
    for col in range(1,row+1):
          print(col, end=" ")
    print()


else:
   print("Error, el numero no es mayor que 0")