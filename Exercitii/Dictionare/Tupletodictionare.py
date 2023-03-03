tuple_list = [("Dorin", 25), ("George", 24), ("Sorin", 19), ("Gigi", 55)]
empty_dict = {}

list_oflists = []

for tuple_item in tuple_list:
    list_oflists.append(list(tuple_item))


for list_item in list_oflists:
    empty_dict.update({list_item[0]: list_item[1]})


print(empty_dict)