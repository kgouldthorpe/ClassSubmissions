import os
import csv
csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')
Found = False

print("Welcome to the Netflix Search Engine")
print("----------------------------------------")
Selection = input("What movie are you looking for? ")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[0] == Selection:
            print(row[0] + " is rated " + row[1] + " and received a score of " + row[5])
                 
        Found = True

        break
        
    if Found is False        
        print("I'm sorry, you're video could not be found.")
