import time 

class fiboIter():
    #metodos necesarios para hacer una clase que sea iterador son dos el iter y el next algo asi como lo que pasaba con los threads en java

    #primer metodo qu ees el que convierte el objeto iterador en un iterable 
    def __iter__(self):
        #entonces como en fibo se necesita la suma de dos numeros que son los que suman para que me de el siguiente resultado
        self.n1=0
        self.n2=1
        self.counter=0
        return self
        
    #segundo metodo que nos da el siguiente valor 
    def __next__(self):
        if self.counter ==0:
            self.counter +=1
            return self.n1
        elif self.counter ==1:
            self.counter+=1
            return self.n2
        else:
            self.aux=self.n1+self.n2
            #self.n1=self.n2
            #self.n2=self.aux
            #generand un suag un intercambio de varables en python
            self.n1 , self.n2=self.n2,self.aux
            self.counter +=1
            return self.aux


if __name__=="__main__":

    fibonacci =fiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1) #pausa un segundo despues de imprimir cada elemento
