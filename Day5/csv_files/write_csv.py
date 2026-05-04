import csv

from pathlib import Path

names_csv_path = Path("name.csv")

with names_csv_path.open("w",encoding="UTF-8") as csv_file:
    writer = csv.writer(csv_file,delimiter=",")

    writer.writerow(["first_name","last_name"])
    writer.writerow(["Bob","Smith"])
    writer.writerow(["Joan","Thomas"])
    writer.writerow(["Tim","Timmons"])

