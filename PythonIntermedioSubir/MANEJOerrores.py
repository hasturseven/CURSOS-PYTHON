

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    correcto = True
    while correcto:
        try:
            num = int(input('Ingresa un número: '))
            if num <= 0:
                raise ArithmeticError('no puedes ingresar iguales o mejores que cero')
            print(divisors(num))
            print("Terminó mi programa")
            correcto = False
        except ValueError:
            print("no puedes ingresar letras o palabras")
        except ArithmeticError as negativos:
            print(negativos)


if __name__ == '__main__':
    run()
