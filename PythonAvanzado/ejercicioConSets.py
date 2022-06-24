my_set_familia={"sergio","adriana","yamid","jader"}
my_set_amigos={"sergio","yamid","franco","wholfan","stiven"}

my_set_union=my_set_familia.union(my_set_amigos)

my_set_interseccion=my_set_familia.intersection(my_set_amigos)

my_set_diferencia=my_set_familia.difference(my_set_amigos)

my_set_diferencia_simetrica=my_set_familia.symmetric_difference(my_set_amigos)

print(my_set_interseccion," ",my_set_diferencia," ", my_set_diferencia_simetrica," ",my_set_union)
