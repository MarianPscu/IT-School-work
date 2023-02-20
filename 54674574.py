my_num = int(input("Select a number: "))

current_number = 1


for i in range(1, my_num):
    stars = i + (i - 1)
    print("*" * stars)