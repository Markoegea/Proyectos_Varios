def run():
    calificaciones = input("Dame numeros: ").split(sep=',')
    #calificaciones = [float(i) for i in calificaciones]
    for i in range(0, len(calificaciones)):
        while float(calificaciones[i]) > 10:
            calificaciones[i]=input(f"Ese no sirve {float(calificaciones[i])}, dame otro: ")
        calificaciones[i] = float(calificaciones[i])
    for i in calificaciones:
        print(i)
    print(f'El promedio es {sum(calificaciones)/len(calificaciones)}')
    calificaciones.sort()
    print(f'La nota mas grande es {calificaciones[0]}')
    calificaciones.sort(reverse=True)
    print(f'La nota mas pequeña es {calificaciones[0]}')




if __name__ == '__main__':
    run()