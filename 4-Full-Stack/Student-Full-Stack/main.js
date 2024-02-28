const getSubjects = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/subjects/")
    let subjects = await response.json()
    console.log(subjects)
    subjects.map((subject) => {
        createItem(subject, "subjectContainer", `ID: ${subject['id']} | Subject: ${subject.subject}`)
    })
}

const addSubject = (event) => {
    event.preventDefault()
    let data = new FormData(event.target)
    let formattedData = Object.fromEntries(data)
    createItem(createItem(formattedData, "subjectContainer", `ID: ${formattedData['id']}`))
    getElementById('form').reset()
}

const getTeachers = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/teachers/")
    let teachers = await response.json()
    console.log(teachers)
    teachers.map((teacher) => {
        createItem(teacher, "teacherContainer", `ID: ${teacher['id']} | Name: ${teacher.first_name} ${teacher.last_name} | Age: ${teacher.age} | Subject: ${teacher.subject} | Students: ${teacher.students}`)
    })
}

const addTeacher = (event) => {
    event.preventDefault()
    let data = new FormData(event.target)
    let formattedData = Object.fromEntries(data)
    createItem(createItem(formattedData, "teacherContainer", `ID: ${formattedData['id']} | Name: ${formattedData.first_name} ${formattedData.last_name} | Age: ${formattedData.age} | Subject: ${formattedData.subject} | Students: ${formattedData.students}`))
    getElementById('form').reset()
}

const createItem = (unit, container, dataSet) => {
    let itemContainer = document.getElementById(container)
    let li = document.createElement('li')
    li.innerText = dataSet
    li.addEventListener('mouseover', (event) => {
        event.target.style.backgroundColor = 'yellow'
        event.target.style.fontSize = '20px'
        event.target.style.width = '40%'
    })
    li.addEventListener('mouseout', (event) => {
        event.target.style.backgroundColor = null
        event.target.style.fontSize = null
    })
    li.addEventListener('click', (event) => {
        if (event.target.style.textDecoration === 'line-through'){
            event.target.style.textDecoration = 'none'
        } else {
            event.target.style.textDecoration = 'line-through'
        }
    })
    itemContainer.appendChild(li)
}

const addStudent = (event) => {
    event.preventDefault()
    let data = new FormData(event.target)
    let formattedData = Object.fromEntries(data)
    createItem(formattedData, studentContainer, `ID: ${formattedData.id} | Name: ${formattedData.first_name} ${formattedData.last_name} | Age: ${formattedData.age} | Class: ${formattedData.class} | Teacher: ${formattedData.teacher}`)
    getElementById('form').reset()
}

const getStudents = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/students/")
    let students = await response.json()
    console.log(students)
    students.map((stud) => {
        // let {id, first_name, last_name, age, grade} = stud
        createItem(stud, "studentContainer", `ID: ${stud.id} | Name: ${stud.first_name} ${stud.last_name} | Age: ${stud.age} | Class: ${stud.class["subject"]} | Teacher: ${stud.class["teacher"]}`)
    })
}

