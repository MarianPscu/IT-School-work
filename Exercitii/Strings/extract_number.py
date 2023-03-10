import_numbers = "Today we had 280 clients."

numbers = ["0","1","2","3","4","5","6","7","8","9"]

the_number =[]

for letter in import_numbers:
    if letter in numbers:
        the_number.append(letter)


completed_number = "".join(the_number)

print(completed_number)