import sys


def main():
    numbers_between()
    try_again()


def numbers_between():
    a = int(input("Insert a number: "))
    n = 0
    while n < a:
        n = n + 1
        if n % 2 == 0:
            print("[", n, "]")
    print("These are all the pairs between 1 and the number you typed!")


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()
