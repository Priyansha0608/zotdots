from flask import Flask, render_template, request, flash 
# flask is main thing, render_template is html, request is for inputs, flash is for outputs
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from sqlalchemy.sql import update

import json
initialized = False
app = Flask(__name__)
app.secret_key = "stupidkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #edited
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app) # initializes an application for the use with this db setup




class Pixel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    color = db.Column(db.Text)
    #updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<point {self.id, self.x, self.y, self.color}>'

def initialize_canvas():
    idx = 0
    for i in range(25):
        for j in range(25):
            #white, red, orange, yellow, green, blue, purple, pink, black, brown
            p = Pixel(id = idx, x = i, y = j, color = 'white')
            db.session.add(p)
            db.session.commit()
            idx += 1

with app.app_context():
    db.drop_all()
    db.create_all() # creates a table in the db

# receive info from canvas.js
@app.route('/test', methods=['POST'])
def test():
    print("in test")
    x = request.form.get("x")
    y = request.form.get("y")
    color = request.form.get("color")
    print("x: " + x)
    print("y: " + y)
    print("color: " + color)

    updateCanvas(x, y, color)

    return [x, y, color]

def updateCanvas(x_coord, y_coord, c):
    # print(Pixel.query.all())
    pixels = Pixel.query.filter_by(x = x_coord, y = y_coord)
    
    for p in pixels:
        print(p)

    pixel = pixels[0]
    pixel.color = c
    db.session.add(pixel)
    db.session.commit()
    
    pixels = Pixel.query.filter_by(x = x_coord, y = y_coord)
    
    for p in pixels:
        print(p)

# def print_current_db():
    


@app.route("/", methods=["POST","GET"])
def index():
    global initialized
    if not initialized:
        initialize_canvas()
        initialized = True
    print_current_db()
    
    return render_template("index.html") 
