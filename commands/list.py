from utils.jsonFunctions import loadExpenses
from datetime import datetime, date

def __printList(expenses: list) -> None:
    for expense in expenses:
        listString = f"{expense["id"]}\t\t {expense["date"]}\t"
        
        if(len(expense["description"]) > 10):
            listString += f" {expense["description"][:10]}...\t\t {expense["amount"]}"
        else:
            listString += f" {expense["description"]}\t\t\t {expense["amount"]}"
            
        print(listString)


def listExpenses(month: int | None) -> None:
    expenses = loadExpenses()
    
    print(f"ID\t\t DATE\t\t DESCRIPTION\t\t AMOUNT")    
    
    if(not month):
        __printList(expenses=expenses)
    else:
        #Filter list view by month too
        filteredExpenses = [i for i in expenses if datetime.strptime(i["date"], "%d-%m-%Y").month == month]
        
        __printList(expenses=filteredExpenses)
            