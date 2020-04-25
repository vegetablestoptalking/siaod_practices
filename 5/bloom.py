import math
import random


def hfunc(text, seed=0):
    """
    Хэш-функция one_at_a_time (Jenkins)
    """
    h = 0
    for c in text:
        h += ord(c) + seed
        h += h << 10
        h ^= h >> 6
    h += h << 3
    h ^= h >> 11
    h += h << 15
    return h & 0xffffffff


class Filter1:
    def __init__(self):
        self.bits = 0x00000000
        

    def add(self, text):
        self.bits |= hfunc(text)

    def contains(self, text):
        hash_code = hfunc(text)
        return hash_code&self.bits == hash_code

class Filter2:
    def __init__(self, bits_per_hash):
        self.arr = []
        self.size_hash = bits_per_hash
        
    def add(self, text):
        self.arr.append(hfunc(text)&(2**self.size_hash-1))

    def contains(self, text):
        return hfunc(text)&(2**self.size_hash-1) in self.arr
           


class Filter3:
    def __init__(self, size):
        self.arr = [0]*size
        self.size = size

    def add(self, text):
        self.arr[hfunc(text)%self.size] = 1

    def contains(self, text):
        return self.arr[hfunc(text)%self.size] == 1


class Filter4:
    def __init__(self, size, nfuncs):
        self.size = size
        self.arr = [0]*self.size
        self.nfuncs = nfuncs
        

    def add(self, text):
        for i in range(self.nfuncs):
            self.arr[hfunc(text, i)%self.size] = 1
            

    def contains(self, text):
        for i in range(self.nfuncs):
            if self.arr[hfunc(text, i)%self.size] != 1:
                return False
        return True


def shuffle(text):
    lst = list(text)
    random.shuffle(lst)
    return "".join(lst)


def test(flt):
    print(type(flt).__name__)
    for e in EMAILS:
        flt.add(e)
    fp = 0
    for e in EMAILS:
        if not flt.contains(e):
            print("Получен ложноотрицательный результат!")
    for e in FALSE_EMAILS:
        if flt.contains(e) and e not in EMAILS:
            fp += 1
    print("Ложноположительных срабатываний: %.1f%%" % (100 * fp / len(EMAILS)))


def test_hfunc(data):
    hashes = [hfunc(x) % len(data) for x in data]
    return len(set(hashes))


random.seed(42)

with open("emails.txt") as f:
    EMAILS = f.read().split("\n")[:10000]
FALSE_EMAILS = [shuffle(e) for e in EMAILS]

#test(Filter1())
#test(Filter2(10))
#test(Filter3(1000))
test(Filter4(100000,5))
