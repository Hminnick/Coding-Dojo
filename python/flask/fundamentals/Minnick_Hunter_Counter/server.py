from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key= "secret key"

@app.route('/')
def index():
    if "count" not in session:
        session["count"]= 0
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/2')
def index2():
    session["count"] += 2
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)