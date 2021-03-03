def main():
    total_sum()


def total_sum():
    n1 = int(input("Please insert a number: "))
    n2 = 0
    n3 = 0
    print("All the numbers between 1 and the number you typed are: ")
    while n2 != n1:
        n2 = n2 + 1
        print("[", n2, "]")
        n3 = n2 + n3
    print("The total sum of all the digits is: [", n3, "]")


main()
