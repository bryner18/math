def main():
    first_20()


def first_20():
    print("These are the first 20 multiples of the number 3: ")
    a = 0
    b = 0
    while b < 20:
        a = a + 1
        if a % 3 == 0:
            b = b + 1
            print(a)


main()

