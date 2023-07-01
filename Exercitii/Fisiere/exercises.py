#absolut = C:\Users\Marian\Desktop\Python work\Exercitii\Object Oriented programming

#relativ = Exercitii\Object Oriented programming

from pathlib import Path

working_dir = Path(".")

print(working_dir)

print(working_dir.absolute())

print(__file__)

print(f"Current working directory: {working_dir.absolute()}")
script_path = Path(__file__)

print(f"Script path: {__file__}")

print(f"Script path: {script_path}")

print(f"Script parent directory {script_path.parent.parent}")

# test if file exists

print(f"{script_path} exists? {script_path.exists()}")


# getting the time/date for running my script

start_time_path = script_path.parent / "program_data/start_time.txt" # asta iti adauga fisierul nou/folder

print(start_time_path)

if not start_time_path.parent.exists():
    start_time_path.parent.mkdir()
    #mkdir = make directory - iti face directory
    print(f"Created {start_time_path.parent}")

# to avoid the error when we have 2 folders, pun parents true ca sa imi faca directory ul de care am nevoie ca sa fac un star time, atunci cand nu ex program data
start_time_path.parent.mkdir(exist_ok = True, parents = True)

# check if path is a directory or file

print(start_time_path.is_dir())
print(start_time_path.is_file())

# w = scriere text
# r = citire text
# a = adaugare text
# wb = scriere binara
# rb = citire binara
# ab = adaugare binara


# open a file

file1 = open(script_path / "test.txt", "w")
file1.close()

#context manager - closes the file automatically fout = file descriptor

with open(file1 / "test.txt", "w") as fout:
    fout.write("test string! Hello world")
    pass

print("File operation done!")


#De facut un script care citeste numele de la tastatura si de facut un fisier in acelasi folder cu scriptul
#si in fisier sa apara inputul

#de scris un script care s aiba un generator - de apelat next de 100 de ori, ca sa extragem primele 100 nmere ale lui fibonacci
#si de facut fisiere de la 1 la 100 si in fiecare fisier punem priml nr din sirul lui fibonacci
# pe toate le punem in fisierul numit Fibonacci

# read - sa vedem cand a fost rulat ult data un fisier.