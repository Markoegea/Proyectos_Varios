class Rectangulo:
    def __init__(self, base, altura):
     self.base = base
     self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

     def __init__(self, lado):
      return super().__init__(lado, lado)

class Triangulo(Rectangulo):
    def __init__(self, base, altura):
     return super().__init__(base, altura)
    def area(self):
     return (self.base * self.altura) /2

if __name__ == '__main__':
    lado1 = int(input("Escribe el lado 1: "))
    lado2 = int(input("Escribe el lado 2: "))
    rectangulo = Rectangulo(base=lado1, altura=lado2)
    print(rectangulo.area())
    lado3 = int(input("Escribe el lado: "))
    cuadrado = Cuadrado(lado=lado3)
    print(cuadrado.area())  
    lado4 = int(input("Escribe el lado 1: "))
    lado5 = int(input("Escribe el lado 2: "))
    triangulo = Triangulo(base=lado4, altura=lado5)
    print(triangulo.area())

