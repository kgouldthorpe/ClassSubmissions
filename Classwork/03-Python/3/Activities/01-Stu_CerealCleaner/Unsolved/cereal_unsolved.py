import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")

with open(cereal_csv, newline="") as cerealfile:
    cerealfile = csv.reader(cerealfile, delimiter=",")

    cereal_header = next(csv.reader, None)
    for row in cerealfile:
        
       if float (row[7])>=5:
           print(row)





