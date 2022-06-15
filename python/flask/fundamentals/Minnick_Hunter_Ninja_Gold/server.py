from flask import Flask, render_template, session, redirect, request
import random 
# random.randint(1,50)

app = Flask(__name__)

app.secret_key= "secret key"

@app.route('/')
def index():
    if 'money' not in session:
        session['money']= 0
    # message = "<ul><li> qwe </li></ul> message = message "
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def proc_mon():
    if request.form['building'] =='farm':
        session['money'] += random.randint(10,20)
    elif request.form['building'] =='cave':
        session['money'] += random.randint(5,10)
    elif request.form['building'] =='house':
        session['money'] += random.randint(2,5)
    elif request.form['building'] =='casino':
        session['money'] += random.randint(-50,50)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)