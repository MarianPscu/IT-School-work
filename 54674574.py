my_dict = {'banana': 3, 'apple': 2, 'orange': 1}

# sort the dictionary by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# print the sorted dictionary
for key, value in sorted_dict.items():
    print(key, value)