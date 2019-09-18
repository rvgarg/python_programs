def is_even(n):
    return n % 2 == 0


f = lambda e: e % 2 == 0
n = [1, 2, 3, 4, 33, 5, 6, 45]
even = list(filter(f, n))
print(even)
double = list(map(lambda n: n * 2, even))
print(double)
from functools import reduce

su = reduce(lambda a, b: a + b, double)
print(su)
