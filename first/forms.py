from django import forms
from django.db.models import DateField

class BankForm(forms.Form):
    name=forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'name':'name' }))
    cardNo=forms.IntegerField()
    date=forms.DateField( input_formats='%m/%d/%y')
    cvv=forms.IntegerField(widget=forms.PasswordInput(), min_value = 100, max_value = 999)

class SecurityForm(forms.Form):
    name_school=forms.CharField(max_length=30)
    mother_name=forms.CharField(max_length=30)
    first_car=forms.CharField(max_length=30)

class OTP(forms.Form):
	otp = forms.IntegerField(min_value = 100000, max_value = 999999)
	password = forms.CharField(max_length=8, widget=forms.PasswordInput)
