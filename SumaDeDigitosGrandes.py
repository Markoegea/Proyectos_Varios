def run(numero,cifras):
    con = 0
    sum=0
    while con < cifras:
        sum+=int(numero[con])
        con+=1
    print(sum)
if __name__ == '__main__':
    numeroB = input("Dame la base :\n")
    numeroE = input("Dame el exponente :\n")
    numero1 = int(numeroB) ** int(numeroE)
    print(len(str(numero1)))
    numero2 = input("Dame el numero 2 :\n")
    resta = int(numero1) - int(numero2)
    cifras = len(str(resta))
    run(str(resta),cifras)