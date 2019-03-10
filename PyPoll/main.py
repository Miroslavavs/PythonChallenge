import os
import csv

#PATHFILE
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
file_to_output = "election_results.txt"
#/Users/miroslavavillalobos/Downloads/RepositorioGitLab/TECMC201902DATA2/02-Homework/03-Python/Instructions/
totalVotes = 0
candidates = []
candidateVotes = {}
winnerCount = 0
winner = ""
# FILLE OPENING
with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #TOTAL VOTES
    for row in csvreader:     
        totalVotes += 1
        candidate = row["Candidate"]
       
        if candidate not in candidates:
            candidates.append(candidate)
            candidateVotes[candidate] = 1
        
        candidateVotes[candidate] = candidateVotes[candidate] + 1

#WRITING IN THE FILE OUTPUT
with open(file_to_output, 'w') as txt_file:
    
    electionHeader = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(electionHeader)

    print ("Total Votes:")
    print (totalVotes)
    #votesTot = len (row["Voter ID"])
    #print("Total Votes:")
    #print(votesTot)
    for candidate in candidateVotes:
        votes = candidateVotes[candidate]
        votePercentage = float(votes)/float(totalVotes)*100
        if (votes > winnerCount):
            winnerCount = votes
            winner = candidate
        voterOutput = f"{candidate}: {votePercentage:.3f}% ({votes})\n"
        print(voterOutput)
        txt_file.write(voterOutput)
          
    winningSummary = (
        f"Winner: {winner}"
    )
    print(winningSummary)
    txt_file.write(winningSummary)


