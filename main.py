import os
import csv

election_data_csv = os.path.join ("Resources", "election_data.csv")
#election_data_csv = '/Users/siykee/Downloads/Starter_Code-3/PyPoll/Resources/election_data.csv'

#file_to_save = os.path.join ("analysis", "election_results.txt")
file_to_save = 'file_to_save/analysis'

#Initalizing list in dictonary 
Canidates_list = []
Canidates_votes = {}
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Reading the header
    header = next(csv_reader)
    #Initalize total vote counter
    Total_votes = 0
    #Read each row of data after header
    for row in csv_reader:
        Canidate = row[2]
        if Canidate not in Canidates_list: 
            Canidates_list.append(Canidate)
            #Starting off each canidate at 0
            Canidates_votes[Canidate]=0
        #Each time it reads each indiviual canidates name in set, it'll add onto their amount of votes
        Canidates_votes[Canidate]=Canidates_votes[Canidate] + 1
        #Asssigning new values onto exisiting variables
        Total_votes+= 1
#Printing title and total votes into terminal
    print(
       f"\nElection Results\n"
       f"-----------------------\n"
       f"Total Votes: {Total_votes:,}\n"
       f"\n-----------------------\n")

#Printing title and total votes into text file
    election_results = (
       f"\nElection Results\n"
       f"-----------------------\n"
       f"Total Votes: {Total_votes:,}\n"
       f"\n-----------------------\n")

#Ruling winning canidate
winning_count = 0
winning_percentage = 0
winning_canidate = ""

#Retrieve each canidates percantages 
for Canidate_name in Canidates_votes:
    votes = Canidates_votes.get(Canidate_name)
    votes_percentage = float(votes) / float(Total_votes) * 100
    canidate_results = (
        f"{Canidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
    print(canidate_results)

#determining winninng canidate
    if (votes_percentage > winning_percentage ) and (votes > winning_count):
        winning_percentage = votes_percentage
        winning_count = votes
        winning_canidate = Canidate_name

ruling_winning_canidate =(
    f"-----------------------\n" 
    f"Winner: {winning_canidate}\n"
    f"-----------------------\n")
print(ruling_winning_canidate)

#adding results to text file
with open(file_to_save, 'w') as txt_file:
    txt_file.write(election_results)
    txt_file.write(canidate_results)
    txt_file.write(ruling_winning_canidate)


    


    


