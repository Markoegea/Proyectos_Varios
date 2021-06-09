import random
ejecutar = True
class RobotColoso:
 def __init__(self, x,y):
    self.x = x
    self.y = y

 def movimiento_adelante(self):
    self.x = self.x + 5
    if self.x >= 100:
        print("No doy mas")
    else:
     print(f'Moviendose hacia adelante')
     print(f'{self.x,self.y}')

 def zero_movement(self):
    print("Devolviendose hacia ")
    self.x = 0
    self.y = 0
    print(f'{self.x,self.y}')


def main():
    global ejecutar
    direccion = input('Hacia donde vas?')
    try: 
        int(direccion)
        eleccion = int(direccion)
    except:
         eleccion = direccion

    if eleccion == 'B':
       robot.movimiento_adelante()

    elif eleccion == 'S':
        ejecutar = False

    elif eleccion == 'D':
        robot.zero_movement()
    
    else:
        print("Opcion Incorrecta")

if __name__ == '__main__':
    robot = RobotColoso(0,0)
    while(ejecutar):
     main()