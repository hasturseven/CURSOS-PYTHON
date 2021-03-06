#ejemplo de operaciones sobre sets 
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 

#añadiendo un elemento al set 
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set 
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 

#Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:

#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple= ('hola', 'hola', 1, 2)
my_set2= set(my_tuple)
print(my_set2) #Output {'hola', 1}

#-------------------------------- operacion con sets
#Unión

#Resultado de juntar todos los elementos que tienen ambos, combinar ambos sets

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 | set_2 #  -> {1, 2, 3, 4, 5}

# O de forma mas explicita
print(set_1.union(set_2)) #  -> {1, 2, 3, 4, 5}

#Intersección

#Los que se repiten en ambos sets

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 & set_2 #  -> {3}

# O de forma mas explicita
set_1.intersection(set_2) #  -> {3}

#Diferencia

#Tomar dos sets y de uno quitarle todos los elementos que tiene el otro

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 - set_2 #  -> {1, 2}

# O de forma mas explicita
set_1.difference(set_2) #  -> {1, 2}

#Diferencia Simétrica

#Tomar todos los elementos exceptos los que se repiten

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 ^ set_2 #  -> {1, 2, 4, 5}

# O de forma mas explicita
set_1.symmetric_difference(set_2) #  -> {1, 2, 4, 5}