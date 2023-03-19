def exer_one(num1, num2):
  

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        true_result = num1 // num2
        remainder = num1 % num2
        print(f"The result is {true_result} with the reminder of {remainder}")

    except ZeroDivisionError:
        print("Division with 0 does not work, please insert a true number")

    except ValueError:
        print("Enter numbers only, not letters or other characters")


#exer_one(5,0)


def exer_two(number):

    try:
        number = int(input("Enter the number: "))
        print(pow(number, 2))

    except ValueError:
        print("Enter numbers only, not letters or other characters")
    
#exer_two(5)


#def exer_three():