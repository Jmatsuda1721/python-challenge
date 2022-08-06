import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
summary_file=('/Users/jenm/Desktop/DataClass/HMW/Challenge_3/python-challenge/PyPoll/analysis')
analysis_txt=('/Users/jenm/Desktop/DataClass/HMW/Challenge_3/python-challenge/PyPoll/election_data.txt')

votes_total=0
Ccs_p=0
Ccs_v=0
Dd_p=0
Dd_v=0
Rad_p=0
Rad_v=0
votes_winner=0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    #Read the header row first
    next(csvreader) 
   
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        votes_total=votes_total +1
        if row[2]== "Charles Casper Stockham":
            Ccs_v +=1
        elif row[2]=="Diana DeGette":
            Dd_v +=1
        elif row[2]=="Raymon Anthony Doane":
            Rad_v +=1

results={"Charles Casper Stockham":Ccs_v, "Diana DeGette":Dd_v, "Raymon Anthony Doane":Rad_v}

Ccs_p=round((Ccs_v/votes_total)*100,3)
Dd_p=round((Dd_v/votes_total)*100,3)
Rad_p=round((Rad_v/votes_total)*100,3)

votes_winner=max(results,key=results.get)

#Generate output lines
output = f"""
Election Results
-------------------------
Total Votes: {votes_total}
-------------------------
Charles Casper Stockham: {Ccs_p}% ({Ccs_v})
Diana DeGette: {Dd_p}% ({Dd_v})
Raymon Anthony Doane: {Rad_p}% ({Rad_v})
-------------------------
Winner: {votes_winner}
"""
print(output)
#Write into text file 
with open(summary_file,'w') as summary_file:
    summary_file.write(output)
with open(analysis_txt,'w') as analysis_txt:
    analysis_txt.write(output)    