def main():
    ended_by_6()


def ended_by_6():
    for x in range(25, 205):
        if x % 10 == 6:
            print(x)


main()
