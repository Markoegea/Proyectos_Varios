import random
Ejecutar = True
def generar_contrasena():
    global Ejecutar
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '$', '&']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    contrasenas = random.choice(mayusculas)+random.choice(minusculas)+random.choice(simbolos)+random.choice(numeros)
    print(contrasenas)
    if contrasenas == "Hi$9":
        Ejecutar = False

     
if __name__ == "__main__":
    while (Ejecutar):
       generar_contrasena()

    
