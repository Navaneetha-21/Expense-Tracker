from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required



def register_view(request):
    context = {
        "errors":[],
    }

    if request.method=="POST":
        username = request.POST.get("username")
        email =request.POST.get("email")
        password=request.POST.get("pass1")
        confirm_password =request.POST.get("pass2")

        if password != confirm_password:
            context['errors'].append("Password Do Not Matching!!")

        if User.objects.filter(username=username).exists():
            context['errors'].append("USER ALREADY EXISTS!!")

        temp_user =User(username=username,password=password)

        try:
            validate_password(password=password,user=temp_user)
        except ValidationError  as err:
            context['errors'].extend(err.messages)

        if not context['errors']:
            user =User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            login(request,user)
            return redirect('home')

    return render(request,'account/register.html',context)


def login_view(request):
    context = {
        'errors':[],
    }

    if request.method=="POST":
        username= request.POST.get("username")
        password =request.POST.get("pass1")

        user =authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['errors'] = "Invalid Credentials"

    return render(request,'account/login.html',context)



def logout_view(request):
    if request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login')
