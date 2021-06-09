class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self._libros = []

    def consultar_nombre_biblioteca(self):
        return self.nombre

    def agregar_libro(self, libro):
        self._libros.append({libro.titulo,libro.autor,libro.genero,libro.cantidad_de_paginas,libro.sinopsis, })

    def consultar_libros(self):
        return self._libros

    def consultar_libro(self, id):
        return self._libros[id]

    def quitar_libro(self, id):
        self._libros.pop(id)

class Libro:
    def __init__(self, titulo, autor, cantidad_de_paginas, genero, sinopsis):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_de_paginas = cantidad_de_paginas
        self.genero = genero
        self.sinopsis = sinopsis
if __name__ == '__main__':
    ejecutar = True
    
    while(ejecutar):
        print("- - - B I B L I O T E C A S - - -")
        opcion = int(input("¿Qué vas a hacer?:\n1-Crear Biblioteca\n2-Agregar libro\n3-Ver catalogo\n4-Quitar Libro\n5-Salir\n:"))
        
        if opcion == 1:
            nombre = input("Nombre de la biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print("Se creo la biblioteca: {}".format(biblioteca.consultar_nombre_biblioteca))

        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            cantidad_de_paginas = input("Paginas: ")
            genero = input("Genero: ")
            sinopsis = input("Sinopsis: ")

            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
            biblioteca.agregar_libro(libro)
        
        elif opcion == 3:
            print("Catalogo de libros: ")
            print(f'{libro.titulo}, {libro.autor}, {libro.genero}, {libro.cantidad_de_paginas}, {libro.sinopsis} ')

        elif opcion == 4:
            indice = input("Id del libro a eliminar: ")
            biblioteca.quitar_libro(indice)

        elif opcion == 5:
            ejecutar = False

        else:
            print("Opcion incorrecta")
            
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon_()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
         print(f'Llenando el tanque con agua {temperatura}')
    def _anadir_jabon_(self):
         print('Anadiendo jabon')

    def _lavar(self):
         print('Lavando la ropa')
    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()



