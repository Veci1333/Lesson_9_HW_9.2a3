# Fizz Buzz & Make String Lowercase

zahl = int(input("Geben Sie bitte eine Zahl zw. 1 und 100 ein: "))

while zahl > 0:

    if zahl % zahl == 0 and zahl % 3 == 0 and zahl % 5 == 0:
        print ("FizzBuzz")
    elif zahl % 5 == 0:
        print("Buzz")
    elif zahl % 3 == 0:
        print("Fizz")
    else:
        print(zahl)

    zahl = zahl - 1
