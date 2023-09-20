import csv
import ast
from user import get_users
from collections import defaultdict

def show_status():
    users = get_users()
    user_paybacks = {}
    for user in users:
        # {user: [{amount, payback_user}, ...], ...}
        user_paybacks[user['username']] = []

    with open('expense_report.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            expense = ast.literal_eval(row[0])
            spender = expense['spender']
            
            for payback in expense['payback']:
                for user, payback_list in user_paybacks.items():
                    if user == payback['user']:
                        if len(payback_list) != 0:
                            for pay in payback_list:
                                if pay['payback_user'] == spender:
                                    pay['amount'] += payback['payback_amount']
                        elif user != spender:
                            payback_list.append({'amount': payback['payback_amount'], 'payback_user': spender})

    print(user_paybacks)
    for user, paybacks in user_paybacks.items():
        if paybacks:
            for payback in paybacks:
                amount = payback['amount']
                payback_user = payback['payback_user']
                print(f"{user} owes {amount:.2f}€ to {payback_user}.")
        else:
            print(f"{user} owes nothing.")
