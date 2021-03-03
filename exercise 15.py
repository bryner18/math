# 15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.


def main():
    first_20_sum()


def first_20_sum():
    print("This is the sum of the first 20 multiples of the number 3: ")
    n1 = 0
    n2 = 0
    while n1 < 20:
        n1 = n1 + 1
        if n1 % 3 == 0:
            n2 = n2 + n1
            print(n2)
    print("Sum: [", n2, "]")


main()
