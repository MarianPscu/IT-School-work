
def get_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    

for n in range(0, 50):
    if get_even(n) == False:
        print(n)


for n in range(0, 2000):
    if get_even(n) == False:
        print(n)