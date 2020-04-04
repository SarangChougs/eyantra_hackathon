from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .forms import UserLoginForm, CreateUserForm
from django.contrib import messages

def login_view(request):
    next = request.GET.get('next')

    # if the request is post we need to process the form data
    if request.method == 'POST':
        #instantiate the userlogin form and populate it with the data from the request
        form = UserLoginForm(request.POST or None)
        #check whether it is a valid form
        if form.is_valid():
            #get the cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #authenticate the user
            user = authenticate(username = username, password = password)
            #if the user is valid then log him in
            login(request, user)
            # if next was present in the request then redirect it to the next
            if next:
                return redirect(next)
            return redirect('/')
        else:
            messages.error(request, form.errors)
    #if get or any other request is passed create a blank form
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'form_errors': form.errors
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

def registration_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = CreateUserForm()

    context ={
        'form':form
    }
    return render(request, "register.html", context)

def forgotPasswordView(request):
    return render(request, "forgot-password.html")

def profileView(request):
    return render(request, "profile.html")