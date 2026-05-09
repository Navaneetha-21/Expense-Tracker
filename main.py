from tracker import ExpenseTracker
from models import Transaction

# amount = float(input("Enter a Amount You Spent:"))
# category   = input("Enter a category:")
# description = input("Enter a Description:")

tracker = ExpenseTracker()
# t=Transaction(amount,category,description)
# tracker.add_expense(t)
# view_expense = tracker.view_all()
# for i in view_expense:
#     print(i)

while True:
    choice =int(input("Enter 1/2/3/4:"))

    if choice == 1:
        amount = float(input("Enter a Amount You Spent:"))
        category   = input("Enter a category:")
        description = input("Enter a Description:")

        t=Transaction(amount,category,description)
        tracker.add_expense(t)

    elif choice ==2:
        view_expense = tracker.view_all()
        for i in view_expense:
            print(i)
    elif choice==3:
        delete_item =input("Enter a Delete Item:")
        tracker.delete_expenses(delete_item)

    else:
        break
        


