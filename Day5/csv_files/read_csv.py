
import csv

from pathlib import Path

names_csv_path = Path("name.csv")

with names_csv_path.open(encoding="UTF-8") as csv_file:
   csv_reader = csv.reader(csv_file,delimiter=",",quotechar='"')

   next(csv_reader)

   for row in csv_reader:
      print(row)

