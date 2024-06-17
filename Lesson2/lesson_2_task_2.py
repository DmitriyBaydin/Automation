year = int(input("Введите год: "))


def is_year_leap():
    if year % 4 == 0:
        print("год", year, ":", True)
    else:
        print("год", year, ":", False)


is_year_leap()
