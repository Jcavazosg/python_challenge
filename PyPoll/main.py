import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

Candidates = {}
Votes = 0
Votes_Counted = 0
percent_of_votes = 0
Most_Votes = 0
Most_Voted = ""

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
        
    for row in csvreader:
        candidate = row[2]
        Votes += 1
        
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
    
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {Votes}")
    print("------------------------")
    
    for candidate in Candidates:
        Votes_Counted += Candidates[candidate]
    
        percent_of_votes = (Candidates[candidate])/(Votes) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {Votes_Counted}")
        
        if Candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = Candidates[candidate]
        
    print("-----------------------")
    
    print(f"Winner: {Most_Voted}")
    
    print("-----------------------")
    
    
output_path = os.path.join(".", 'output.txt')

with open (output_path, 'w') as txt: 
    txt.write("Poll Analysis")
    txt.write("\n")
    txt.write("-----------------")
    txt.write("\n")
    txt.write("Election Results")
    txt.write("\n")
    txt.write("------------------")
    txt.write("\n")
    txt.write(f"Total Votes: {Votes}")
    txt.write("\n")
    txt.write("------------------")
    txt.write("\n")
    txt.write(f"Winner: {Most_Voted}")
    txt.write("\n")
    txt.write("------------------")

 
    
    
    