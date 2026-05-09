from models import Transaction
from database import Database

class ExpenseTracker:
    def __init__(self):
        self.db=Database()

    def add_expense(self,t):
        self.db.add_transaction(t)

    def view_all(self):
        result = self.db.get_all_transactions()
        return result
    
    def delete_expenses(self,d):
        self.db.delete_expense(d)
    

tracker = ExpenseTracker()
t=Transaction(200,"Food","Lunch",None,100)
tracker.add_expense(t)
data =tracker.view_all()
for  i  in data:
    print(i)
