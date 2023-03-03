tuple_list = [("Dorin", 25), ("George", 24), ("Sorin", 19), ("Gigi", 55)]
empty_dict = {}

for tuple_item in tuple_list:
    for name, age in enumerate(tuple_item):
        empty_dict.update({"name": age})


print(empty_dict)