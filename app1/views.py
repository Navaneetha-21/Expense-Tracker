from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ExpenseForm
from . models import Expense
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    print(request.user)
    print(request.user.is_authenticated)

    expenses = Expense.objects.all()

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = ExpenseForm()

    category = request.GET.get("category")

    if category:
        expenses = expenses.filter(category=category)


    context = {
        'form':form,
        'expenses':expenses
    }


    return render(request,'app1/index.html',context)


def delete_expense(request,expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method =="POST":
        expense.delete()
        return redirect('home')

    context ={
        'expense' : expense
    }
    return render(request,'app1/delete.html',context)




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

    return render(request,'app1/update.html',context)



def analysis(request):
    return render(request,'app1/analysis.html')





    

