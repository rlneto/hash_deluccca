def primo(n):
    if n % 2 == 0:
        n += 1
    while True:
        for i in range(3, n, 2):
            if n % i == 0:
                break
        else:
            return n
        n += 2


def hash(chave, tamanho: int) -> int:
    if type(chave) == type(str()):
        return sum([ord(x) for x in chave]) % tamanho
    else:
        return int(chave) % tamanho
    

        
class Elemento:
    def __init__(self, valor: int, chave: str):
        self.__valor = valor
        self.__chave = chave
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor
    
    @property
    def chave(self):
        return self.__chave
    
    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, novo):
        self.__proximo = novo

class HashTable:
    def __init__(self, tamanho):
        self.__tamanho = primo(tamanho)
        self.__conteudo = [ list() for _ in range(self.__tamanho)]

    @property
    def conteudo(self):
        return self.__conteudo
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, novo):
        self.__tamanho = novo
    
    def inserirElem(self, elem):
        pos = hash(elem.valor, self.__tamanho)
        self.__conteudo[pos] = elem
        
    def printar(self):
        for bucket in self.conteudo:
            for elemento in bucket:
                print(self.conteudo.index(bucket), elemento)



def reHash(hash: HashTable) -> HashTable:
    return hash


hash_do_rudolf = HashTable(20)

print(len(hash_do_rudolf.conteudo), hash_do_rudolf.conteudo)
