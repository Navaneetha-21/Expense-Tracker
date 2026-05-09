import sqlite3
from models import Transaction

class Database:
    def __init__(self):
        self.db_path = "expenses.db"
        self._init_tables() 


    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    def _init_tables(self):
        with self._connect() as conn:
            conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT)
""")

    def add_transaction(self,txn):
        with self._connect() as conn:
            conn.execute("INSERT INTO transactions(amount,category,description,date) VALUES(?,?,?,?)",
                         (txn.amount,txn.category,txn.description,txn.date)
)
            
    
    def get_all_transactions(self):
        with self._connect() as conn:
            result =conn.execute(
                "SELECT * FROM transactions "

                
            )
        
        rows = result.fetchall()
        transcationss = []

        for i in rows:
            t=Transaction(i[1],i[2],i[3],i[4],i[0])
            transcationss.append(t)

        return transcationss
    
    def delete_expense(self,id_delete):
        with self._connect() as conn:
            conn.execute("DELETE FROM transactions WHERE id = ?",
            (id_delete,))





