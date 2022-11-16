from flask import Flask, render_template, request, flash 
# flask is main thing, render_template is html, request is for inputs, flash is for outputs
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = "stupidkey"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///zotdots/database.db'
db = SQLAlchemy(app)

class Canvas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    color = db.Column(db.Text)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<point {self.x, self.y}>'

canvas_array = []

@app.route("/question")
def index():
    flash("what are we doing?")
    return render_template("index.html") 

def initialize_canvas():
    idx = 0
    for i in range(10):
        for j in range(10):
            #white, red, orange, yellow, green, blue, purple, pink, black, brown
            c = Canvas(id = idx, x = i, y = j, color = 'white')
            db.session.add(c)
            idx += 1

@app.route("/whatis", methods=["POST","GET"])
def answerme():
    flash("Hi, let's do " + str(request.form['verb_input']) + "!")
    return render_template("index.html") 

