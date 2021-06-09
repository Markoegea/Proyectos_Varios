class Coordenada:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        
        return(x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    #print(isinstance(3, Coordenada))
    
class Saludo:
    
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def Saluda(self, otro_Saludo):
      return f'Hola {otro_Saludo.nombre} de edad {otro_Saludo.edad} anos, me llamo {self.nombre} de edad, {self.edad} anos, como estas?'
    
  
if __name__ == '__main__':
      Saludo1 = Saludo('Marco', 16)
      Saludo2 = Saludo('Lucy', 2)
      print(Saludo2.Saluda(Saludo1))
