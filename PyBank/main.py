# Your task is to create a Python script that analyzes the records to calculate each of the following:
# # Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path("/Users/joshhopkins/Desktop/python-challenge/PyBank/Resources/budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    budgetreader= csv.reader(csvfile, delimiter=",")

    header= next(budgetreader)
    total_months=0
    totals=0
    change=0
    prev=[]

#List the total number of months included in the dataset
    
    for row in budgetreader:

        total_months+=1
        totals+=int(row[1])
        
        

    print ("Financial Analysis")
    print ("-------------------------------")
    print ("Total Number of Months:", total_months)
    print ("Total: ", totals)
    print ("Average Change: $", )
    print ("Greatest Increase in Profits: ")
    print ("Greatest Decrease in Profits: ")