import datetime

from utils.jsonFunctions import loadExpenses, writeExpense


'''def isInExpenses(description: str, expenses: list) -> int | None:
    for expense in expenses:
        if description == expense["description"]:
            return expense['id'] - 1

    return None'''

def addExpense(description: str, amount: int) -> str:
    if amount < 0:
        return "Plese add a valid amount."
    if description == '':
        return "Please add a valid description"
    
    
    expenses = loadExpenses()
    # idAlreadyInExpenses = isInExpenses(description=description, expenses=expenses)
    
    expenses.append(
        {"id":len(expenses)+1, 
         "description":description, 
         "amount": amount})
    
    writeExpense(expense=expenses)
    
    return f"Added new expense with id {len(expenses)}."