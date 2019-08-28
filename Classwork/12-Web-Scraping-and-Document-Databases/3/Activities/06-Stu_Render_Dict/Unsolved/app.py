# import necessary libraries
from flask import Flask, render_template

# Initialize your Flask app here
app = Flask(__name__)

# Create a list of dictionaries
animal_dict = [{"Name": "Petey", "Type": "Dog"}, 
                {"Name": "Sasha", "Type": "Cat"}, 
                {"Name":"Luna", "Type": "Fish"}, 
                {"Name":"Freddie", "Type":"Turtle"}]

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
@app.route("/")
def index():
    return render_template("index.html", list=animal_dict)

if __name__ == "__main__":
    app.run(debug=True)
