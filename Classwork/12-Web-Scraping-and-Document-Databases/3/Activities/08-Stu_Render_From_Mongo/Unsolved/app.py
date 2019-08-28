from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.store_inventory
db.store_inventory.drop()
db.store_inventory.insert_many(
    [
        {
        "type": "apples",
        "cost": .23,
        "stock": 333
        },
        {
        "type": "oranges",
        "cost": .45,
        "stock": 259
        },
        {
        "type": "pears",
        "cost": .78,
        "stock": 156
        },
        {
        "type": "carrots",
        "cost": .05,
        "stock": 1000
        },
        {
        "type": "bananas",
        "cost": .24,
        "stock": 340
        }
    ]
)    

@app.route('/')
def index():
    # Store the entire team collection in a list
    inventories = list(db.store_inventory.find())
    print(inventories)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template('index.html', inventories = inventories)


if __name__ == "__main__":
    app.run(debug=True)
