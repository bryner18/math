def main():
    first_20_sum()


def first_20_sum():
    print("This is the sum of the first 20 multiples of the number 3: ")
    a = 0
    b = 0
    c = 0
    while b < 20:
        a = a + 1
        if a % 3 == 0:
            b = b + 1
            c = c + a
    print("[", c, "]")


main()
