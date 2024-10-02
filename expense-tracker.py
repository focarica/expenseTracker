from utils.add import addExpense
from utils.list import listExpenses

import argparse

parser = argparse.ArgumentParser(
    prog='expense-tracker'
)

subparsers = parser.add_subparsers(dest='command')

# commands
 
addParser = subparsers.add_parser('add', help='Add a new expense.')
addParser.add_argument('--description', 
                       type=str, 
                       required=True,
                       help='Description of the new expense.')

addParser.add_argument('--amount', 
                       type=int, 
                       required=True,
                       help='Amount of the new expense.')


listParser = subparsers.add_parser('list', help='List all expenses.')
listParser.add_argument('--month',
                        type=int,
                        help="Filter list to a specific month")

summaryParser = subparsers.add_parser('summary', help='Summary of all expenses.')
summaryParser.add_argument('--month',
                           type=int,
                           help="Filter summary to a specific month")


deleteParser = subparsers.add_parser('delete', help='Delete a expense.')
deleteParser.add_argument('--id',
                          type=int,
                          help='Id of expense to delete.')

args = parser.parse_args()

match args.command:
    case 'add':
        print(addExpense(description=args.description, amount=args.amount))
    case 'list':
        listExpenses(month=args.month)
    case 'summary':
        pass
    case 'delete':
        pass