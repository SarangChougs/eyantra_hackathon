from django.shortcuts import render


#homepage
def homepage(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def forgotPassword(request):
    return render(request, 'forgot-password.html')