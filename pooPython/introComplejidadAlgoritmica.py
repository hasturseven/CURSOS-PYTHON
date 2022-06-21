import time
import sys

def factorial(n):
  respuesta=1
  while n > 1:
    respuesta*=n
    n -=1
  return respuesta

def factorial_recursivo(n):
  if n == 1:
    return 1
  return n * factorial_recursivo(n-1)


sys.setrecursionlimit(3000000)


n=100000

comienzo= time.time()
print(factorial(n))

final=time.time()

total=final-comienzo

print(f'tiempo tardado con la funcion normal ({total})')

comienzo= time.time()


print(factorial_recursivo(n))
final=time.time()
total=final-comienzo

print(f'tiempo tardado con la funcion recursiva {total}')