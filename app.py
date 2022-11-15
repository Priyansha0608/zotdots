from flask import Flask, render_template, request, flash 
# flask is main thing, render_template is html, request is for inputs, flash is for outputs

app = Flask(__name__)
app.secret_key = "stupidkey"

@app.route("/question")
def index():
    flash("what are we doing?")
    return render_template("index.html") 

@app.route("/whatis", methods=["POST","GET"])
def answerme():
    flash("Hi, let's do " + str(request.form['verb_input']) + "!")
    return render_template("index.html") 

