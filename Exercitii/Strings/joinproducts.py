product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf"
    "weee"
]

new_list = []

for word in product_code_list:
    word = word + "►"
    new_list.append(word)
    

print(new_list)

fused = "".join(new_list)


print(fused)