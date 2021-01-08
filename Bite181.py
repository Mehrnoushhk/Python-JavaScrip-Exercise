# Complete the add method of the OrderedList class which takes a num argument
# and adds that to the self._numbers list keeping it ordered upon insert.
#
# Using a manual .sort() or .sorted() each time is not allowed.
# Look into the bisect module how to do it

import bisect


class OrderedList:
    def __init__(self):
        self._numbers = []

    def add(self, num):
        bisect.insort_left(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)