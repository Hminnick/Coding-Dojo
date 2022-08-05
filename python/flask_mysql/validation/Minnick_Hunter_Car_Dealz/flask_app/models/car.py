from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Car:
    db = 'car_dealz_schema'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.price = db_data['price']
        self.model = db_data['model']
        self.make = db_data['make']
        self.year = db_data['year']
        self.description = db_data['description']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        if 'first_name' in db_data:
            self.seller = db_data['first_name'] + db_data['last_name']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description, user_id) VALUES (%(price)s,%(model)s,%(make)s,%(year)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_cars = []
        for row in results:
            all_cars.append( cls(row) )
        return all_cars
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if results:
            return cls( results[0] )
        return False

    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET price=%(price)s,model=%(model)s, make=%(make)s, year=%(year)s, description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_car(car):
        is_valid = True
        if car['price'] == "":
            is_valid = False
            flash("Car must have value!","car")
        if len(car['model']) < 2:
            is_valid = False
            flash("Model must be at least 2 characters","car")
        if len(car['make']) < 2:
            is_valid = False
            flash("Make must be at least 2 characters","car")
        if len(car['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","car")
        return is_valid
