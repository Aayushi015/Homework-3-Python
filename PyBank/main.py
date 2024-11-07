# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
file_to_output = "analysis/Budget_data_yoshi.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

last_months_profit = 0
curr_months_profit = 0
total_change = 0

max_change = 0
max_month = ""
min_month = ""
min_change = 0


#code ripped 3.2.8
with open(filepath) as csvfile:

#csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')

#read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

#read each row of tge data after the header
    for row in csvreader:
            #print(row)
            total_months += 1
            total_net += int(row[1])

            #check if first row
            if total_months == 1:
                  last_months_profit = int(row[1])
            else:
                  curr_months_profit = int(row[1])
                  change = curr_months_profit - last_months_profit
                  total_change += change

                  #reset
                  last_months_profit =curr_months_profit

                  #check max change
                  if change > max_change:
                        max_change = change
                        max_month = row[0]

                  #check min changes
                  if change < min_change:
                        min_change = change
                        min_month = row[0]


#generate the outpuy summery

output = f"""
Financial Analysis
----------------------------------
Total Months: {total_months}
Total Net: ${total_net}
ave_change = {round(total_change / (total_months - 1), 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""

#print the output
print(output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
