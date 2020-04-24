"""
Fib module.
"""
import timeit
import matplotlib.pyplot as plt


def fib(x: int) -> int:
    """Fib function.

    :param x: Argument of function.
    :type x: int
    :returns: Result of function.
    :rtype: int

    Examples.

        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(6)
        8
    """
    assert x >= 0
    if x < 2:
        return x
    return fib(x - 1) + fib(x - 2)


def magic(f):
    table = {}
    def g(x):
        if x in table.keys():
            return table[x]
        table[x] = f(x)
        return table[x]
    return f


def fast_fib(x): return x if x < 2 else fast_fib(x - 1) + fast_fib(x - 2)


fast_fib = magic(fast_fib)


def bench(funcs, x):
    return [timeit.timeit(lambda: f(x), number=100) for f in funcs]


if __name__ == "__main__":
    import doctest
    doctest.testmod()



plt.bar(['fib', 'fast_fib'], bench([fib, fast_fib], 16))
plt.show()

