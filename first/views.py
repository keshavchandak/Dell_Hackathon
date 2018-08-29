from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.http import require_POST

from .models import First,Inventory
from .forms import BankForm, SecurityForm ## LoginForm,RegisterForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
	#loginform= LoginForm()
	#registerlogin=RegisterForm()
	context = {}
	return render(request, 'first/index.html', context)

def bank(request,model_no):
	model=Inventory.objects.get(model_No=model_no)
	print(model.model_price)

	form=BankForm()
	context={'form':form,'model':model}
	return render(request,'first/bank.html',context)

@require_POST
def getBankData(request):
	form=BankForm(request.POST)
	print(request.POST['cvv'])
	if int(request.POST['cvv'])==513:
		return redirect('security')
	else:
		return HttpResponse('The CVV number does not match with Card Number')

def email():
	send_mail('Hello from Kshitij',
	'Hello There, This is an automatic message from Kshitij Srivastava. If you have recieved this message then Email service is working :)',
	'guadalupe.wagner@lcelandic.com',['woji@hurify1.com'])

def thankyou(request):
	#email()
	return render(request,'first/thankyou.html')

#While going to the security page the object which is to be bought is lost

@require_POST
def getSecurityData(request):
	form=SecurityForm(request.POST)
	if request.POST['name_school']=='dps' and request.POST['mother_name']=='gita' and request.POST['first_car']=='nano':
		return redirect('thankyou')
	else:
		return HttpResponse("Security Question is wrongly answered")

def securitypage(request):
	form=SecurityForm()
	context={'form':form}
	return render(request,'first/security.html',context)


def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username, password=password)
			login(request,user)
			return redirect('index')
	else:
		form=UserCreationForm()
	context={'form':form}
	return render(request,'registration/register.html',context)


""" To be used in Order Number formation
import uuid

Returns a random string of length string_length
def my_random_string(string_length=10):
	random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	random = random.upper() # Make all characters uppercase.
	random = random.replace("-","") # Remove the UUID '-'.
	return random[0:string_length] # Return the random string.

print(my_random_string(6)) # For example, D9E50C

"""

	# def alternatelogin(request):
	# 	return True
	#
	# def alternateregister(request):
	# 	return True
