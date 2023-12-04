import numpy as np
import sys

duza_lista = [i for i in range(1,10000000)]
duzy_slownik = {str(i): i for i in range(1, 1000000)}
duza_tablica = np.arange(1, 1000000)
generator = (x for x in range(1000000))

def display_size(x):
    return sys.getsizeof(x)
    

print("duza liczba w bajtach: " + str(display_size(duza_lista)))
print("duzy slownik w bajtach: " + str(display_size(duzy_slownik)))
print("duza tablica w bajtach: " + str(display_size(duza_tablica)))
print("generator w bajtach: " + str(display_size(generator )))

print("duza liczba w gigabajtach: " + str((display_size(duza_lista)/1024**3)))
print("duzy slownik w gigabajtach: " + str(display_size(duzy_slownik)/1024**3))
print("duza tablica w gigabajtach: " + str(display_size(duza_tablica)/1024**3))
print("generator w gigabajtach: " + str(display_size(generator )/1024**3))