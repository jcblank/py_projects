contacts = {
    "number":4,
    "students": 
                [
                    {"name":"Joao Carlos", "email":"jcarlos.x@gmail.com"},
                    {"name":"Charles Brown", "email":"brown@gmail.com"},
                    {"name":"Antony Josh", "email":"joshua@gmail.com"}
                ] 
}

for student in contacts["students"]:
    print("The student", student["name"],"has the email address", student["email"],".")