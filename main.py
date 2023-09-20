from PyInquirer import prompt
from examples import custom_style_2
from expense import new_expense
from user import add_user

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_option",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_option']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_option']) == "New User":
        add_user()
        ask_option()

def main():
    ask_option()

main()