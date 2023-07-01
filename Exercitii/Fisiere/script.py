from pathlib import Path


the_path = Path("inputdata.txt")

absolute = the_path.resolve()

my_file = open(the_path / "inputdata.txt", "w")
my_file.close()

with open(the_path / "inputdata.txt", "w") as fout:
    fout.write(input("Type your name: "))






# file1 = open(script_path / "test.txt", "w")
# file1.close()

# #context manager - closes the file automatically fout = file descriptor

# with open(file1 / "test.txt", "w") as fout:
#     fout.write("test string! Hello world")
#     pass