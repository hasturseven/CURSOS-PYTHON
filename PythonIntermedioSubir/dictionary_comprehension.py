
#se aplica lo mismo que en la list_comprehension

import math


def run():
    #creando un diccinario con los 100 numeros elevados a la 3
    dictionary_comprehension={i:i**3 for i in range(1,101)  }

    print(dictionary_comprehension)

    #creando un diccionario  las primeras 100 raices cuadradas de cada numero del uno al 100
    dictionary_square={i: round(math.sqrt(i),2) for i in range(1,101)}
    print(dictionary_square)


if __name__=='__main__':
    run()