# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
filepath = "Resources/election_data.csv"
file_to_output = "Analysis/election_data_yoshi.txt"

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
dictionary_vote = {}


# Open the CSV file and process it
with open(filepath) as csvfile:

#csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through each row of the dataset and process it
    for row in csvreader:
        total_votes += 1

    #total votes
        candidate = row[2]
        if candidate in dictionary_vote.keys():
            dictionary_vote[candidate] += 1 # add one to the value
        else:
            dictionary_vote[candidate] = 1


#output summary
print(dictionary_vote)
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
winner = ""
max_votes = 0

#dictionary loop
for candidate in dictionary_vote.keys():
        votes = dictionary_vote[candidate]
        vote_perc = round(100* votes / total_votes, 3)

        #winner find
        if votes > max_votes:
             max_votes = votes
             winner = candidate

        #create output
        Names = f"{candidate}: {vote_perc}% ({votes})\n"
        output += Names


#winner
winner_name = f"""
-------------------------
Winner: {winner}
-------------------------
"""
output += winner_name

#print the output
print(output)

#write output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)