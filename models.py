from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
        
        amount : int
        category : str
        description : str
        date : str = None
        id : int=None

        def __post_init__(self):
                if self.date is None:
                    self.date=datetime.today().strftime("%Y-%m-%d")


        def __str__(self):
               return f"[{self.date}] | {self.category} | {self.description} | ${self.amount}"

# t=Transaction(200,"Food","Lunch")


