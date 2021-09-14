def run(num):
    cont = 1
    sum = 0
    while cont <= 2004:
        sum += int(num * cont)
        cont += 1
    print(sum)
    print(len(str(sum)))

if __name__ == '__main__':
    num = input("Dame el numero:\n")
    run(num)