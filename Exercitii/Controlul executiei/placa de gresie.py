# De ce nu iese

a = 21
initial = a
b = 6


while b:
    b = a % b
    a = b
    

print(a)


#Dar in schimb iese

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage

print(gcd(21, 6))


#De ce nu functioneaza salvarea pe linii diferite a variabilelor

