def main():
    equation()


def equation():
    x = int(input("Insert your first number: "))
    b = 0
    c = 0
    d = 0
    for x in range(x):
        while b < x:
            b = b + 1
            if b % 2 == 0:
                d = d + 1
                c = c + b
                # print(b)
    print("First average of the multiple of two: ", "[", c // d, "]")

    x1 = int(input("Insert your second number: "))
    b1 = 0
    c1 = 0
    d1 = 0
    for x in range(1, x1):
        while b1 < x:
            b1 = b1 + 1
            if b1 % 5 == 0:
                d1 = d1 + 1
                c1 = c1 + b1
                # print(b1)
    print("Second  average of the multiple of five: ", "[", c1 // d1, "]")

    if (c // d) > (c1 // d1):
        print("The first average is bigger than the second.")
    else:
        print(" \n---------------------------------------------\nThe second average is bigger than the first average.\n---------------------------------------------")


main()
