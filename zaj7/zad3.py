import os
import sys

kat_do_spr = "D:\\Users\\UL0255407\\hunger_games\\zaj7\\toolss"

exist = os.path.exists(kat_do_spr)
if(exist):
    print(exist)
else:
    print("nie istnieje")