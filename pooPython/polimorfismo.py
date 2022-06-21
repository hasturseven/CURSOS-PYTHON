from cProfile import run


class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def avanza(self):
        return ('ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def avanza(self):
        return super().avanza() + 'soy un crack'

def run():
    persona =Persona('sergio')
    print(persona.avanza())

    ciclista = Ciclista('andres')
    print(ciclista.avanza())

    


if __name__=='__main__':
    run()