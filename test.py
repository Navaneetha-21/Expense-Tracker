from database import Database
from models import Transaction

db = Database()
t=Transaction(200,"Food","Lunch")
db.add_transaction(t)
tt = db.get_all_transactions()
for i in tt:
    print(i)    