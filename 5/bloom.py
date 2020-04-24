import math
import random


def hfunc(text, seed=0):
    """
    Хэш-функция one_at_a_time (Jenkins)
    """
    h = 0
    for c in text:
        h += ord(c)
        h += h << 10
        h ^= h >> 6
    h += h << 3
    h ^= h >> 11
    h += h << 15
    return h & 0xffffffff


class Filter1:
    def __init__(self):
        self.bits = 0x00000000
        
        pass

    def add(self, text):
        self.bits |= hfunc(text)
        self.bits

    def contains(self, text):
        # TODO
        pass


class Filter2:
    def __init__(self, bits_per_hash):
        # TODO
        pass

    def add(self, text):
        # TODO
        pass

    def contains(self, text):
        # TODO
        pass


class Filter3:
    def __init__(self, size):
        # TODO
        pass

    def add(self, text):
        # TODO
        pass

    def contains(self, text):
        # TODO
        pass


class Filter4:
    def __init__(self, size, nfuncs):
        # TODO
        pass

    def add(self, text):
        # TODO
        pass

    def contains(self, text):
        # TODO
        pass


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
    EMAILS = f.read().split("\n")[:100]
FALSE_EMAILS = [shuffle(e) for e in EMAILS]
