import csv
from email import header
from email.headerregistry import HeaderRegistry
import os

# Assign variable to load
file_to_load = os.path.join("election_results.csv")

# Assign variable to save
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign Variable to keep track of votes
total_votes = 0 

#Assing variable to keep track of candidates
candidate_options = []

#Variable to keep track of votes for each candidate
candidate_votes = {}

#Tracking the winning candidates information
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#opening the Election Data CSV
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Assign headers using next variable and print
    headers = next(file_reader)
    print(headers)

    #Loop to iterate through each row to keep track of candidate information
    for row in file_reader:
        
        #Increase votes for each candidate
        total_votes += 1
        
        #Assigning a value to each Candidate
        candidate_name = row[2]
        
        #Creating a list of candidates 
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Calcualting the total votes for each candidate    
        candidate_votes[candidate_name] += 1

    #Loop to iterate through each candidate and calculate the votes for each
    for candidate_name in candidate_votes:

        #assigning the total amount of votes to each candidate
        votes = candidate_votes[candidate_name]

        #Calculating the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

        #If statement to determine which Candidate has the most amount of votes and assign them as the Winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Printing Winning Candidate summary information
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
