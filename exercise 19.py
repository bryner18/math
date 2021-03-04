def main():
    mult_table()


def mult_table():
    a = int(input("Insert your number: "))
    print("Multiplication table for [", a, "]")
    for x in range(1, 11):
        print("[", a, "] x [", x, "] = ", a*x)


main()
