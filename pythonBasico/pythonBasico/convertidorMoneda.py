opcion = input("1)para convertir de pesos a dolares \n 2)para convertir de dolares a pesos")

if opcion=='1':
    pesos = float(input("cuantos pesos colombianos desea transformar"))
    endoalres=0
    endoalres=(pesos*0.00025)
    print(endoalres)
else:
    dolares = float(input("cuantos dolares tiene para transformar a pesos colombianos"))
    pesosconver= round((dolares*4001),2)
    print(pesosconver)



