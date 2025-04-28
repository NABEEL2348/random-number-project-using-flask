from flask import Flask, render_template, request
import csv
import random
import os

app = Flask(__name__)

# Function to load names from a CSV file
def load_names_from_csv(file):
    names = []
    file.stream.seek(0)  # Make sure we start reading from beginning
    reader = csv.DictReader(file.stream.read().decode("utf-8").splitlines())
    for row in reader:
        names.append(row["Full Name"])
    return names

# Function to select 3 random names
def select_random_names(names):
    winners = random.sample(names, 3)  # Pick 3 unique winners
    return {
        'Winner': winners[0],
        'Runner-up': winners[1],
        'Second Runner-up': winners[2]
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            names = load_names_from_csv(file)
            selected_people = select_random_names(names)
            return render_template("index.html", selected_people=selected_people)
    
    return render_template("index.html", selected_people=None)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))  # default to 10000
    app.run(host='0.0.0.0', port=port)
