import sys


def main():
    two_numbers()
    try_again()


def two_numbers():
    n1 = int(input("Insert a number: "))
    n2 = int(input("Insert another number: "))
    
    if n1 < n2:
        for x in range(n1, n2 + 1):
            print(x)
    if n1 > n2:
        for a in range(n1, n2, -1):
            print(a)


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()
