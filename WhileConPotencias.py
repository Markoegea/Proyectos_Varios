
menu = """ Hola, deseas conocer las potencia de un numero, 
muy bien, escribe un numero: """  

def main(numero_potenciado):
    i = 1
    while(numero_potenciado < 1000):
        print(f"La potencia del {numero} a la {i} es {numero_potenciado}" )
        numero_potenciado = numero ** i
        i = i + 1



if __name__== '__main__':
    numero = int(input(menu))
    if numero == 1 or 0:
        print(f"No puedo potenciar el numero {numero}")
    else:
        main(numero)
        


   