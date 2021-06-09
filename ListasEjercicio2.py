import sys
frutas_precios={
    'fresa':3000,
    'manzana': 1500,
    'mango': 4000,
    'kiwi': 3000,
    'guayaba': 3000
}
def run():
    ejecutar = True
    global frutas_precios
    fruta_a_buscar = input("Cual fruta vendiste? ")
    while ejecutar:
        if fruta_a_buscar not in frutas_precios.keys():
            print("Hay un error, adios")
        else:
            for i in frutas_precios.keys():
                if i == fruta_a_buscar:
                    cantidad = int(input(f"Cuantas {fruta_a_buscar} vendiste? "))
                    print(f'Ganaste la moderada cantidad de {frutas_precios.get(i)*cantidad} pesos')
        fruta_a_buscar = input("Cual otra fruta vendiste? ")


if __name__ == '__main__':
    run()