# [1,1,2,2,4] -> [1,2,4]

def remove_duplicates(some_list):
    set_para_quitar_los_duplicados=set(some_list)
    
    #al usar el for guardamos cada elemento pero como os set no guardan los elementos repetidos entonces 
    # me da la lista sin elementos repetidos y es mas facil que el codigo que hice sin sets
    return list(set_para_quitar_los_duplicados)

def run():
    random_list=[1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()