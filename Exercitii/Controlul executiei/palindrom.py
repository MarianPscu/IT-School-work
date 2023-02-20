#Method 1

n = 292

str_conversion = str(n)

int_process = int(str_conversion[::-1])

if n == int_process:
    print("Is Palindrome")

else:
    print("Is not palindrome")