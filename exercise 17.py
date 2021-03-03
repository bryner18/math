# 17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.


def main():
    main_equation()


def main_equation():
    b = 0
    c = 0
    d = 1
    print("Type as many numbers you like, to stop just enter 0.")
    while d > 0:
        a = int(input("Type: "))
        if a % 10 == 5:
            b = b + a
            c = c + 1
        if a == 0:
            d = d - 1
            print("The average of the numbers you typed is [", b // c, "]")
            break


main()





