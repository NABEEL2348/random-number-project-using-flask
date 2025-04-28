import csv
import random

# Load the CSV file
filename = "teams_activity.csv"

# Read Full Names from the CSV
full_names = []
with open(filename, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        full_names.append(row["Full Name"])

# Randomly select 3 unique winners
winners = random.sample(full_names, 3)

# Print the winners
print("🎉 Winners are:")
for i, winner in enumerate(winners, start=1):
    print(f"{i}. {winner}")
