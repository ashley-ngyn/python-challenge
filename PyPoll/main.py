#PyPoll main.py

#create file path
import os

#reading cvs file
import csv

#path to find the cvs file
csvpath = os.path.join('Resources', 'election_data.csv')

#make empty lits (source 01)
candidate_list = []

#set variables to 0
charles = 0
diana = 0
raymon = 0

#open cvs file
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)

    #read headers
    cvsheader = next(csvfile)

    #loop through candidates
    for row in csvreader:
        #put candidates into a list (source 05)
        candidate_list.append(row[2])

    #use if function
    #source 10 for += to add to variable list
        if row[2] == "Charles Casper Stockham":
            charles +=1
        elif row[2] == "Diana DeGette":
            diana +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon +=1

#calculate the total votes
total_votes = len(candidate_list)

#create another if statement and use conditionals to find winner
if charles > diana and raymon:
    winner = "Charles Casper Stockham"
elif diana > charles and raymon:
    winner = "Diana DeGette"
elif raymon > charles and diana:
    winner = "Raymon Anthony Doane"

#calculate percentages
#source 11 for rounded to third decimal place
charles_percent = round(((charles/total_votes) * 100), 3)
diana_percent = round(((diana/total_votes) * 100), 3)
raymon_percent = round(((raymon/total_votes) * 100), 3)


#print analysis in terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {charles_percent}% ({charles})")
print(f"Diana DeGette: {diana_percent}% ({diana})")
print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export a text file with the results (soruce 9)
filepath = os.path.join("analysis", "PyPoll_analysis.txt")
with open(filepath, 'w') as textfile:
    textfile.write("Election Results")
    textfile.write("\n-------------------------")
    textfile.write(f"\nTotal Votes: {total_votes}")
    textfile.write("\n-------------------------")
    textfile.write(f"\nCharles Casper Stockham: {charles_percent}% ({charles})")
    textfile.write(f"\nDiana DeGette: {diana_percent}% ({diana})")
    textfile.write(f"\nRaymon Anthony Doane: {raymon_percent}% ({raymon})")
    textfile.write("\n-------------------------")
    textfile.write(f"\nWinner: {winner}")
    textfile.write("\n-------------------------")