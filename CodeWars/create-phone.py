def create_phone_number(n):

    for numbers in n:
        if numbers > 9 or numbers < 0:
            raise ValueError("The integers is not in 0 a 9")

    paquet = ""

    for numbers in n[3:6]:
        paquet += str(numbers)

    paquet += "-"

    for numbers in n[6:]:
        paquet += str(numbers)

    return f"({n[0]}{n[1]}{n[2]}) {paquet}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
