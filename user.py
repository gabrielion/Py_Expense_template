from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Name: ",
    }
]

def add_user():
    infos = prompt(user_questions)
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([infos['username']])
    # This function should create a new user, asking for its name
    return

def get_users():
    users = []

    with open('users.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                user = {"username": row[0].strip()}  # Assuming the username is in the first column
                users.append(user)

    return users
