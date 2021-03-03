# 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar


def main():
    mult_table()


def mult_table():
    a = int(input("Insert your number: "))
    print("Multiplication table for [", a, "]")
    print(
        "[", a, "] x 1 is [", a * 1, "]""\n"
        "[", a, "] x 2 is [", a * 2, "]""\n"
        "[", a, "] x 3 is [", a * 3, "]""\n"
        "[", a, "] x 4 is [", a * 4, "]""\n"
        "[", a, "] x 5 is [", a * 5, "]""\n"
        "[", a, "] x 6 is [", a * 6, "]""\n"
        "[", a, "] x 7 is [", a * 7, "]""\n"
        "[", a, "] x 8 is [", a * 8, "]""\n"
        "[", a, "] x 9 is [", a * 9, "]""\n"
        "[", a, "] x 10 is [", a * 10, "]"
        )


main()
