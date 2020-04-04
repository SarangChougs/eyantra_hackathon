from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#homepage
@login_required
def homepage(request):
    return render(request, 'index.html')

def relativeView(request):
    return render(request, 'relative.html')

def doctorView(request):
    return render(request, 'doctor.html')

def reportView(request):
    return render(request, 'report.html')