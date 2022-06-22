def run():
    
    # list_squares=[]
    # for i in range (1,101):
    #     if(i%3 != 0):

    #         list_squares.append(i**2)
    
    list_squares=[i**2 for i in range(1,10) if i%3 != 0]
    #y de esta manera podemos generar lo mismo de arriba pero con menos lineas de codigo

    list_platzi=[i for i in range(1,1001) if i%36 == 0]

    print(list_platzi)
    print(list_squares)

if __name__ == '__main__':
    run()
