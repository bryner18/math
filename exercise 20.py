# 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.


def main():
    factorial()


def factorial():
    a = int(input("Insert a number: "))
    if a > 0:
        b = 1
        for x in range(1, a + 1):
            b = b * x
        print("The factorial of [", a, "] is [", b, "]")
    elif a == 0:
        print("The factorial of 0 is 1")
    else:
        print("No factorials for negative numbers")
    exit()


main()
