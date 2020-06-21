import csv 
import os

outputfile = os.path.join("Analysis", "poll.txt")
inputfile = os.path.join("Resources", "election_data.csv")
#establishing variables
each_candidate = {}  #start a dictionary
candidate = []
total_votes = 0
winner = []

with open(inputfile) as election_data: #telling where to look and how to read the file
    csvreader =csv.reader(election_data, delimiter=',')
    
    print(csvreader)
    
    header = next(csvreader) #we are telling what the header is

    for row in csvreader:

        total_votes += 1 #this is for adding votes within the loop
        candidate = row[2]
        if candidate not in each_candidate: # this conditional will start feeding the candidates in the dictionary 
           each_candidate [candidate] =1 # when a new candidate is found within the loop
        else:
           each_candidate [candidate] +=1 # if the candidate exists, add 1 to the vote count
        
winner = max(each_candidate, key=each_candidate.get) # got this from https://tutorialdeep.com/knowhow/key-maximum-value-dictionary-python/

print("Election Results")
print("--------------------")
print("Total Votes: "+str(total_votes))
print("--------------------")
# my tutor guided me to this website to get the format for the percentages https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
print("Khan: " + "{:.3%}".format(each_candidate["Khan"] / total_votes) +  " ("+ str(each_candidate["Khan"])+")")
print("Correy: " + "{:.3%}".format(each_candidate["Correy"] / total_votes) +  " ("+ str(each_candidate["Correy"])+")")
print("Li: " + "{:.3%}".format(each_candidate["Li"] / total_votes) +  " ("+ str(each_candidate["Li"])+")")
print("O'Tooley: " + "{:.3%}".format(each_candidate["O'Tooley"] / total_votes) +  " ("+ str(each_candidate["O'Tooley"])+")")
print("--------------------")
print("Winner: " + winner + "  in the best Captain James T. Kirk Scream!")# had to do it!
print("--------------------")

#this is to write to another file
with open(outputfile, 'w') as poll:
    poll.write("Election Results\n")
    poll.write("-------------------\n")
    poll.write("Total Votes: "+str(total_votes))
    poll.write("\n")
    poll.write("-------------------\n")
    poll.write("Khan: " + "{:.3%}".format(each_candidate["Khan"] / total_votes) +  " ("+ str(each_candidate["Khan"])+")")
    poll.write("\n")
    poll.write("Correy: " + "{:.3%}".format(each_candidate["Correy"] / total_votes) +  " ("+ str(each_candidate["Correy"])+")")
    poll.write("\n")
    poll.write("Li: " + "{:.3%}".format(each_candidate["Li"] / total_votes) +  " ("+ str(each_candidate["Li"])+")")
    poll.write("\n")
    poll.write("O'Tooley: " + "{:.3%}".format(each_candidate["O'Tooley"] / total_votes) +  " ("+ str(each_candidate["O'Tooley"])+")")
    poll.write("\n")
    poll.write("------------------\n")
    poll.write("Winner: " + winner + "  in the best Captain James T. Kirk Scream!")
    poll.write("\n")
    poll.write("------------------")

