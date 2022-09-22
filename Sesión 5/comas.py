# CSV = Comma Separated Values = Valores separados por comas.
import csv

nombres = ""

with open("profes.csv") as file:
    lector = csv.reader(file)

    for row in lector:
        nombres = nombres + ", " + str(",".join(row))

print(nombres)
