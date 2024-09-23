import datetime
import json

def addExpense(description: str, amount: int) -> str:
    if amount < 0:
        return "Plese add a valid amount."
    if description == '':
        return "Please add a valid description"
    
    
    with open('MyExpenses.json', 'a') as file:
        json.dump(
            {"description": description,
            "amount": amount},
            file,
            indent=4,
        )