class Lavadora:
    def __init__(self):
        pass

    def lavar(self,temp='caliente'):
        self._llenar_tanque(temp)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self,temp):
        print(f'llenando el tanque con aguia{temp}')
    
    def _anadir_jabon(self):
        print('añadiendo jabon')
    
    def _lavar(self):
        print('lavando ropa')
    
    def _centrifugar(self):
        print('esta centrifugando')
    
def run():
    lavadora =Lavadora()
    lavadora.lavar()

if __name__=='__main__':
        run()