import sys
import is_palindrome
import infinite_sequence

"""
This is is to compare performance of a normal lists comprehension and 
generator comprehension in terms of memory.
"""

def get_compute_size(iterator):
    return sys.getsizeof(iterator)

# Declare the list comprehension
num_squared_lc = [i**2 for i in range(10000)]
num_squared_gc = (i**2 for i in range(10000))

# Check for the size of a list
list_size = get_compute_size(num_squared_lc)
gen_size = get_compute_size(num_squared_gc)

#print them
print("List memory size: ",list_size)
print("Generator memory size: ", gen_size)

# However, the performance in terms if speed, list comprehension does better
import cProfile

# For List comprehension
print("*******************List Comprehension********************")
print(cProfile.run('sum([i**2 for i in range(10000)])'))

# For Generators
print("*******************Generator Comprehension********************")
print(cProfile.run('sum((i**2 for i in range(10000)))'))

