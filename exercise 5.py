# 5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

import sys


def main():
    two_numbers()
    try_again()


def two_numbers():
    n1 = int(input("Insert your first number: "))
    n2 = int(input("Insert your second number: "))
    n3 = 0
    if n3 < n1:
        print("All the numbers ended on 4 for the first number are: ")
        while n3 < n1:
            n3 = n3 + 1
            if n3 % 10 == 4:
                print("[", n3, "]")

    n3 = 0
    if n3 < n2:
        print("All the numbers ended on 4 for the second number are: ")
        while n3 < n2:
            n3 = n3 + 1
            if n3 % 10 == 4:
                print("[", n3, "]")


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()
