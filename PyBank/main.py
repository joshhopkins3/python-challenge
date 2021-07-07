# Your task is to create a Python script that analyzes the records to calculate each of the following:
# # Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
budget_csv = Path("/Users/joshhopkins/Desktop/untitled folder/python-challenge/PyBank/Resources/budget_data.csv")

line_num = 0
profitloss = []
profitloss_dates = []
profitloss_sum = 0
max_pl = 0
min_pl = 0
sum = 0

with open(budget_csv, 'r') as csvfile:
    
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    
    header = next(csv_reader)
    
    for row in csv_reader:
        # print(row)
        line_num += 1
        profitloss.append(int(row[1]))
        profitloss_sum += int(row[1])
        profitloss_dates.append(row[0])
        

profitloss_change = []

for i in range(1, len(profitloss)):
    x = profitloss[i] - profitloss[i - 1]
    profitloss_change.append(int(x))
    

for i in range(0, len(profitloss_change)):
    sum += profitloss_change[i]
    average_change_profitloss = round((sum / (len(profitloss_change))), 2)


for profloss in profitloss:
    
    if min_pl == 0:
        max_pl == profloss
        min_pl == profloss
    if profloss > max_pl:
        max_pl = profloss
    elif profloss < min_pl:
        min_pl = profloss
        

max_pl_index = profitloss.index(max_pl)
min_pl_index = profitloss.index(min_pl)

max_pl_date = profitloss_dates[max_pl_index]
min_pl_date = profitloss_dates[min_pl_index]


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {line_num} \n"
    f"Total: ${profitloss_sum}\n"
    f"Average Change: ${average_change_profitloss}\n"
    f"Greatest Increase in Profits: {max_pl_date} (${max_pl}) \n"
    f"Greatest Decrease in Profits: {min_pl_date} (${min_pl}) \n"
)

print (output)