my_number = int(input("Enter your number: "))
final_no = str(my_number)
conversion = final_no[-1]



if len(str(my_number)) < 3 or len(str(my_number)) > 3 or my_number < 0:
    print("Eroare")

elif int(conversion) >= 5:
    print(my_number + int(conversion))
else:
    print(my_number - int(conversion))

