from django import forms
from django.db.models import DateField

class BankForm(forms.Form):
    name=forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'name':'name' }))
    cardNo=forms.IntegerField()
    date=forms.DateField(input_formats='%m/%d/%y')
    cvv=forms.CharField(widget=forms.PasswordInput)

class SecurityForm(forms.Form):
    name_school=forms.CharField(max_length=10)
    mother_name=forms.CharField(max_length=10)
    first_car=forms.CharField(max_length=10)

# class LoginForm(forms.Form): #Alternate Login
#     user_name=forms.CharField(max_length=10)
#     password=forms.CharField(max_length=10)
#
# class RegisterForm(forms.Form): #Alternate Register
#     user_name=forms.CharField(max_length=10)
#     password=forms.CharField(max_length=10)
