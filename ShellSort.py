lista_desordenada = []

def ordenar(n,k):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            num = k[i]
            while i >= intervalo and k[i-intervalo] > num:
                k[i] = k[i-intervalo]
                i -= intervalo
            k[i] = num
        intervalo //= 2
    return k

def ordenarInversa(n,k):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo,n ):
            num = k[i]
            while i >= intervalo and k[i-intervalo] < num:
                k[i] = k[i-intervalo]
                i -= intervalo
            k[i] = num
        intervalo //= 2
    return k

if __name__ == '__main__':
    lista_desordenada = input("Dame numeros: ").split(sep=',')
    for i in range(0,len(lista_desordenada)):
        lista_desordenada[i] = int(lista_desordenada[i])
    print(f' De menor a mayor {ordenar(len(lista_desordenada),lista_desordenada)}')
    print(f'De mayor a menor {ordenarInversa(len(lista_desordenada),lista_desordenada)}')

