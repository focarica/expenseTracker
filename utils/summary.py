from utils.jsonFunctions import loadExpenses
from datetime import datetime
import calendar

def summaryExpenses(month: int | None) -> int:
    if month <= 0 or month > 12:
        return "Please add a number corresponding to one of the months of the year."
    
    expenses = loadExpenses()
    
    if(not month):
        return f"Total expenses: ${sum([i["amount"] for i in expenses])}"
    else:
        sumExpensesMonth = sum([i["amount"] for i in expenses if datetime.strptime(i["date"], "%d-%m-%Y").month == month])
        return f'Total expenses for {calendar.month_name[month]}: ${sumExpensesMonth}'
        