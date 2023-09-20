import csv
import ast

def show_status():
    user_balances = {}

    # Read expenses data from a CSV file
    with open('expense_report.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            expense = ast.literal_eval(row[0])
            spender = expense['spender']
            
            user_balances[spender] = user_balances.get(spender, 0) + float(expense['amount'])
            
            # Subtract the payback amounts from the balances of users involved in paybacks
            for payback in expense.get('payback', []):
                user = payback['user']
                payback_amount = float(payback['payback_amount'])
                user_balances[user] = user_balances.get(user, 0) - payback_amount

    # Generate the status report
    for user, balance in user_balances.items():
        if balance > 0:
            print(f"{user} owes {balance:.2f}€ to others.")
        else:
            print(f"{user} owes nothing.")
