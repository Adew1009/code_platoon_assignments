from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

from datetime import datetime, timedelta

# Calculate the date 21 years ago from the current date
twenty_one_years_ago = datetime.now() - timedelta(days=21*365)

app = Flask(__name__)
# app = Flask(__name__.split('.')[0])
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://andrew-dew:"password"@localhost/school'

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    birthdate = db.Column(db.Integer)
    address_id = db.Column(db.String(10))
#   id           serial PRIMARY KEY,
#   first_name   varchar(255) NOT NULL,
#   last_name    varchar(255) NOT NULL,
#   birthdate    date NOT NULL,
#   address_id   integer

@app.route('/api/v1/students/', methods=['GET'])
# @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
def get_students():
    students = Students.query.all()
    json_students = [{"id": stud.id, "first_name": stud.first_name,
                      "last_name": stud.last_name, "birthdate": stud.birthdate, "address_id": stud.address_id} for stud in students]
    response = (jsonify(json_students))
    return response


@app.route('/api/v1/old_students/', methods=['GET'])
# @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
def get_old_students():
    students = Students.query.filter(Students.birthdate >= twenty_one_years_ago)
    json_students = [{"id": stud.id, "first_name": stud.first_name,
                      "last_name": stud.last_name, "birthdate": stud.birthdate, "address_id": stud.address_id} for stud in students]
    response = (jsonify(json_students))
    return response
 
@app.route('/api/v1/young_students/', methods=['GET'])
# @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
def get_young_students():
    students = Students.query.filter(Students.birthdate < twenty_one_years_ago)
    json_students = [{"id": stud.id, "first_name": stud.first_name,
                      "last_name": stud.last_name, "birthdate": stud.birthdate, "address_id": stud.address_id} for stud in students]
    response = (jsonify(json_students))
    return response


@app.route('/api/v1/students_age/', methods=['GET'])
# @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
def get_students_age():
    students = Students.query.all()
    today = datetime.now().date()
    json_students = []
    for stud in students:
        age = today.year - stud.birthdate.year - ((today.month, today.day) < (stud.birthdate.month, stud.birthdate.day))
        json_student = {
        "id": stud.id, 
        "first_name": stud.first_name,
        "last_name": stud.last_name, 
        "birthdate": stud.birthdate.strftime("%a, %d %b %Y %H:%M:%S GMT"), 
        # %a: abbreviated weekday name (e.g., Sun, Mon, Tue)
        # %d: day of the month as a zero-padded decimal number (01 to 31)
        # %b: abbreviated month name (e.g., Jan, Feb, Mar)
        # %Y: year with century as a decimal number (e.g., 2024)
        # %H: hour (24-hour clock) as a zero-padded decimal number (00 to 23)
        # %M: minute as a zero-padded decimal number (00 to 59)
        # %S: second as a zero-padded decimal number (00 to 59)
        # GMT: indicates that the time is in Greenwich Mean Time
        # So, strftime("%a, %d %b %Y %H:%M:%S GMT") formats the datetime object into a string representing the date and time in the specified format, including the weekday, day, month, year, hour, minute, second, and timezone information.  
        "age": age
        } 
        json_students.append(json_student)
    response = (jsonify(json_students))
    return response


app.run(port=8000, debug=True)











app.run(port=8000, debug=True)

# @app.route('/api/v1//advance_students', methods=['GET'])  # GET PUT POST DELETE
# def get_advance_students():
#     advance_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["grade"] == "A":
#             advance_students.append(stud)
#     return jsonify(advance_students)




# app.run( debug=True)

