# Election__Analysis

## Project Overview
A Colorado Board of Elections has given the following tasks to complete an election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of counties who received votes
3. Calculate the total number of votes each county received
4. Get a complete list of votes each candidate received
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python, Visual Studio Code

## Election-Audit Results
### The analysis of the election show that
There were 369,711 Votes cast in the election.

### Counties 
- Jefferson 
- Denver 
- Arapahoe 

### Counties data
- Jefferson county received 10.5% of the votes with 38,855 votes
- Denver county received 82.8% of the votes with 306,055 votes
- Arapahoe county received 6.7% of the votes with 24,801 votes


### The Candidates data:
- Charles Casper Stockham received 23.0% of the votes with 85,213 total votes
- Diana DeGette received 73.8% of the votes with 272,892 total votes
- Raymon Anthony Doane recevied 3.1% of the votes with 11,606 total votes


### The Winner of the Election:
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

![image](https://user-images.githubusercontent.com/109490755/198905232-6fc12923-2283-4921-a40e-51cc497be041.png)



## Election-Audit Summary
### Business Proposal
We can use this code as a base and format the script to review a lot of election results. the script currently looks at only 3 variables but with additional data we can add much more in-depth information such as party they align to, where their voters reside to review what areas, each candidate are most popular and much more information.   

A modification to the script is we could initiate an input variable and ask the user which data they want to see with a popup asking, “do you want to see County data, Candidate data, or both?” dependent on their answer the respective data would write the txt file.  This is useful as with large files there could be load of information that wouldn’t be easily digestible, with this input we can help our user narrow down what exactly they are looking for.


Another modification is all our variables are above the open the election data file.  It is a little confusing going back to the top of the script to see the variables you have initiates since they all are part of the election data script.  A proposal is to include these variables where they are readily used as the county variables should be close to the county for loop and the candidate variables next to the candidate for loop etc…  

![image](https://user-images.githubusercontent.com/109490755/198905236-3a4b528c-4cbc-47a0-a13f-ce08b2bf7e45.png)



 

