def main():
    multiple_between_5()


def multiple_between_5():
    n1 = int(input("Insert a number: "))
    n2 = 0
    print("These are all the multiple of 5 between 1 and the number you typed: ")
    while n2 < n1:
        n2 = n2 + 1
        if n2 % 5 == 0:
            print("[", n2, "]")


main()
