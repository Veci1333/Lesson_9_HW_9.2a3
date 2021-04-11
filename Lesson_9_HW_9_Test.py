# Fizz Buzz & Make String Lowercase

zahl = int(input("Geben Sie bitte eine Zahl zw. 1 und 100 ein: "))

while zahl > 0:

    if zahl % zahl == 0 and zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 5 == 0:
        print("Buzz")
    elif zahl % 3 == 0:
        print("Fizz")
    else:
        print(zahl)

    zahl = zahl - 1

    # Abfrage, ob nochmal gespielt werden möchte

    if zahl <= 0:
        abfrage = input("Wollen Sie nochmal? JA oder NEIN eingeben: ")
        abfrage = abfrage.upper()
        print(abfrage)

        if abfrage == "JA":
            zahl = int(input("Bitte neue Zahl eingeben: "))

        elif abfrage != "JA" and abfrage != "NEIN":
            print("Bitte Ja oder Nein eingeben")

        elif abfrage == "NEIN":
            print("Ihre Antwort ist " + abfrage + " Vielen Dank")
