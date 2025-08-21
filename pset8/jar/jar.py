'''
1. __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
2. __str__ should return a str with🍪, whereis the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
3. deposit should add n cookies to the cookie jar.
4. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
5. withdraw should remove n cookies from the cookie jar. Nom nom nom.
6. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
7. capacity should return the cookie jar’s capacity.
8. size should return the number of cookies actually in the cookie jar, initially 0.
'''


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity should not be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if (n + self._size) > self._capacity:
            raise ValueError("Capacity Exceeded")
        self._size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Size Exceeded")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
