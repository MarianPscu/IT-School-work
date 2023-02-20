my_num = int(input("Select a number: "))

current_sum = 0

for i in range(3, my_num + 1):

    if i % 3 == 0 or i % 5 == 0:

        current_sum += i

print(current_sum)