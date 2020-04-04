from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# User login form
class UserLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        # attrs = {
        #     'class':'form-control form-control-user',
        #     'placeholder':'Enter username',
        # }
        ))
    password = forms.CharField(widget = forms.PasswordInput(
        # attrs = {
        #     'class': 'form-control form-control-user',
        #     'placeholder': 'Enter password',
        # }
    ))

    #this method is applied every time the form is submitted 
    #this method ensures that the data being sent by the form is the data that we need
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist.')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

# User signup form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']