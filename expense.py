import json

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def display(self):
        print(f"{self.name}: {self.amount} ({self.category})")

    def to_dict(self):
        return{"name": self.name, "amount": self.amount, "category": self.category}

def add_expense(expenses, name, amount, category):
    expenses.append(Expense(name, amount, category))

def show_expenses(expenses):
    for i in expenses:
        i.display()

def total_expenses(expenses):
    total_amount = 0
    for i in expenses:
        total_amount += i.amount
    print(f"Total: ${total_amount:.2f}")

try:
    expenses = []
    with open("expense.json", "r") as file:
        for i in json.load(file):
            data = Expense(i["name"], i["amount"], i["category"])
            expenses.append(data)
except FileNotFoundError:
    expenses = []

while True:
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")
    action = input("Enter an action: ")

    if action == "1":
        name = input("Enter name of expense: ")
        amount = float(input("Enter amount for expense: "))
        category = input("Enter category of expense: ")
        add_expense(expenses, name, amount, category)
    elif action == "2":
        show_expenses(expenses)
    elif action == "3":
        total_expenses(expenses)
    elif action == "4":
        data = []
        for e in expenses:
            data.append(e.to_dict())

        with open("expense.json", "w") as file:
            json.dump(data, file)
        break
    else:
        print("Error")




