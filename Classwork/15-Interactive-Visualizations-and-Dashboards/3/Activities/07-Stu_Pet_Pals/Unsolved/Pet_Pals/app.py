# import necessary libraries
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    type = db.Column(db.String(64))

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

@app.route("/send", methods = ["GET", "POST"])
def send():
    if request.method == "POST":
        nickname = request.form["nickname"]
        type = request.form["type"]

        pet = Pet(nickname = nickname, type = type)
        db.session.add(pet)
        db.session.commit()

        return "Thank you for the information on your pet!"
    return render_template("form.html")

@app.route("/api/pals")
def pet_list():
    results = db.session.query(Pet.nickname, Pet.type).all()

    pets = []
    for result in results:
        pets.append({"Name":result[0], "Type": result[1]})
        return jsonify(pets)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
