students = {"Gabi": 6, "Gigi": 7, "Gica":8, "Doru": 9}

students.update(({"Cornel": 10}))

#print(students)

students["Gigi"] = 4

sorted_dict = sorted(students.keys())

for name in sorted_dict:
    print(name, students[name])