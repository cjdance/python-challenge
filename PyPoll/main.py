#import dependencies
import os
import csv

poll_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Create list to store Voter ID's
voter_id = []
#Create list to hold candidates voted for by voters
candidate_votes = []
#Create list to hold candidate names as single value
candidates = []
#Create List to Hold Total Votes for a Candidate
vote_count = []
#Create list to hold percentage vote count
vote_percent = []

# Open and read csv file containing poll data
with open(poll_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    #store header from CSV file
    header = next(csvreader)

    #Use for loop to count total votes and create list of candidate votes
    for row in csvreader:
        voter_id.append(row[0])
        candidate_votes.append(row[2])

#Total votes is calculated by number of inidividual voter ID's
total_vote = int(len(voter_id))
#Using a set inside Python to find only unique values in the candidate_votes table
#This returns a final list of candidates
candidates = list(set(candidate_votes))
#For loop iterates through for each name of a candidate and creates a count for their total votes
#For loop also creates a value for their percentage, total votes and percentage vote are stored in separate lists
for item in candidates:
    votes = int(candidate_votes.count(item))
    vote_count.append(votes)
    vote_per = round(votes/total_vote * 100,2)
    vote_percent.append(vote_per)
    
#dictionary is created to hold the values from the lists generated previously
#List of candidate names, count of votes and percentage of votes are placed into a dictionary
candidate_list = {"name": "test","vote count": "test","vote %":"test"}
candidate_list["name"] = candidates
candidate_list["vote count"] = vote_count
candidate_list["vote per"] = vote_percent

#Calculating candidate with highest vote count
largest_vote = max(vote_count)
winner_index = vote_count.index(largest_vote)
winner = candidates[winner_index]

#Create path to analysis output file
analysis = os.path.join("..","PyPoll","Analysis","poll_analysis.txt")

#Print final results to terminal
print("Election Results\n")
print("-----------------------\n")
print("Total Votes: " + str(total_vote) + "\n")
print("-----------------------\n")
for i in range(len(candidates)):
    print(f'{candidate_list["name"][i]}: {candidate_list["vote per"][i]}% ({candidate_list["vote count"][i]})\n')
print("-----------------------\n")
print("Winner: " + winner +"\n")
print("-----------------------\n")

#Open txt file and print final results to file
f = open(analysis,'w')
f.write("Election Results\n")
f.write("-----------------------\n")
f.write("Total Votes: " + str(total_vote) + "\n")
f.write("-----------------------\n")
for i in range(len(candidates)):
    f.write(f'{candidate_list["name"][i]}: {candidate_list["vote per"][i]}% ({candidate_list["vote count"][i]})\n')
f.write("-----------------------\n")
f.write("Winner: " + winner +"\n")
f.write("-----------------------\n")









#print(len(voter_id))
#print(len(candidate_votes))


