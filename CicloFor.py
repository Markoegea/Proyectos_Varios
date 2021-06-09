def run(frase):
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    frase = input('Escribe un frase: ')
    run(frase)
    # for i in range(501):
    #     f = open('./forMe'+'.txt', 'a', encoding='utf-8')
    #     f.write(str(i) +". "+"Marco" + '\n')
    #     print(i)
    #     f.close