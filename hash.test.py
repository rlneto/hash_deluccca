from hash import *
from random import randint

minhaHash = HashTable(100)

for _ in range(100):
    minhaHash.inserirElem(Elemento(randint(0,100), str(randint(0,100))))

minhaHash.printar()
