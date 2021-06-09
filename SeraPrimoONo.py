def primera_opcion(numero):
    contador = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            contador += 1
        if numero == i:
            if contador == 2:
                return print('Es primo')
    return print('No es primo')

def segunda_opcion(numero):
  contador = 0
  for num in range(numero):
    if numero % (num+1) != 0:
      continue
    else:
      contador +=1
  if contador == 2:
    print('El número es primo')
  else:
    print('el número no es primo')  

def tercera_opcion(numero):
    if numero == 1:
        print('No es primo')
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return print('No es primo')           
        return print("Es primo")       



if __name__ == '__main__':
    numero = int(input('Mandame un numero: '))
    primera_opcion(numero)