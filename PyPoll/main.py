# Allows us to use functions in operating systems
import os 

# Brings in functions for CSV files
import csv

csvpath = os.path.join('.', 'Resources','election_data.csv')

candidates = []   #creates empty list to capture the candidates

with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

   

    for row in csvreader:
        candidates.append(row[2])

    


# Open a text file in analysis folder with write mode
with open("analysis/results.txt", "w") as file:

    # writes headers to text file 'results.txt' 
    file.write("Election Results:\n")    
    file.write("-----------------------\n")

    # writes headers to terminal 
    print("\nElection Results:")    
    print("-----------------------")

    # tallies the number of votes
    num_votes = len(candidates)

    file.write(f"Total Votes: {num_votes}\n")
    file.write("-----------------------\n")

    print(f"Total Votes: {num_votes}")
    print("-----------------------")

    # creates a list with unique candidates' names
    unique_names=set(candidates)
    #print(unique_names)
    
    winner = ''   # initializes for winner name
    winner_count = 0  # initializes vote counter for winning candidate

    for canidate in sorted(unique_names):  # sorts the candidates' names alphebetically
        vote_percent = candidates.count(canidate)/num_votes  # calculates the percentage of votes each candidate received
        # writes to the text file the percentage of votes and total number of votes each candidate received
        file.write(f'{canidate}: {vote_percent: .3%} ({(candidates.count(canidate))})\n')

        print(f'{canidate}: {vote_percent: .3%} ({(candidates.count(canidate))})')

        # compares the total number of votes to determine the winner
        if (candidates.count(canidate))>winner_count:
            winner = canidate       # stores the winning candidate's name
            winner_count = candidates.count(canidate)    # stores the number of votes the candidate received

    file.write("-----------------------\n")
    file.write(f'Winner: {winner}\n')
    file.write("-----------------------\n")  

    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------") 
      