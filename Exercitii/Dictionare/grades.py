register = [{"nume": "Adrian", "note": [5,6,7]}, {"nume": "Caramian", "note": [2,9,5]}, {"nume": "Georgica", "note": [8,9,9]}, 
           {"nume": "Svoboda", "note": [4,9,9]}, {"nume": "Cerasel", "note": [4,4,10]}]

final_grades = []

for student in register:
    average = sum(student["note"]) / 3

    student.update(({"media": average}))

    #final_grades.append(sum(student["note"]) / 3)

sorted_grades = sorted(register, key = lambda x: x["media"])
    
for student in sorted_grades:
    print(student["nume"], student["media"])