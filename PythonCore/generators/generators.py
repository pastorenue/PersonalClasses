import os
import sys

"""
This function opens a given file and uses file.read() 
along with .split() to add each line as a separate element to a list
"""
# def csv_reader1(filename):
#     file = open(filename)
#     result = file.read().split('\n')
#     return result
# csv_gen = csv_reader2("files/techcrunch.csv")
# count = 0
# for row in csv_gen:
#     count += 1


"""This function uses a generator"""
# def csv_reader2(filename):
#     for row in open(filename, 'r'):
#         yield row
# Call the file reader function
# csv_gen = csv_reader2("files/techcrunch.csv")
# count = 0
# for row in csv_gen:
#     count += 1

"""
You can also use a generation comprehension to create a generator 
without necessarily creating a function
"""
csv_gen = (row for row in open(os.path.join(sys.path[0],"files/techcrunch.csv")))
for row in csv_gen:
    print(row)

    

