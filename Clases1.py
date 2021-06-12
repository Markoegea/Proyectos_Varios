class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def getNombre(self):
        return self.nombre

persona1= Persona('Lincoln','Kant','70')
print(persona1.getNombre())
