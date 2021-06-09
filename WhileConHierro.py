menu = '''Dime el numero de las piezas del lote, que tienes
'''
contador = 1
numero = 0
if __name__ == '__main__':
    piezas = int(input(menu))
    while contador <= piezas:
        longitud = float(input(f'Dime la longitud de la pieza numero {contador}: '))
        if longitud >= 1.20 and longitud <= 1.30:
            numero+=1
        else:
            pass
        contador+=1
    print(f'Solo hay {numero} piezas aptas')
