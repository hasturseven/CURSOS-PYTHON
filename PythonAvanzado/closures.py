#CLORUSRES SON FUNCIONES QUE TIENEN OTRA FUNCION ANIDADA PERO ESTA FUNCION QUE ANIDA LA OTRA FUNCION LA DEBE RETORNAR EJEMPLO


def ingresa_palabra(palabra):
    def repetir_cadena(repeteiciones):
        return palabra*repeteiciones
    return repetir_cadena

#acabamos de crear un closures el cual es una funcion anidando otra el ucal la retorna 

#ahroa usandola para poder usarla debemos guardarla en una variable ya que quiero que guarde una varibale local o globar que se tiene en alguna de estas dos funciones para que la pueda retirnar en este caso es la mutiplicacion de esas cadenas osea las veces qeu se repetira oara poder verla asi estemos fuera del alcance de esa variable

palabraRepetir=ingresa_palabra("  sergio es un crack  ")

print(palabraRepetir(5)) #con esto hacemos que la palabra que escribi se repita 5 veces usando closures


def make_division(divisor):
    def make_dividendo(dividendo):
        return dividendo/divisor
    return make_dividendo

dividir_por=make_division(float(input('ingresa el numero el cual sera el divisor')))

print(dividir_por(float(input('ingresa el numero que sera el dividendo'))))


