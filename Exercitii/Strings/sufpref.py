string = "antilope, string, strokes, accident, boulder, attack, apple, vinegar, antiquity"

substrings = string.strip(" ")

for i in string:
    
    truth = i.startswith("a")
    if i[0] == truth:
        print(i)