from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://andrew-dew:"password"@localhost/school2'

db = SQLAlchemy(app)

student_data = [
    {
        "age": 32,
        "first_name": "David",
        "id": 1,
        "last_name": "Miller",
        "subject": 3
    },
    {
        "age": 28,
        "first_name": "Sarah",
        "id": 2,
        "last_name": "Johnson",
        "subject": 1
    },
    {
        "age": 35,
        "first_name": "Robert",
        "id": 3,
        "last_name": "Williams",
        "subject": 4
    },
    {
        "age": 30,
        "first_name": "Emily",
        "id": 4,
        "last_name": "Anderson",
        "subject": 5
    },
    {
        "age": 29,
        "first_name": "Michael",
        "id": 5,
        "last_name": "Smith",
        "subject": 4
    },
    {
        "age": 31,
        "first_name": "Olivia",
        "id": 6,
        "last_name": "Johnson",
        "subject": 5
    },
    {
        "age": 27,
        "first_name": "Matthew",
        "id": 7,
        "last_name": "Brown",
        "subject": 3
    },
    {
        "age": 29,
        "first_name": "John",
        "id": 8,
        "last_name": "Doe",
        "subject": 1
    },
    {
        "age": 30,
        "first_name": "Laura",
        "id": 9,
        "last_name": "Clark",
        "subject": 2
    },
    {
        "age": 33,
        "first_name": "Rebecca",
        "id": 10,
        "last_name": "Wilson",
        "subject": 2
    },
    {
        "age": 31,
        "first_name": "Chris",
        "id": 11,
        "last_name": "Evans",
        "subject": 1
    },
    {
        "age": 29,
        "first_name": "Anna",
        "id": 12,
        "last_name": "Robinson",
        "subject": 1
    },
    {
        "age": 34,
        "first_name": "James",
        "id": 13,
        "last_name": "Moore",
        "subject": 5
    },
    {
        "age": 28,
        "first_name": "Elizabeth",
        "id": 14,
        "last_name": "White",
        "subject": 3
    },
    {
        "age": 30,
        "first_name": "William",
        "id": 15,
        "last_name": "Harris",
        "subject": 5
    },
    {
        "age": 32,
        "first_name": "Julia",
        "id": 16,
        "last_name": "Lewis",
        "subject": 4
    },
    {
        "age": 29,
        "first_name": "Daniel",
        "id": 17,
        "last_name": "Turner",
        "subject": 3
    },
    {
        "age": 35,
        "first_name": "Grace",
        "id": 18,
        "last_name": "Parker",
        "subject": 4
    },
    {
        "age": 28,
        "first_name": "Charles",
        "id": 19,
        "last_name": "Bennett",
        "subject": 2
    },
    {
        "age": 30,
        "first_name": "Sophia",
        "id": 20,
        "last_name": "Wright",
        "subject": 1
    }
]
teacher_data = [
    {
        "age": 32,
        "first_name": "David",
        "id": 1,
        "last_name": "Miller",
        "subject": 1
    },
    {
        "age": 28,
        "first_name": "Sarah",
        "id": 2,
        "last_name": "Johnson",
        "subject": 2
    },
    {
        "age": 35,
        "first_name": "Robert",
        "id": 3,
        "last_name": "Williams",
        "subject": 3
    },
    {
        "age": 30,
        "first_name": "Emily",
        "id": 4,
        "last_name": "Anderson",
        "subject": 4
    },
    {
        "age": 29,
        "first_name": "Michael",
        "id": 5,
        "last_name": "Smith",
        "subject": 5
    }
]
subject_data = [
    {
        "id": 1,
        "subject": "Mathematics"
    },
    {
        "id": 2,
        "subject": "Science"
    },
    {
        "id": 3,
        "subject": "English"
    },
    {
        "id": 4,
        "subject": "History"
    },
    {
        "id": 5,
        "subject": "Physical Education"
    }
]



class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(10))

    # def subject_data():
    #     all_subjects = Subjects.query.all()
    #     json_subjects = [{"id": sub.id, "subject": sub.subject}
    #                     for sub in all_subjects]
    #     return json_subjects

@app.route('/api/v1/subjects/', methods=['GET'])
def get_subjects():
    all_subjects = Subjects.query.all()
    json_subjects = [{"id": sub.id, "subject": sub.subject}
                     for sub in all_subjects]
    response = (jsonify(json_subjects))
    return response
 

#Class for student table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    # db.relationship('Subject', secondary=students_subjects_association, backref='students')#db.Column(db.String(10))

    # def student_data():
    #     all_students =  Student.query.all()
    #     json_students = [{"id": stud.id, "first_name": stud.first_name,
    #                     "last_name": stud.last_name, "age": stud.age, "subject": stud.subject} for stud in all_students]
    #     return json_students

@app.route('/api/v1/students/', methods=['GET'])
def get_student():
    all_students =  Student.query.all()
    for stud in all_students:
        for subs in subject_data:
            if subs["id"]==stud.subject:
                subject = (subs["subject"])
    for teach in teacher_data:
        if teach["subject"]==stud.subject:
            teacher =(f"{teach['first_name']} {teach['last_name']}")            
        json_students = [{
            "id": stud.id, 
            "first_name": stud.first_name,
            "last_name": stud.last_name, 
            "age": stud.age, 
            "class": {"subject": subject, "teacher": teacher }}for stud in all_students]
    # response = (jsonify(json_students))
    response = (json_students)
    return response



#Class for teachers table
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(10))
    
    # def teacher_data():
    #     all_teachers = Teachers.query.all()
    #     json_teachers = [{"id": teach.id, "first_name": teach.first_name,
    #                     "last_name": teach.last_name, "age": teach.age,
    #                     "subject": teach.subject} for teach in all_teachers]
    #     return json_teachers

@app.route('/api/v1/teachers/', methods=['GET'])
def get_teachers():
    all_teachers = Teachers.query.all()
    json_teachers = []
    for teach in all_teachers:
        for subs in subject_data:
            if subs["id"]==teach.subject:
                subject = (subs["subject"])
        studentlist = []
        for stud in student_data:
                if stud["subject"]==teach.subject:
                    studentlist.append(f"{stud['first_name']} {stud['last_name']}")
        teachers = {
            "first_name": teach.first_name, 
            "last_name": teach.last_name, 
            "age": teach.age, 
            "subject": subject, "students": studentlist}
        json_teachers.append(teachers)
        studentlist = []
    response = (jsonify(json_teachers))
    return response  


# student_data = [
#     {
#         "age": 32,
#         "first_name": "David",
#         "id": 1,
#         "last_name": "Miller",
#         "subject": 3
#     },
#     {
#         "age": 28,
#         "first_name": "Sarah",
#         "id": 2,
#         "last_name": "Johnson",
#         "subject": 1
#     },
#     {
#         "age": 35,
#         "first_name": "Robert",
#         "id": 3,
#         "last_name": "Williams",
#         "subject": 4
#     },
#     {
#         "age": 30,
#         "first_name": "Emily",
#         "id": 4,
#         "last_name": "Anderson",
#         "subject": 5
#     },
#     {
#         "age": 29,
#         "first_name": "Michael",
#         "id": 5,
#         "last_name": "Smith",
#         "subject": 4
#     },
#     {
#         "age": 31,
#         "first_name": "Olivia",
#         "id": 6,
#         "last_name": "Johnson",
#         "subject": 5
#     },
#     {
#         "age": 27,
#         "first_name": "Matthew",
#         "id": 7,
#         "last_name": "Brown",
#         "subject": 3
#     },
#     {
#         "age": 29,
#         "first_name": "John",
#         "id": 8,
#         "last_name": "Doe",
#         "subject": 1
#     },
#     {
#         "age": 30,
#         "first_name": "Laura",
#         "id": 9,
#         "last_name": "Clark",
#         "subject": 2
#     },
#     {
#         "age": 33,
#         "first_name": "Rebecca",
#         "id": 10,
#         "last_name": "Wilson",
#         "subject": 2
#     },
#     {
#         "age": 31,
#         "first_name": "Chris",
#         "id": 11,
#         "last_name": "Evans",
#         "subject": 1
#     },
#     {
#         "age": 29,
#         "first_name": "Anna",
#         "id": 12,
#         "last_name": "Robinson",
#         "subject": 1
#     },
#     {
#         "age": 34,
#         "first_name": "James",
#         "id": 13,
#         "last_name": "Moore",
#         "subject": 5
#     },
#     {
#         "age": 28,
#         "first_name": "Elizabeth",
#         "id": 14,
#         "last_name": "White",
#         "subject": 3
#     },
#     {
#         "age": 30,
#         "first_name": "William",
#         "id": 15,
#         "last_name": "Harris",
#         "subject": 5
#     },
#     {
#         "age": 32,
#         "first_name": "Julia",
#         "id": 16,
#         "last_name": "Lewis",
#         "subject": 4
#     },
#     {
#         "age": 29,
#         "first_name": "Daniel",
#         "id": 17,
#         "last_name": "Turner",
#         "subject": 3
#     },
#     {
#         "age": 35,
#         "first_name": "Grace",
#         "id": 18,
#         "last_name": "Parker",
#         "subject": 4
#     },
#     {
#         "age": 28,
#         "first_name": "Charles",
#         "id": 19,
#         "last_name": "Bennett",
#         "subject": 2
#     },
#     {
#         "age": 30,
#         "first_name": "Sophia",
#         "id": 20,
#         "last_name": "Wright",
#         "subject": 1
#     }
# ]
# teacher_data = [
#   {
#     "age": 32,
#     "first_name": "David",
#     "id": 1,
#     "last_name": "Miller",
#     "subject": 1
#   },
#   {
#     "age": 28,
#     "first_name": "Sarah",
#     "id": 2,
#     "last_name": "Johnson",
#     "subject": 2
#   },
#   {
#     "age": 35,
#     "first_name": "Robert",
#     "id": 3,
#     "last_name": "Williams",
#     "subject": 3
#   },
#   {
#     "age": 30,
#     "first_name": "Emily",
#     "id": 4,
#     "last_name": "Anderson",
#     "subject": 4
#   },
#   {
#     "age": 29,
#     "first_name": "Michael",
#     "id": 5,
#     "last_name": "Smith",
#     "subject": 5
#   }
# ]
# subject_data = [
#   {
#     "id": 1,
#     "subject": "Mathematics"
#   },
#   {
#     "id": 2,
#     "subject": "Science"
#   },
#   {
#     "id": 3,
#     "subject": "English"
#   },
#   {
#     "id": 4,
#     "subject": "History"
#   },
#   {
#     "id": 5,
#     "subject": "Physical Education"
#   }
# ]




#Uses port=8000 due to OS conlfict
app.run(port=8000, debug=True)


# http://127.0.0.1:8000/api/v1/subjects/
# http://127.0.0.1:8000/api/v1/teachers/
# http://127.0.0.1:8000/api/v1/students/

# @app.route('/api/v1/teachers/', methods=['GET'])
# def get_teachers():
#     all_teachers = Teachers.query.all()
#     for subs in subject_data:
#         if subs["id"] == teach.subject:
#             subject = (subs["subject"])

#     def sub_students():
#         studentlist = []
#         for stud in student_data:
#             if stud["subject"] == teach.subject:
#                 studentlist.append(f"{stud['first_name']} {stud['last_name']}")
#         return studentlist
#     json_teachers = [{"first_name": teach.first_name, "last_name": teach.last_name,
#                       "age": teach.age, "subject": subject, "students": sub_students()} for teach in all_teachers]
#     response = (jsonify(json_teachers))
#     return response
