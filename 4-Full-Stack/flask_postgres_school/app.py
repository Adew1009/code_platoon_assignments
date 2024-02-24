from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://andrew-dew:"password"@localhost/school2'

db = SQLAlchemy(app)


# Define the association table for the many-to-many relationship between students and subjects
# students_subjects_association = db.Table('students_subjects',
# db.Column('student_id', db.Integer, db.ForeignKey('Student.id')),
# db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
# )

# # Define the association table for the many-to-many relationship between teachers and subjects
# teachers_subjects_association = db.Table('teachers_subjects',
# db.Column('teacher_id', db.Integer, db.ForeignKey('Teachers.id')),
# db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
# )
# Class for subjects


class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(10))


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

@app.route('/api/v1/students/', methods=['GET'])
def get_student():
    all_students =  Student.query.all()
    json_students = [{"id": stud.id, "first_name": stud.first_name,
                      "last_name": stud.last_name, "age": stud.age, "subject": stud.subject} for stud in all_students]
    response = (jsonify(json_students))
    return response


#Class for teachers table
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(10))

@app.route('/api/v1/teachers/', methods=['GET'])
def get_teachers():
    all_teachers = Teachers.query.all()
    json_teachers = [{"id": teach.id, "first_name": teach.first_name,
                  "last_name": teach.last_name, "age": teach.age,
                  "subject": teach.subject} for teach in all_teachers]
    response = (jsonify(json_teachers))
    return response




#Uses port=8000 due to OS conlfict
app.run(port=8000, debug=True)


# http://127.0.0.1:8000/api/v1/subjects/
# http://127.0.0.1:8000/api/v1/teachers/
# http://127.0.0.1:8000/api/v1/students/