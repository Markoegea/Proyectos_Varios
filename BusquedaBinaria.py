

def busqueda_binaria(objetivo):     
 epsilon = 0.01
 bajo = 0.0
 alto = max(1.0, objetivo)
 respuesta = (alto + bajo) /2
 while abs(respuesta**2 - objetivo) >= epsilon:
  if respuesta**2 < objetivo:
       bajo = respuesta
  else: 
        alto = respuesta
  respuesta = (alto + bajo) / 2
 print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def suma(objetivo1, objetivo2):

    sumas = objetivo1 + objetivo2
     

eleccion = int(input('Elige: '))
if eleccion == 1:
  objetivo = int(input('Escoge un numero: '))
  busqueda_binaria(objetivo)
elif eleccion == 2:
   objetivo1 = int(input('Escoge un numero1: '))
   objetivo2 = int(input('Escoge otro numero: '))
   suma(objetivo1, objetivo2)

