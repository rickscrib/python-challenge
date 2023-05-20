import os as os
import csv
from pathlib import Path
from statistics import mean

filepath = (r"C:\Users\eriks\Desktop\Class Folder\Challenge_3\python-challenge\PyPoll\Resources\election_data.csv")

with open(filepath) as poll_csv:
    
    poll = csv.reader(poll_csv, delimiter=',')

    header = next(poll)

    count = 0
# create list of candidates and an iterator, and string variables to shorten code, along with counters for votes
    all_candidates = []
    candidates = ''
    candidates_prev = ''
    charles = "Charles Casper Stockham"
    ccount = 0
    diana = "Diana DeGette"
    dcount = 0
    raymon = "Raymon Anthony Doane"
    rcount = 0

# add to vote count
    for row in poll:
        count = (count + 1)
# generate list of candidates with unique values
        candidates = row[2]
        if candidates in all_candidates:
            pass
        else:
            all_candidates.append(candidates)

# assign votes to specific candidates

        if row[2] == charles:
            ccount = (ccount +1)
        elif row[2] == diana:
            dcount = (dcount + 1)
        else:
            rcount = (rcount +1)

# find each candidate's percentage of total votes, and
# format the percentages
cperc = ccount / count
cpercent = f"{cperc:.3%}"
dperc = dcount / count
dpercent = f"{dperc:.3%}"
rperc = rcount / count
rpercent = f"{rperc:.3%}"

# generate analysis

print("Election Results")
print("-------------------------")
print("Total Votes:", count)

# format list to display as plain text

candidatespl = ', '.join(str(item) for item in all_candidates)
print(f"The candidates who received votes are: {candidatespl}.")
print("-------------------------")
print(f"{charles}: {cpercent} ({ccount})")
print(f"{diana}: {dpercent} ({dcount})")
print(f"{raymon}: {rpercent} ({rcount})")

# find the candidate with the most votes and display

wincount = max(ccount, dcount, rcount)
if wincount == ccount:
    winner = charles
elif wincount == dcount:
    winner = diana
else:
    winner = raymon


print(f"The winner of this election is {winner}, with {wincount} votes.")

with open(r"C:\Users\eriks\Desktop\Class Folder\Challenge_3\python-challenge\PyPoll\analysis\Analysis.txt", "w") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes:", count, file=f)
    print(f"The candidates who received votes are: {candidatespl}.", file=f)
    print("-------------------------", file=f)
    print(f"{charles}: {cpercent} ({ccount})", file=f)
    print(f"{diana}: {dpercent} ({dcount})", file=f)
    print(f"{raymon}: {rpercent} ({rcount})", file=f)
    print(f"The winner of this election is {winner}, with {wincount} votes.", file=f)

