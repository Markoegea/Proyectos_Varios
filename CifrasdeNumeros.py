import math
menu = """ 
Buenas, quieres saber cuantas cifras tiene un numero?, 
averguemoslo juntos, dime el numero: """


def buenas_cifras(i):
    global numero
    if i==1:
        return print(f"El numero {numero} tiene {i} cifra")  
    else:
        return print(f"El numero {numero} tiene {i} cifras")             
        
if __name__ == '__main__':
    numero_entrar = float(input(menu))
    numero_piso = math.floor(numero_entrar)
    numero = str(numero_piso)
    buenas_cifras(len(numero))