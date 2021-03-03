# 3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

import sys


def main():
    exact_divider()
    try_again()


def exact_divider():
    a = int(input("Insert a number: "))
    n = 0
    while n < a:
        n = n + 1
        d = a % n
        if d == 0:
            print("[", n, "]")
    print("These are all the exact divisors between 1 and the number you typed!")


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()