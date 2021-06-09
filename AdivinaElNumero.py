import random
def run():
    numero_aleatorio = random.randint(1, 999)
    ayudas(numero_aleatorio)
    numero_elegido = int(input('Elige un numero entre el 1 al 999: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido > numero_aleatorio:
            print('Es un numero mas pequeño')
        else:
            print('Es un numero mas grande')
        numero_elegido = int(input('Escoge otro numero: '))
    print(f'Ganaste, si era el {numero_aleatorio}')

def ayudas(numero_aleatorio):
    cifra_numero = len(str(numero_aleatorio))
    letra_entero = str(numero_aleatorio)
    if numero_aleatorio % 2 == 0:
        print('Ayuda 1: Es un numero par')
    else:
        print('Ayuda 1: Es un numero impar')
    if cifra_numero == 1:
        print('Ayuda 2: Es un numero de una cifra') 
    elif cifra_numero == 2:
        print(f'Ayudas 2: Es un numero de dos cifras, el producto de sus cifras es {multiplicar_cifras(letra_entero,cifra_numero)}')
    else: 
        print(f'Ayudas 2: Es un numero de tres cifras, y la suma de sus cifras es {suma_cifras(letra_entero,cifra_numero)}')

def suma_cifras(letra_entero,cifra_numero):
    #sumar las cifras de una numero una por una, es una lista, con append() se agrega elementos y con sum() se suman, mirar SumaLista.py
    Result = 0
    for i in range(0,cifra_numero):
        Result += int(letra_entero[i])
    return Result

def multiplicar_cifras(letra_entero,cifra_numero):
    #sumar las cifras de una numero una por una, es una lista, con append() se agrega elementos y con sum() se suman, mirar SumaLista.py
    Result = 1
    for i in range(0,cifra_numero):
        Result *= int(letra_entero[i])
    return Result

if __name__ == '__main__':
    run()