import os
import sys


file_name = "files/techcrunch.csv"
lines = (line for line in open(os.path.join(sys.path[0],file_name)))

# split each line into a list
list_lines = (s.rstrip().split(",") for s in lines)

# We need the column names which is always line 1
cols = next(list_lines)

# let's convert the data into a dictionary where the keys are the column names 
company_dicts = (dict(zip(cols, data)) for data in list_lines)

# lets create another generator to filter the funding round
funding = (
    int(company_dict['raisedAmt'])
    for company_dict in company_dicts
    if company_dict['round'] == 'a'    
    )

# get the sum of all seriesA funding
total_funding_a = sum(funding)
print("The total amount raised is ${}".format(total_funding_a))

#or
print(f"The total amount raised is ${total_funding_a}")
