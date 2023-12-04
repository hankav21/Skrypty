import os

root = "D:\\Users\\UL0255407\\hunger_games\\zaj7"

for dirpath, dirnames, filenames in os.walk(root):
    print(dirnames)
    for filename in filenames:
        #print(os.path.join(dirpath, filename))
        print("\t" + str(filename))