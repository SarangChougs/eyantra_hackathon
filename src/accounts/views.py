from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    error = 'none'
    next = request.GET.get('next')

    # if the request is post we need to process the form data
    if request.method == 'POST':
        error = 'Request is post'
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
            error = 'Please Provide valid data'
    #if get or any other request is passed create a blank form
    else:
        form = UserLoginForm()
        error = 'Request is not post'

    context = {
        'form': form,
        'error': error
    }
    return render(request, "login.html", context)
