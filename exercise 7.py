# 7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.


def main():
    one_to_hundred()


def one_to_hundred():
    print("This will print all numbers between 1 to 100")
    for x in range(1, 101):
        print("[", x, "]")


main()
