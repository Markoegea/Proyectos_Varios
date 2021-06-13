class Persona:
    def __init__(self, nombre='anonimo',apellido='',edad=0):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    @property
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getEdad(self):
        return self.edad

    def setNombre(self):
        self.nombre = input('Cual es tu nombre?\n')
        return self.nombre
    
    def imprimirPersona(self):
        return '\nNombre: ' + self.setNombre() + '\nApellido: ' + self.getApellido() + '\nEdad: ' + str(self.getEdad())

class Estudiante(Persona):

    def __init__(self,nombre='John',apellido='Doe',edad='?'):
        super().__init__(nombre='John',apellido='Doe',edad='?')

    def imprimirPersonaOtraVez(self):
        return '\n Otro nombre:\nNombre: ' + self.setNombre() + '\nApellido: ' + self.getApellido() + '\nEdad: ' + str(self.getEdad())





# apellido = input('Digita apellido: ')
# edad = int(input('Digita edad: '))
persona1 = Persona()
persona2 = Estudiante()
print(persona1.imprimirPersona())
print(persona2.imprimirPersonaOtraVez())
#print(persona1.setNombre(),persona1.getApellido(),persona1.getEdad())

