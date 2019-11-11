import os
import csv

# Import CSV here
file = os.path.join("PyPoll/Resource", "election_data.csv")

Candidate = []
VoteCounter = []
rowcount = 0
Winner = 0
WinnerName = ""
i = 0

with open(file, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	# Skip header line
	next(csvreader, None)
	
	for row in csvreader:
		rowcount = rowcount + 1
		if row[2] not in Candidate:
			Candidate.append(row[2])
			VoteCounter.append(0)
		else:
			VoteCounter[Candidate.index(row[2])] = VoteCounter[Candidate.index(row[2])] + 1

Winner = max(range(len(VoteCounter)), key = lambda x: VoteCounter[x])
WinnerName = Candidate[int(Winner)]

print("Election Results are in!")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Total Votes: " + str(rowcount))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
while i <= (len(Candidate) - 1):
	print(Candidate[i] + ": " + str(round((VoteCounter[i]/rowcount * 100),2)) + "% (" + str(VoteCounter[i]) + ")")
	i = i + 1
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Winner: " + str(WinnerName))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

i = 0

with open("Output.txt", "w") as output:
	output.write("Election Results are in!\n")
	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	output.write("Total Votes: " + str(rowcount) + "\n")
	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	while i <= (len(Candidate) - 1):
		output.write(Candidate[i] + ": " + str(round((VoteCounter[i]/rowcount * 100),2)) + "% (" + str(VoteCounter[i]) + ")\n")
		i = i + 1
	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	output.write("Winner: " + str(WinnerName) + "\n")
	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")