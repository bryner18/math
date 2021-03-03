# 18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.


def main():
    ten_to_one()


def ten_to_one():
    n = 0
    for x in range(10, 0, -1):
        n = n + 1
        print(n)


main()
