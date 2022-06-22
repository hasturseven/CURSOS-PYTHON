


def is_palindrome(palabra:str)-> bool:
    palabra = palabra.replace(" ","").lower()
    return palabra == palabra[::-1]

def is_prime(numero:int)-> bool:
    disivible:int=0;
    for i in range(1,numero+1):
        if numero%i == 0:
            disivible +=1
    if disivible==2:
        return True
    else:
        return False
#PARA QUE MEM UESTRE LOS ERRORES DE TIPO TENGO QUE EJECUTAR EN LA TERMINAR EL SIG COMANDO mypy nmbreaArchivo.py --check-untyped-defs


def run():
    print(is_palindrome(input('ingresa una palabra')))
    print(is_prime(int(input('ingrese un numero entero'))))

if __name__ == '__main__':
    run()
