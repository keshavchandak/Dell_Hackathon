from django import forms
from django.db.models import DateField

class BankForm(forms.Form):
    name=forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'placeholder':'Shreyangi Prasad','name':'name' }))
    cardNo=forms.IntegerField()
    date=forms.DateField(input_formats='%m/%d/%y')
    cvv=forms.IntegerField()
