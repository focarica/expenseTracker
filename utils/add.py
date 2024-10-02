from utils.jsonFunctions import loadExpenses, writeExpense

    
def addExpense(description: str, amount: int) -> str:
    if amount < 0:
        return "Plese add a valid amount."
    if description == '':
        return "Please add a valid description"
    
    
    expenses = loadExpenses()
    newExpense = {"id": -1, "description":description, "amount": amount}
    
    if(len(expenses) == 0):
        newExpense["id"] = 1
    else:
        newExpense["id"] = expenses[-1]["id"]+1
               
    expenses.append(newExpense)            
        
    writeExpense(expense=expenses)
    return f"Added new expense with id {newExpense["id"]}."