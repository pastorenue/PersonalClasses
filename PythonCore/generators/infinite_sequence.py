"""Defining a infinite sequence generator"""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# for i in infinite_sequence():
#     print(i, end=" ")   

"""Using next() on the generator object directly"""

# gen = infinite_sequence()
# for i in range(1000):
#     print(next(gen), end=" ")