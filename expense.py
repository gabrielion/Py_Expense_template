from PyInquirer import prompt
from user import get_users
import csv

users = get_users()
amount_question = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
]
label_question = [
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]

spender_question = [
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": [user['username'] for user in users]
    },
]


def new_expense(*args):
    amount = prompt(amount_question)
    
    label = prompt(label_question)
    spender = prompt(spender_question)
   
    involved_question = [
        {
            "type":"checkbox",
            "name":"involved_users",
            "message":"New Expense - involve users: ",
            "choices": [{'name': user["username"], 'checked': True if user["username"] == spender['spender'] else False } for user in users]
        },
    ]
    involved_users = prompt(involved_question)
    print(involved_users)
    paybacks = []
    for user in involved_users['involved_users']:
        if user != spender['spender']:
            payback_amount = float(amount['amount']) / len(involved_users)
            payback_dict = {
                'user' : user,
                'payback_amount': payback_amount,
                'payback_person': spender['spender']
            }
            paybacks.append(payback_dict)

    infos = {**amount, **label, **spender, **{'payback': paybacks}}
    print(infos)

    with open('expense_report.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([infos])
    print("Expense Added !")

    return True
