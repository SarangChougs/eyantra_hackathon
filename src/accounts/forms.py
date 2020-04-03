from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

# User login form
class UserLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class':'form-control form-control-user',
            'placeholder':'Enter username',
        }
        ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control form-control-user',
            'placeholder': 'Enter password',
        }
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
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email address')
    password = forms.CharField(widget = forms.PasswordInput ,label = 'password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'confirm password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password must match ')
        email_qs = User.objects.filter(email = email)
        if email_qs.exits():
            raise forms.ValidationError("This email is already being used")
        return email