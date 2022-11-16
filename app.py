from flask import Flask, render_template, request, flash 
# flask is main thing, render_template is html, request is for inputs, flash is for outputs
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = "stupidkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zotdots/database.db'
db = SQLAlchemy(app)
initialized = False


class Pixel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    color = db.Column(db.Text)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<point {self.x, self.y}>'

@app.route("/home")
def index():
    flash("what are we drawing today?")
    if not initialized:
        initialize_canvas()
    
    return render_template("index.html") 

def initialize_canvas():
    idx = 0
    for i in range(10):
        for j in range(10):
            #white, red, orange, yellow, green, blue, purple, pink, black, brown
            p = Pixel(id = idx, x = i, y = j, color = 'white')
            db.session.add(p)
            idx += 1


@app.route("/", methods=["POST","GET"])
def getName():
    flash("Hi, " + str(request.form['name_input']) + "! Thanks for adding to ZotDots :D")
    return render_template("index.html")
