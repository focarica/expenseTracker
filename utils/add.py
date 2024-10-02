from utils.jsonFunctions import loadExpenses, writeExpense


# remake
def isInExpenses(description: str, expenses: list) -> int | None:
    for i in range(len(expenses)):
        if expenses[i]["description"] == description:
            return i
    return None

def addExpense(description: str, amount: int) -> str:
    ret = ""
    
    if amount < 0:
        return "Plese add a valid amount."
    if description == '':
        return "Please add a valid description"
    
    
    expenses = loadExpenses()
    
    idExpenseAlreadyAdd = isInExpenses(description=description, expenses=expenses)

    newExpense = {"id": '''to make''', "description":description, "amount": amount}
    
    if(idExpenseAlreadyAdd):
        expenses.remove('''to make''')
        expenses.insert(idExpenseAlreadyAdd+1, newExpense)    
        
        ret = f"Updated amount of {description} expense."
    else:
        expenses.append(newExpense)            
        ret = f"Added new expense with id {'''to make'''}."
        
    writeExpense(expense=expenses)
    return ret