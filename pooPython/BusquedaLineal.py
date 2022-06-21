from pickle import TRUE
import random

def busqueda_lineal(lista,objetivo):
  match=False
  for elemento in lista:
    if elemento == objetivo:
      match=True
      break
  return match


tam_de_lista=int(input('de que tamano sera la lista?'))
objetivo=int(input('que numeros quieres encontrar'))
lista=[]
for i in range(tam_de_lista):
    lista.append(random.randint(0,1000))
# lista=[ for i in range(tam_de_lista) random.random.randint(0 , 100)] esta forma esta mal de crearlo
#de esta manera le metemos numeros aleatorios segun el tam que se especifique de la lista

encontrado=busqueda_lineal(lista,objetivo)

print(lista)
print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')