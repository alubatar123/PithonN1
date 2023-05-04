"""
Practica de evaluación corta 2
Curso Python Nivel 1
Autor Esteban Garro Echevarria

3.	 Un programa para adivinar un número al azar entre 1 y 10. 
Utilizar la librería “import random”, investigar sobre random.randrange. 

"""

import random
#establece un numero random del 1 al 10
NumReal=(random.randrange(1, 11))

def AdivinaNum():
    #Funcion que permite adivinar el numero random
    while True:
        try:
            Trivia=int(input("¿Cual es el numero ganador? "))
            if Trivia<1 or Trivia>10:
                print("Solo numeros del 1 al 10 se permiten")
                AdivinaNum()
            elif Trivia==NumReal:
                print("Felicidades adivinó!")
            else:
                print("Respuesta incorrecta, trate de nuevo")
                AdivinaNum()
            break
        except ValueError:
            print("Valor invalido")

AdivinaNum()