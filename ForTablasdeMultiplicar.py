menu = """Hola, 
dime que tabla de multiplicar deseas conocer: """

def tablas(numero_tabla):
    print(f"La tabla del numero {numero_tabla} es: ")
    for i in range(1,11):
        print(f"{numero_tabla} por {i} es {numero_tabla * i}")
        

if __name__ == "__main__":
   tablas(int(input(menu)))
