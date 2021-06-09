class clase:
  z = 20
  def my_func(z):
    respuesta = 0
    for i in range(2000):
        respuesta += 1
        print(f'{respuesta}')
        return respuesta
