import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'web_jargon'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-7mwaw.mongodb.net/web_jargon?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template("home.html")

@app.route('/get_defin')
def get_defin():
       return render_template("def.html", 
    defines=mongo.db.definitions.find())
    

@app.route('/add_jargon')
def add_jargon():
    return render_template('addjargon.html',
    category=mongo.db.categories.find())


@app.route('/insert_jargon', methods=['POST'])
def insert_jargon():
    definitions =  mongo.db.definitions
    definitions.insert_one(request.form.to_dict())
    return render_template("insertjargon.html")  


@app.route('/search',  methods=['GET', 'POST'])
def search():
    text = request.form["projectFilePath"]
    return render_template("searchdef.html",
    defines=mongo.db.definitions.find({'def_name': text}))

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)