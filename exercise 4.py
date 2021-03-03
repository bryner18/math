# 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

import sys


def main():
    two_numbers()
    try_again()


def two_numbers():
    n1 = int(input("Insert a number: "))
    n2 = int(input("Insert another number: "))
    n3 = 0
    n4 = n1 - n2
    if n3 < n4:
        while n3 < n4:
            n3 = n3 + 1
            print(n3)
    if n3 > n4:
        while n3 > n4:
            n3 = n3 - 1
            print(abs(n3))


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()
