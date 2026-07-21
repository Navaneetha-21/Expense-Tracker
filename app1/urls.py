from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name='home'),
    path("delete/<int:expense_id>/",views.delete_expense,name="delete"),
    path("update/<int:expense_id>/",views.update_expense,name="update"),
    path("analysis/",views.analysis,name='analysis'), 
]