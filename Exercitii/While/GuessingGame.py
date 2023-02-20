from random import randint

print("Start")

rand_number = randint(1, 99)

guess = int(input("Mai incearca: "))

while guess != rand_number:
    if guess < rand_number:
        print("+","\n","Try again")
        guess = int(input("Mai incearca: "))
    elif guess > rand_number:
        print("-","\n", "Try again")
        guess = int(input("Mai incearca: "))

    else:
        print("Felicitari")