raza = int(input("Care e raza?: "))

perimetru = 2 * 3.14 * raza


print(f"Perimetrul cercului:{perimetru}")

if raza > 100:
    aria = 3.14 * raza **2
    print(f"Aria cercului: {aria}")

else:
    print("Aria = Not applicable")