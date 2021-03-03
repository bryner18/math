# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

import sys


def main():
    numbers_between()
    try_again()


def numbers_between():
    a = int(input("Insert a three digits number: "))
    if 99 < a <= 999:
        n = 0
        while n < a:
            n = n + 1
            print("[", n, "]")
    else:
        print("Your number isn't three digits long")


def try_again():
    again = input("Would you like to try again? ")
    if again == "y" or again == "Y" or again == "yes" or again == "Yes":
        return main()
    else:
        sys.exit()


main()
