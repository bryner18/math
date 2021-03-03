# 9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.


def main():
    ended_by_6()


def ended_by_6():
    for x in range(25, 205):
        if x % 10 == 6:
            print(x)


main()
