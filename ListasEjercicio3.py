def run():
    meses_del_ano=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    mes=input('Digite mes numero (1-12) o nombre, en minisculas:')
    try:
        mes = int(mes)
        if mes >=1 and mes <=12:
            print(f'El mes de {meses_del_ano[mes-1]} tiene {dias[mes-1]} dias')
    except:
        mes = str(mes)
        for i in range(0, len(meses_del_ano)):
            if mes == meses_del_ano[i]:
                print(f'El mes de {meses_del_ano[i]} tiene {dias[i]} dias')


if __name__ == '__main__':
    run()