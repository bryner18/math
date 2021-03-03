# 14. Mostrar en pantalla los primeros 20 múltiplos de 3.


def main():
    first_20()


def first_20():
    print("These are the first 20 multiples of the number 3: ")
    n = 0
    while n < 20:
        n = n + 1
        if n % 3 == 0:
            print("[", n, "]", end=" ")


main()

