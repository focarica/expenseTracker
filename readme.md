# Expense Tracker

Sample solution for the [expense-tracker](https://roadmap.sh/projects/expense-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## How to run

Clone the repository and run the following command:

```bash
git clone https://github.com/focarica/expenseTracker.git
cd /expenseTracker


To run the project, just:

```bash
python3 expenseTracker.py add --description "Lunch" --amount 20 # Add an expense
python3 expenseTracker.py add --description "Dinner" --amount 10 # Add another expense
python3 expenseTracker.py list # List all expenses 
python3 expenseTracker.py list --month 8 # List all expenses for specific month
python3 expenseTracker.py summary # Show summary of expenses
python3 expenseTracker.py summary --month 8 # Show summary of expenses for specific month
python3 expenseTracker.py delete --id 1 # Delete an expense by ID
