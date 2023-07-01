from interface import CLIMenu
from complaint import Complaint
import pickle
from pathlib import Path



menu = CLIMenu("Complaint booklet", {

    "Adauga plangere": lambda : print("Adauga Plangere"),
    "Rezolva plangere": lambda : print("Rezolva Plangere"),
    "Vezi plangeri nerezolvate": lambda : print("Vezi Plangere"),

})

#menu.show_main()


c1 = Complaint("Am o problema", "Random text here")
c2 = Complaint("Am o problema", "Random text here")
c3 = Complaint("Am o problema", "Random text here")
c4 = Complaint("Am o problema", "Random text here")

l1 = [c1, c2, c3, c4]

for i in l1:
    print(i.id)


