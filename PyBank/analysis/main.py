import os as os
import csv
from pathlib import Path
from statistics import mean

filepath = (r"C:\Users\eriks\Desktop\Class Folder\Challenge_3\python-challenge\PyBank\Resources\budget_data.csv")

with open(filepath) as budget_csv:
    
    budget = csv.reader(budget_csv, delimiter=',')

# set variables

    months = 0
    total = 0
    change = 0
    prev_change = 0
    difference_ls = []
    difference =0
    maxmin = {}
    keys = []
    values = []

    header = next(budget)

    for row in budget:

# count number of months(rows)
        months = (months +1)

# count total of column 2
        total += int(row[1])


# find the change per month of P/L: find difference between current and previous row, 
# then keep track of that number and add it to a list
        change = int(row[1])
        difference =(change - prev_change)
        prev_change = change
        difference_ls.append(difference)

        # gather keys for the dictionary we'll make
        keys.append(row[0])

# remove first value since it's not a difference
difference_ls.pop(0)
# same for what will be the date keys of our dictionary
keys.pop(0)

# gather values for dictionary
for i in difference_ls:
    values.append(i)

# combine to create dictionary
maxmin = dict(zip(keys, values))

# find highest and lowest values and associated keys
max_value = max(maxmin, key=maxmin.get), max(maxmin.values())
min_value = min(maxmin, key=maxmin.get), min(maxmin.values())

# change the total to a dollar value
total_curr = "${:,.2f}".format(total) 

# print analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months:", months)
print("Total:", total_curr)

# use function to find the average difference
print("Average Change:","${:,.2f}".format(mean(difference_ls)))
print("Greatest Increase in Profits:", max_value)
print("Greatest Decrease in Profits:", min_value)


with open(r"C:\Users\eriks\Desktop\Class Folder\Challenge_3\python-challenge\PyBank\analysis\Analysis.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print("Total Months:", months, file=f)
    print("Total:", total_curr, file=f)
    print("Average Change:","${:,.2f}".format(mean(difference_ls)), file=f)
    print("Greatest Increase in Profits:", max_value, file=f)
    print("Greatest Decrease in Profits:", min_value, file=f)