from persona import Persona


class Deportista(Persona):
    
    def __init__( self, nombre, edad, altura, sexo, deporte= " ", años = 0):
        super.__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._añosPracticando = deporte
        

    def get (self):
       return  self._añosPracticando
    
    def get (self):
        return self._deporte
