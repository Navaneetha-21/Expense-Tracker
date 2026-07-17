from django.db import models


class Expense(models.Model):
    class Category(models.TextChoices):
        Food = "Food" , "Food"
        Transport = "Transport" ,"Transport"
        shopping = "Shopping" , "Shopping"
        Health = "Health" , "Health"
        Home = "Home" , "Home"
        College = "College" , "College"
        Other = "Other" , "Other"


    description = models.CharField(max_length=100,null=False)
    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(
        max_length=100,
        choices=Category.choices,
        default=Category.Food
    )

    

    def __str__(self):
        return self.description