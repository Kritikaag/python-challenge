#Module for reading CSV files
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'election_data.csv')
voterid_number_list = []
candidate_list = set()
max_count = 0

with open(csvpath) as csvfile:

      # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader :
        voterid_number_list.append (str(row [2]))
        candidate_list.add(str(row [2]))

        #print(voterid_number_list)


total_vote = len(voterid_number_list)

print ("Election Results")

print("---------------------")

print ("Total Votes: ",total_vote)

print (candidate_list)

total_candidates = len(candidate_list)

for x in candidate_list:
    candidate_count = voterid_number_list.count(x)
    percentage_votes = round(( candidate_count / total_vote ) * 100,2)


    print (x,'votes count is :',candidate_count,percentage_votes,'%')
    if candidate_count > max_count: 
        max_count = candidate_count
        winner = x

print("winner is", winner,'with maximum votes of:', max_count)