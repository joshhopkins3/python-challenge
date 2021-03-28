# Your task is to create a Python script that analyzes the records to calculate each of the following:
# # Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path("/Users/joshhopkins/Desktop/python-challenge/PyPoll/Resources/election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    electionreader= csv.reader(csvfile, delimiter=",")

    print(electionreader)

    total_votes=0
    
# Get the total number of votes cast
    
    for row in electionreader:
        total_votes+=1


print ("Election Results")
print ("-------------------------------")
print ("Total Votes:", total_votes)
print ("Khan: ")
print ("Correy: $")
print ("Li: ")
print ("O'Tooley:",)
print ("-------------------------------")
print("Winner:",)
print ("-------------------------------")