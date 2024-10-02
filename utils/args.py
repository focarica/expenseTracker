import argparse


def commands():
    parser = argparse.ArgumentParser(
        prog='expense-tracker'
    )

    subparsers = parser.add_subparsers(dest='command')

    
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
                            required=True,
                            help='Id of expense to delete.')

    return parser.parse_args()