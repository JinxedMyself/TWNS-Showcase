from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import tweepy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:C2FM8tnksy74djMnUWnjLchj@localhost/NS_Twitter'
db = SQLAlchemy(app)

tweets = [
    {
        'author': 'Anonymous',
        'message': 'Great service',
        'date_posted': 'June 4, 2020'
    },
    {
        'author': 'John Dough',
        'message': 'The trains are dirty!',
        'date_posted': 'June 5, 2020'
    }
]

# class Tweets(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String(120), nullable=False)
#     message = db.Column(db.Text, nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     moderation_status = db.Column(db.Boolean, nullable=True)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", tweets=tweets)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)