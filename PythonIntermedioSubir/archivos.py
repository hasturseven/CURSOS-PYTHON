def write():
    names=['sergio','yamid','adriana','jader']
    with open("./archivos/names.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def read():
    number = []
    with open("./archivos/number.txt","r",encoding="utf-8") as f:
        #estamos recorriendo linea a linea para ver que tiene y lo garamos en mi lista
        for line in f:
            number.append(int(line))
    print (number)




def run():
    write()



if __name__=='__main__':
    run()