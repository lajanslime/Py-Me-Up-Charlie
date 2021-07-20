#import Modules 
import csv 
import os 

election_csv = os.path.join("/Users/wolfey/Desktop/homework/PyPoll/Resources/election_data.csv")

total_votes = 0 
khan_votes = 0 
correy_votes = 0 
li_votes = 0 
otooley_votes = 0 

#open CSV and Set Variable 
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Read Header 
    header = next(csv_reader)
    row = next(csv_reader)

    #Set For Loop 
    for row in csv_reader:
        total_votes += 1 
        #Count Candidate votes 
        if (row[2] == "Khan"): 
            khan_votes += 1 
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"): 
            li_votes += 1 
        else: 
            otooley_votes += 1

    #calculate the candidate votes percentage 
    khan_percentage = (khan_votes / total_votes)*100
    correy_percentage = (correy_votes / total_votes)*100
    li_percentage = (li_votes / total_votes)*100
    otooley_percentage = (otooley_votes / total_votes)*100

    #Calculate winner of election 
    winner_of_election = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner_of_election == khan_votes: 
        winner = "Khan"
    elif winner_of_election == correy_votes: 
        winner = "Correy"
    elif winner_of_election == li_votes:
        winner = "Li"
    else: 
        winner = "Otooley" 
    

#Print Values 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(f"Khan: {khan_percentage} ({khan_votes})")
print(f"Correy: {correy_percentage} ({correy_votes})")
print(f"Li: {li_percentage} ({li_votes})")
print(f"O'Tooley {otooley_percentage} ({otooley_votes})")
print("Winner: " + str(winner))


#Write Text File 
with open('Election Results.txt', 'w') as writer:


  writer.write('Election Results')
  writer.write('\n-------------------------')
  writer.write('\n' + "Total Votes: " + str(total_votes))
  writer.write('-------------------------')
  writer.write('\n' + "Khan: " + str(khan_percentage) + str(khan_votes))
  writer.write('\n' + "Correy: " + str(correy_percentage) + str(correy_votes))
  writer.write('\n' + "Li: " + str(li_percentage).format(2) + str(li_votes))
  writer.write('\n' + "O'Tooley: " +  str(otooley_percentage) + str(otooley_votes))
  writer.write('\n' + "Winner: " + str(winner))  


    



