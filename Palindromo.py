def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False



def main():
    palabra = input('Escribe una palabra: ')
    if es_palindromo(palabra):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    main()