from ast import Return
from tkinter.messagebox import RETRY


class PuestoVotacion:
    def __init__(self,identificador,pais) :
        self.__pais=pais
        self.__identificador=identificador
        self.__region=None
    
    #al poner el property estoy definiendo qeu cierto atributo tendra un get y lo que me da cabida a crear e get,seter,y deleter
    #recordando que cualquier cosa que tenga un arroba se puede decir que es un decorador
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self,region):
        if region in self.__pais:
            self.__region=region
        else:
            raise ValueError(f'la region {region} no es valida en {self.__pais}')
    

puestoVota=PuestoVotacion(123,['colombia','bogota'])
print(puestoVota.region)
puestoVota.region='bogota'
print(puestoVota.region)


