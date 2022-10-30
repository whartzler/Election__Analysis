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
    
    #Open new txt file to write Election Data to
    with open(file_to_save, "w") as txt_file:

        #Formatting the Results of Election data and printing total votes
        election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n")

        #Print Election Results to txt file and terminal
        print(election_results, end="")
        txt_file.write(election_results)

        #Loop to iterate through each candidate and calculate the votes for each
        for candidate_name in candidate_votes:

            #assigning the total amount of votes to each candidate
            votes = candidate_votes[candidate_name]

            #Calculating the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100

            #creating candidate results variable
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #Printing the candidate results output to txt file and terminal
            print(candidate_results)
            txt_file.write(candidate_results)

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

        #Print Winning Candidate Summary to txt file and terminal
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)