from functools import reduce #TENEMOS QUE IMPORTAR REDUCE PARA PODER USARLO 


#funcion de orden superior es una funcion que recibe como parametro una funcion ej:
def saludo(funcion):
    funcion()

def saludar():
    print("hola!!!")

def despedir():
    print("adios!!!")

saludo(saludar)
saludo(despedir)

#________________________---¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿

#FILTER

my_list =[1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, my_list))
print(odd)

#de esta manera añadimos solo los numeros pares el list() nos sirve para
#convertir lo retornado en lista .
#la funcion filter recibe dos parametros una funcion anonima , y un iterable
#donde x es los objetos que estan en mi iterable (en este caso la lista)
#entonces se realiza la condicion si son par se agregan si no no

#MAP
my_list1 = [1,2,3,4,5]
squares =list(map(lambda x:x**2,my_list1))
print(squares)
#mismo caso lis() me trasforma lo que me regresa map que es un iterable en lista
#map(tiene dos argumetnos) 1 una funcion anonima, y otra el objeto iterable lo 
#mismo que en filter pero en este caso operaremos cada entrada osea le entrada = salida
#el mismo caso x son cada valor de la lista , los o peramos y guardamos en la nueva lsita


#REDUCE
list2=[2,2,2,2,2]
all_multiplied = reduce(lambda a,b: a*b,list2)
print(all_multiplied)
#LI MISMO QUE EN LAS OTRAS PERO RECIBE DO ARGUMENTOS LOS CUALES SON A Y B QUE SERAN LOS DOSP RIMEROS TERMINO DE LA LISTA