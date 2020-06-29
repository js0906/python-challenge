import os
import csv

#Define variables
total_votes = 0
candidates = []
votes_won = [0, 0, 0, 0]
percent_won = []

# Path to collect data from the Resources folder
election_csv = os.path.join("python-challenge\Resources",'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    # Loop through the data
    for row in csvreader:

#Calculate total number of votes
        total_votes += 1

        if (row[2] not in candidates): # if the current candidate isn't already in candidates
            candidates.append(row[2]) # add a new candidate to candidates
        
        idx = candidates.index(row[2]) 
        votes_won[idx] += 1 
#Calculate percentage of votes won
    percent_won = [round((votes/total_votes)*100) for votes in votes_won] # percent_won is the array that calculates the percent of total votes won for each candidate
    i = percent_won.index(max(percent_won)) # getting index of the max percentage of votes won
    winner = candidates[i] # winner = candidate with max votes

#Display print statements
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

for i in range(len(candidates)): # i is the indexes of the candidates
    print(f"{candidates[i]}: {percent_won[i]}% ({votes_won[i]})")

print("-----------------------")
print(f"Winner: {winner}")

print("-----------------------")

txtpath = os.path.join("python-challenge\pypoll","Analysis.txt") 
with open(txtpath, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("----------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("----------------------- \n")

    for i in range(len(candidates)): # i is the indexes of the candidates
        txtfile.write(f"{candidates[i]}: {percent_won[i]}% ({votes_won[i]}) \n")

    txtfile.write("-----------------------\n")
    txtfile.write(f"Winner: {winner} \n")

    txtfile.write("-----------------------\n")
