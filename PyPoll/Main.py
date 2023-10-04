import os
import csv

#Inspiration derived from/code sourced from: https://github.com/eddiexunyc/python-challenge/blob/main/PyPoll/main.py

cand_list = {}
break_line = "------------------------------"

# Import csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")  

# Open and read csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    total_vote = 0
    for row in csv_reader:
        #increase total_vote
        total_vote += 1
        name = row[2]
        if name in cand_list:
            cand_list[name] += 1
        else:
            cand_list[name] = 1

#calculate who won    
cand_list["Khan Percent"] = round((cand_list["Khan"]/total_vote) * 100, 2)
cand_list["Correy Percent"] = round((cand_list["Correy"]/total_vote) * 100, 2)
cand_list["Li Percent"] = round((cand_list["Li"]/total_vote) * 100, 2)
cand_list["O'Tooley Percent"] = round((cand_list["O'Tooley"]/total_vote) * 100, 2)

cand_winner = max(cand_list, key=cand_list.get)

#print the results
print("Election Results")
print(break_line)
print("Total Vote: " + str(total_vote))
print(break_line)
print("Khan: " + str(cand_list["Khan Percent"]) + "% " + str(cand_list["Khan"])) 
print("Correy: " + str(cand_list["Correy Percent"]) + "% " + str(cand_list["Correy"]))
print("Li: " + str(cand_list["Li Percent"]) + "% " + str(cand_list["Li"]))
print("O'Tooley: " + str(cand_list["O'Tooley Percent"]) + "% " + str(cand_list["O'Tooley"]))
print(break_line)
print("Winner: " + str(cand_winner))
print(break_line)

#write results to result.txt analysis file
output_result = os.path.join(".", "analysis", "result.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Total Vote: " + str(total_vote) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Khan: " + str(cand_list["Khan Percent"]) + "% " + str(cand_list["Khan"]) + "\n") 
    txt_file.write("Correy: " + str(cand_list["Correy Percent"]) + "% " + str(cand_list["Correy"]) + "\n")
    txt_file.write("Li: " + str(cand_list["Li Percent"]) + "% " + str(cand_list["Li"]) + "\n")
    txt_file.write("O'Tooley: " + str(cand_list["O'Tooley Percent"]) + "% " + str(cand_list["O'Tooley"]) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Winner: " + str(cand_winner) + "\n")
    txt_file.write(break_line + "\n")