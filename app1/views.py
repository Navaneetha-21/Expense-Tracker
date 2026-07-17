from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ExpenseForm
from . models import Expense

def home(request):

    expenses = Expense.objects.all()

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = ExpenseForm()



    context = {
        'form':form,
        'expenses':expenses
    }



    return render(request,'index.html',context)


def delete_expense(request,expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method =="POST":
        expense.delete()
        return redirect('home')

    context ={
        'expense' : expense
    }
    return render(request,'delete.html',context)




def update_expense(request,expense_id):
    expense = Expense.objects.get(id=expense_id)

    if request.method=="POST":
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ExpenseForm(instance=expense)

    context = {
        'expense':expense,
        'form':form,
    }

    return render(request,'update.html',context)

    

