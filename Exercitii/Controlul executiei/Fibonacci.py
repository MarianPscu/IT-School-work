my_num = int(input("Select a number: "))

current_line = 1
first = 0
second = 1

while current_line != my_num:

    
    star_no = first + second

    print("*" * star_no)

    first += 1
    second += 1
    current_line +=1

