from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# # app = Flask(__name__.split('.')[0])



# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
#     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
#     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
#     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
#     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
#     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
# ]

# #https://127.0.0.1:5000/students
# @app.route('/api/v1/students/', methods=['GET'])
# # @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_students():
#     return jsonify(students)


# @app.route('/api/v1/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_old_students():
#     old_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] > 20:
#             old_students.append(stud)
#     return jsonify(old_students)


# @app.route('/api/v1/young_students', methods=['GET'])  # GET PUT POST DELETE
# def get_young_students():
#     young_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] < 21:
#             young_students.append(stud)
#     return jsonify(young_students)


# @app.route('/api/v1//advance_students', methods=['GET'])  # GET PUT POST DELETE
# def get_advance_students():
#     advance_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["grade"] == "A":
#             advance_students.append(stud)
#     return jsonify(advance_students)


# @app.route('/api/v1//student_names', methods=['GET'])  # GET PUT POST DELETE
# def get_student_names():
#     student_names= []
#     for stud in students:
#         # return "HELLO WORLD"
#            student_names.append(f"first_name: {stud['first_name']}, last_name: {stud['last_name']}")
#     return jsonify(student_names)


# @app.route('/api/v1//student_ages', methods=['GET'])  # GET PUT POST DELETE
# def get_student_agess():
#     student_ages = []
#     for stud in students:
#         # return "HELLO WORLD"
#         student_ages.append(
#             f"first_name: {stud['first_name']}, last_name: {stud['last_name']}, age: {stud['age']}")
#     return jsonify(student_ages)

# app.run(port=8000,
#         debug=True)
# # app.run( debug=True)











second_app = Flask(__name__)
# app = Flask(__name__.split('.')[0])
second_app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://andrew-dew:"password"@localhost/school'

db = SQLAlchemy(second_app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(10))

@second_app.route('/api/v1/students/', methods=['GET'])
# @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
def get_students():
    students= Students.query.all()
    json_students = [{"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "age": student.age, "grade": student.grade} for stud in students] 
    response = (jsonify(json_students))
    return response
# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily',
#         'last_name': 'Williams', 'age': 18, 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael',
#         'last_name': 'Brown', 'age': 19, 'grade': 'B'},
#     {'id': '6', 'first_name': 'Samantha',
#         'last_name': 'Davis', 'age': 22, 'grade': 'A'},
#     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
#     {'id': '8', 'first_name': 'Sophia',
#         'last_name': 'Miller', 'age': 21, 'grade': 'A'},
#     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
#     {'id': '10', 'first_name': 'Isabella',
#         'last_name': 'Moore', 'age': 22, 'grade': 'B'}
# ]

# https://127.0.0.1:5000/students


# @app.route('/api/v1/students/', methods=['GET'])
# # @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_students():
#     return jsonify(students)


# @app.route('/api/v1/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_old_students():
#     old_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] > 20:
#             old_students.append(stud)
#     return jsonify(old_students)


# @app.route('/api/v1/young_students', methods=['GET'])  # GET PUT POST DELETE
# def get_young_students():
#     young_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] < 21:
#             young_students.append(stud)
#     return jsonify(young_students)


# @app.route('/api/v1//advance_students', methods=['GET'])  # GET PUT POST DELETE
# def get_advance_students():
#     advance_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["grade"] == "A":
#             advance_students.append(stud)
#     return jsonify(advance_students)


# @app.route('/api/v1//student_names', methods=['GET'])  # GET PUT POST DELETE
# def get_student_names():
#     student_names = []
#     for stud in students:
#         # return "HELLO WORLD"
#         student_names.append(
#             f"first_name: {stud['first_name']}, last_name: {stud['last_name']}")
#     return jsonify(student_names)


# @app.route('/api/v1//student_ages', methods=['GET'])  # GET PUT POST DELETE
# def get_student_agess():
#     student_ages = []
#     for stud in students:
#         # return "HELLO WORLD"
#         student_ages.append(
#             f"first_name: {stud['first_name']}, last_name: {stud['last_name']}, age: {stud['age']}")
#     return jsonify(student_ages)


second_app.run(port=8000, debug=True)
# app.run( debug=True)





# app = Flask(__name__)
# # app = Flask(__name__.split('.')[0])


# students = [
#     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
#     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
#     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
#     {'id': '4', 'first_name': 'Emily',
#         'last_name': 'Williams', 'age': 18, 'grade': 'A'},
#     {'id': '5', 'first_name': 'Michael',
#         'last_name': 'Brown', 'age': 19, 'grade': 'B'},
#     {'id': '6', 'first_name': 'Samantha',
#         'last_name': 'Davis', 'age': 22, 'grade': 'A'},
#     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
#     {'id': '8', 'first_name': 'Sophia',
#         'last_name': 'Miller', 'age': 21, 'grade': 'A'},
#     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
#     {'id': '10', 'first_name': 'Isabella',
#         'last_name': 'Moore', 'age': 22, 'grade': 'B'}
# ]

# # https://127.0.0.1:5000/students


# @app.route('/api/v1/students/', methods=['GET'])
# # @app.route('/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_students():
#     return jsonify(students)


# @app.route('/api/v1/old_students', methods=['GET'])  # GET PUT POST DELETE
# def get_old_students():
#     old_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] > 20:
#             old_students.append(stud)
#     return jsonify(old_students)


# @app.route('/api/v1/young_students', methods=['GET'])  # GET PUT POST DELETE
# def get_young_students():
#     young_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["age"] < 21:
#             young_students.append(stud)
#     return jsonify(young_students)


# @app.route('/api/v1//advance_students', methods=['GET'])  # GET PUT POST DELETE
# def get_advance_students():
#     advance_students = []
#     for stud in students:
#         # return "HELLO WORLD"
#         if stud["grade"] == "A":
#             advance_students.append(stud)
#     return jsonify(advance_students)


# @app.route('/api/v1//student_names', methods=['GET'])  # GET PUT POST DELETE
# def get_student_names():
#     student_names = []
#     for stud in students:
#         # return "HELLO WORLD"
#         student_names.append(
#             f"first_name: {stud['first_name']}, last_name: {stud['last_name']}")
#     return jsonify(student_names)


# @app.route('/api/v1//student_ages', methods=['GET'])  # GET PUT POST DELETE
# def get_student_agess():
#     student_ages = []
#     for stud in students:
#         # return "HELLO WORLD"
#         student_ages.append(
#             f"first_name: {stud['first_name']}, last_name: {stud['last_name']}, age: {stud['age']}")
#     return jsonify(student_ages)


# app.run(port=8000,
#         debug=True)
# # app.run( debug=True)
