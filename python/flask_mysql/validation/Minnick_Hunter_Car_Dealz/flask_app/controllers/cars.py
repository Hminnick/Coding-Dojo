from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.car import Car
from flask_app.models.user import User

@app.route('/cars/add')
def new_car():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_car.html',user=User.get_by_id(data))

@app.route('/cars/create',methods=['POST'])
def create_car():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect('/cars/add')
    data = {
        "price": request.form["price"],
        "model": request.form["model"],
        "make": request.form["make"],
        "year": request.form["year"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    Car.save(data)
    return redirect('/dashboard')

@app.route('/cars/edit/<int:id>')
def edit_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_car.html",edit=Car.get_one(data),user=User.get_by_id(user_data))

@app.route('/cars/update',methods=['POST'])
def update_car():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect(f"/cars/edit/{request.form['id']}")
    data = {
        "price": request.form["price"],
        "model": request.form["model"],
        "make": request.form["make"],
        "year": request.form["year"],
        "description": request.form["description"],
        "id": request.form['id']
    }
    Car.update(data)
    return redirect('/dashboard')

@app.route('/cars/<int:id>')
def show_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("summary.html",car=Car.get_one(data),user=User.get_by_id(user_data))

@app.route('/cars/destroy/<int:id>')
def destroy_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Car.destroy(data)
    return redirect('/dashboard')