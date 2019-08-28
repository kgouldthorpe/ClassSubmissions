# import necessary libraries
from flask import Flask, render_template

# Initialize your Flask app here
app = Flask(__name__)


# Create a route and view function that takes in a list of strings and renders index.html template
@app.route("/")
def index():
    movie_list = ["Old Cold", "Tommy Boy", "Bridesmaid", "Thor Ragnarok", "Armageddon"]
    return render_template("index.html", list=movie_list)

if __name__ == "__main__":
    app.run(debug=True)
