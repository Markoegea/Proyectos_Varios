def mover(n, origen, destino, auxiliar):
   if n > 0:
     mover(n-1, origen,auxiliar, destino)
     destino.append(origen.pop())
     mover(n-1,auxiliar, destino, origen)

if __name__ == '__main__':
    n = int(input('cuanto es?'))
    A = (n,0,-1)
    B = []
    C= []
    print(A,B,C)
    mover(n,A,C,B)
    print(A,B,C)