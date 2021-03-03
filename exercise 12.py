# 12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.


def main():
    three_digits_one()


def three_digits_one():
    n1 = int(input("Insert a number: "))
    if 99 < n1 <= 999:
        d1 = n1 // 100
        d2 = (n1 % 100) // 10
        d3 = (n1 % 100) % 10
        if d1 == 1:
            print("Your first digit [", d1, "] is the number 1.")
        else:
            print("Your first digit [", d1, "] isnt the number 1.")
        if d2 == 1:
            print("Your second digit [", d2, "] is the number 1.")
        else:
            print("Your first digit [", d2, "] isn't the number 1.")
        if d3 == 1:
            print("Your third digit [", d3, "] is the number 1.")
        else:
            print("Your first digit [", d3, "] isn't the number 1.")


main()
