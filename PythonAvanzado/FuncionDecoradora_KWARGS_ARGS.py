from datetime import datetime
# importamos el modulo para trabar con fechas o mirar el tiempo en este caso  que tarda en ejecutarse una funcion


def execution_time(func):

    """esto sirve para saber cuanto tiempo tarde una funcion en ejecutarse
    #  AHORA LE AGREGAREMOS AL WRAPPER los *args: que son los argumentos que no estan definidos en una funcion ejemplo fun(a,b)
    #  y tambien los **kwargs: que son los argumentos nombrados o definidos ejemplo fun(nombre='sergio') y el * (asterisco ) 
    #  y ** (doble asterisco para kwargs): nos indica que no     importara cuantos args o kwargs tenga los reciba todos """
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()  # momento y fehca exacta en que se ejecuta el codigo

        """y ahora al llamar esta func() osea la que genero el llamado al decorador le estaremos pasando los argumentos que requiera
        ya que estos como dije antes son recordados por la funcion decoradora este caso execution_time"""
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time

        print('pasaron '+str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper


@execution_time
# cuando queremos hacer un for y no nos importa la variable a rrecorrer se le pone
# un _ para no usarla
def random_func():
    for _ in range(1, 100000000):
        pass


@execution_time
# los argumentos que no estan definidos son los *args en este caso a y b son args
def suma(a: int, b: int) -> int:
    """ahora estariamos pasadole dos argumentos al decorador que son los que tiene esta funcion
    # siempre que llamemos un decorador a una funcoin que tenga un argumento O MAS ESTOS
    # SERAN ENVIADOS AL DECORADOR TENDRA CONOCIMIENTO DE ESTAS LAS CUALES LAS PASARA EL WRAPPER"""
    return a+b


@execution_time
# al pasar un parametro definido como en este caso nombre se determina como **kwargs
def saludo(nombre='cesar'):
    print('hola ' + nombre)


"""
entonces como usamos un decorador el cual puede recibir cuantos argumentos quiera lo podemos 
usar para cualquier funcion GENERALMENTE ES SIEMPRE MEJOR HACER LOS DECORADORES CON ESTE TIPO
DE *args y **kwargs

"""
suma(3, 5)
random_func()
saludo()
