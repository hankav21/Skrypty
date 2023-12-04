import os
import sys

root = "D:\\Users\\UL0255407\\hunger_games\\zaj7"

for dirpath, dirnames, filenames in os.walk(root):
    sum=0
    for filename in filenames:
        #print(os.path.join(dirpath, filename))
        sum+= sys.getsizeof(filename)
    print(str(dirpath) + ": ", str(sum))