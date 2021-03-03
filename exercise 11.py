def main():
    numbers_between_digits()


def numbers_between_digits():
    n1 = int(input("Please insert a number: "))
    if 9 < n1 <= 99:
        d1 = n1 // 10
        d2 = n1 % 10
        print("The numbers between the two digits of your number are: ")
        if d1 > d2:
            for x in range(d2, d1):
                print("[", x, "]")
        if d1 < d2:
            for x in range(d1, d2):
                print("[", x, "]")
    else:
        print("Your number is not two digits long")


main()

