cont = 10
numerosmenores = 0
numerosmayores = 0

for i in range (0,10):
    nota = float(input(f"Cual es la nota del estudiante numero {cont}: "))
    if nota>=0 and nota<7:
        numerosmenores+=1
    elif nota>=7 and nota<=10:
        numerosmayores+=1
    else:
        print("Hay algo mal, intentalo otra vez")
        while nota<0 or nota>10:
            nota = float(input(f"Cual es la nota del estudiante numero {cont}, otra vez: "))
            if nota>=0 and nota<=7:
                numerosmenores+=1
            elif nota>=7 and nota<=10:
                numerosmayores+=1
    cont-=1

print(f"Hay {numerosmayores} numero mayores a 7")
print(f"Hay {numerosmenores} numero menores a 7")