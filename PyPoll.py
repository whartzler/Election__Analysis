import csv
from email import header
from email.headerregistry import HeaderRegistry
import os

# Assign variable to load
file_to_load = os.path.join("election_results.csv")

# Assign variable to save
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Assign headers using next variable and print
    headers = next(file_reader)
    print(headers)