from utils.jsonFunctions import loadExpenses, writeExpense


def __idExpense(id: int, expenses: list) -> int | None:
    try:
        return [i["id"] for i in expenses].index(id)
    except ValueError:
        return None


def deleteExpense(id: int) -> str:
    expenses = loadExpenses()
    id = __idExpense(id, expenses=expenses)

    if not id and id != 0:
        return "There is no expense with this ID."
    
    expenses.pop(id)
    writeExpense(expenses)
    
    return "Expense deleted successfully"