lista = {"Gelu": 67, "Zoro": 55, "Batman": 25}
sorting = []

for name in lista.keys():
    sorting.append(name)

sorting.sort(reverse=True)

print(sorting)

finder = "Gelu"

if finder in lista:
    print(True)

else:
    print(False)