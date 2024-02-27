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

# json_students = [{ "class": {"subject": 1 subjectname, "teacher": teachername}}]
studentlist=[]
for stud in student_data:
            if stud["subject"]==1:
                studentlist.append(f"{stud['first_name']} {stud['last_name']}")

print(studentlist)