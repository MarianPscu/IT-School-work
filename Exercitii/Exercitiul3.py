number_a = int(input("Type the first number: "))
number_b = int(input("Type the second number: "))

if number_a > number_b:
    print(number_a - number_b)
elif number_a == number_b:
    print(number_a**number_b)
else:
    print(number_a+number_b)