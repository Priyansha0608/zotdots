from flask import Flask, render_template, request, flash 
# flask is main thing, render_template is html, request is for inputs, flash is for outputs
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
import json

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

def initialize_canvas():
    idx = 0
    for i in range(10):
        for j in range(10):
            #white, red, orange, yellow, green, blue, purple, pink, black, brown
            p = Pixel(id = idx, x = i, y = j, color = 'white')
            db.session.add(p)
            idx += 1

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
    return [x, y, color]

    # pixelInfo = json.loads(pixelInfo)
    # print(pixelInfo)
    # return('/')


    # output = request.get_json()
    # print(output) # This is the output that was stored in the JSON within the browser
    # print(type(output))
    # result = json.loads(output) #this converts the json output to a python dictionary
    # print(result) # Printing the new dictionary
    # print(type(result))#this shows the json converted as a python dictionary
    # return result

@app.route("/", methods=["POST","GET"])
def index():
    if not initialized:
        initialize_canvas()
    
    return render_template("index.html") 
