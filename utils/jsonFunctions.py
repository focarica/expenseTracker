import json

def loadExpenses():
    try:
        with open("MyExpense.json", 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        file = open("MyExpense.json", 'x')
        file.close() 
        
        return []
    
def writeExpense(expense: dict):
    with open("MyExpense.json", 'w') as file:
        json.dump(expense, file, indent=4, ensure_ascii=False)