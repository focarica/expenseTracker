from commands.add import addExpense
from commands.list import listExpenses
from commands.summary import summaryExpenses
from commands.delete import deleteExpense

from utils.args import commands

args = commands()

match args.command:
    case 'add':
        print(addExpense(description=args.description, amount=args.amount))
    case 'list':
        listExpenses(month=args.month)
    case 'summary':
        print(summaryExpenses(month=args.month))
    case 'delete':
        print(deleteExpense(id=args.id))