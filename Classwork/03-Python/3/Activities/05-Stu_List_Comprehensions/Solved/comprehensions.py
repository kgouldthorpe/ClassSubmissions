cdnames = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

lowercased = [name.lower() for name in names]
titlecased = [name.title() for name in lowercased]
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
for row in election_data.values():
    
    #calcuate total votes cast
    total_votes = len(election_data[row[0]])
    print(total_votes)

    #calculate complete list of candidates

    #calculate total vote per candidate

    #calculate percentages of votes for each candidate

    #calculate winner of the election
#Read CSV

