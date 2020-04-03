from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#homepage
@login_required
def homepage(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def forgotPassword(request):
    return render(request, 'forgot-password.html')