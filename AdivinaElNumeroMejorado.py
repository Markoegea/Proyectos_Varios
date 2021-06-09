import random

ejecutar = True
lista_de_jugadores = {}

def listaArchivo():
    try:
        d = open('ResultadoJuego.txt','r', encoding='utf-8')
        l =  int(len(d.readlines())/2)
        d.seek(0)
        for i in range(l):
            lista_de_jugadores.update({d.readline().strip('\n') : d.readline().strip('\n')}) 
            d.close
        print(f'''
            Lista de Jugadores''')
        for i,s in lista_de_jugadores.items():
            print(f'''
            {i} : {s}
            ''')
    except:
        f = open('ResultadoJuego.txt','x', encoding='utf-8')
        f.close
    jugandoAndo()

def jugandoAndo():
    numaleatorio = numero_aleatorio()
    vida = 5
    numero_elegido = int(input('Elige un numero entre el 1 al 100: '))
    while numero_elegido != numaleatorio:
        if vida == 0:
            print("GAME OVER")
            break
        if numero_elegido > numaleatorio:
            print('MAS PEQUEÑO')
        else:
            print('MAS GRANDE')
        vida-=1
        numero_elegido = int(input('Escoge otro numero: '))
    if numero_elegido == numaleatorio:
        print(f'GANASTE')
    nombre_del_jugador = str(input('Cual es tu nombre jugador? '))
    if vida == 0:
        intentos = 'No lo consiguo en ningun'
    else:
        intentos = str((5 - vida) + 1)
    meterloArchivo(nombre_del_jugador, intentos)

def meterloArchivo(nombre_del_jugador, intentos):
    lista_de_jugadores[nombre_del_jugador] = f'En {intentos} intentos'
    f = open('ResultadoJuego.txt','w', encoding='utf-8')
    for i,s in lista_de_jugadores.items():
        f.write(f'{i}\n{s}\n')
    f.close

def numero_aleatorio():
    numero_aleatorio = random.randint(1,100)
    ayudas(numero_aleatorio)
    return numero_aleatorio

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
    Result = 0
    for i in range(0,cifra_numero):
        Result += int(letra_entero[i])
    return Result

def multiplicar_cifras(letra_entero,cifra_numero):
    Result = 1
    for i in range(0,cifra_numero):
        Result *= int(letra_entero[i])
    return Result

if __name__ == '__main__':
    #while(ejecutar):
    listaArchivo()