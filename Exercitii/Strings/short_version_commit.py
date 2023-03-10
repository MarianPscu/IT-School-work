commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300
    shuffle method"""


splitted = commit.split()



print(splitted[3] +" " + splitted[4] + " " + splitted[1][:11])