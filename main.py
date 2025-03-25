import random

number = random.randint(1, 100)
tebak = None

while tebak != number:
    tebak = int(input("Tebak angka dari 1 sampai 100: "))

    if tebak < number:
        print("Terlalu Rendah!")

    