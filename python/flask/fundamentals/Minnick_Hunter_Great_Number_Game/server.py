from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)

app.secret_key = 'secret key'

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    if "count" not in session:
        session["count"]= 0
    else:
        session["count"] += 1
    return render_template("index.html")
    
@app.route('/answer',methods=['POST'])
def answer():
    session['answer']= int(request.form['answer'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)