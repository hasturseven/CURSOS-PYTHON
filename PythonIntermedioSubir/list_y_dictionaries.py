
def run():
    my_list=[1,"hola",True,4.6]
    my_dict = {'firstname':'sergio','lastname':'andres'}

    super_list = [
        {'firstname':'sergio','lastname':'andres'},
        {'firstname':'yamid','lastname':'julian'},
        {'firstname':'adriana','lastname':'maria'},
        {'firstname':'jader','lastname':'de jesus'},
        {'firstname':'yesid','lastname':'francisco'}
    ]

    super_dict={
        'natural_nums':[1,2,3,4,5],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums':[1.2 , 5.2 , 4.8]
    }
    
#imprimiendo los diccionarios que estan dentro de una lista
    for key, value in super_dict.items():
        print(key," ", value)

    print("\n")
    print("estos son los diccionarios que estan dentro de una lista")
    print()

    for dic in super_list:
        for key,value in dic.items():
            print(key," ", value)
    
    list_nums_to_elavate=[]
    for i in range(100):
        list_nums_to_elavate.append(i**2)

    for i in list_nums_to_elavate:
        print(i)





if __name__== '__main__':
    run()