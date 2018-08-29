from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import First,Inventory
from .forms import BankForm, SecurityForm, OTP
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.core.mail import EmailMultiAlternatives
import pickle
import csv
import numpy as np
# Create your views here.

dataset = 'sample.csv'
raw_data = open(dataset, 'rt')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
data_1 = np.array(x).astype('float')

def Naivebayes():
	num = [[x1, 20, 0, 0, 3461, 0, 1, 0]]
	features_test = np.array(num)

	filename_1 = 'naivebayes.sav'
	pickle_in_1 = open(filename_1, 'rb')
	loaded_model_1 = pickle.load(pickle_in_1)
	result_1 = int(loaded_model_1.predict(features_test))

	# raw_data.close()
	print("Naive Bayes Output: (if 0 -> extrinsic filter \n else if 1 -> Towards Extrinsic Filter) " , result_1)
	if(result_1 == 1):
		result_2 = Adaboost()
		print("AdaBoost Output: ", result_2)
		result_3 = Knn()
		print("Knn Output: ", result_3)
		result_4 = Logistic()
		print("Logistic Regression Output: ", result_4)
		if(result_2==1 and result_3==1):
			return 1
		elif(result_2==1 and result_4==1):
			return 1
		elif(result_3==1 and result_4==1):
			return 1
	else:
		return 0

def Adaboost():
	num = [[x1, 20, 0, 0, 3461, 0, 1, 0]]
	features_test = np.array(num)
	# dataset = 'sample.csv',
	# # raw_data = open(dataset, 'rt')
	# reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
	# x = list(reader)
	# data1 = np.array(x).astype('float')
	# features_test = data_1[4:5, 0:8]
	filename_2 = 'Adaboost.sav'
	pickle_in_2 = open(filename_2, 'rb')
	loaded_model_2 = pickle.load(pickle_in_2)

	result_2 = int(loaded_model_2.predict(features_test))
	print(result_2)
	return result_2

def Knn():
	num = [[x1, 20, 0, 0, 3461, 0, 1, 0]]
	features_test = np.array(num)
	# dataset = 'sample.csv'
	# raw_data = open(dataset, 'rt')
	# reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
	# x = list(reader)
	# data1 = np.array(x).astype('float')
	# features_test = data_1[4:5, 0:8]
	filename_3 = 'Knn.sav'
	pickle_in_3 = open(filename_3, 'rb')
	loaded_model_3 = pickle.load(pickle_in_3)
	result_3 = int(loaded_model_3.predict(features_test))
	print(result_3)
	return result_3

def Logistic():
	num = [[x1, 20, 0, 0, 3461, 0, 1, 0]]
	features_test = np.array(num)
	# dataset = 'sample.csv'
	# raw_data = open(dataset, 'rt')
	# reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
	# x = list(reader)
	# data1 = np.array(x).astype('float')
	filename_4 = 'Logistic.sav'
	pickle_in_4 = open(filename_4, 'rb')
	loaded_model_4 = pickle.load(pickle_in_4)
	result_4 = int(loaded_model_4.predict(features_test))
	print(result_4)
	return result_4

def index(request):
	context = {}
	return render(request, 'first/index.html', context)

@login_required
def bank(request,model_no):
	global x1
	model=Inventory.objects.get(model_No=model_no)
	print(model.model_price)
	x1 = int(model.model_price/70)
	form=BankForm()
	context={'form':form,'model':model}
	return render(request,'first/bank.html',context)

@require_POST
def getBankData(request):
	form=BankForm(request.POST)
	print(request.POST['cvv'])
	Naivebayes()
	if int(request.POST['cvv'])==513 and Naivebayes() == 0:
		return redirect('otp')
	else:
		return redirect('security')

def email():
	send_mail("Hello From Kshitij", "Hi, This is Kshitij. If you have recieved this message then email system works :)",
  "Kshitij Srivastava <kshitij127@yahoo.co.in>", ["ks435@snu.edu.in"])


def thankyou(request):
	if request.method=='POST':
		form = OTP(request.POST)
		if int(request.POST['otp']) == 123456:
			return render(request, 'first/thankyou.html')
		else:
			return render(request,'first/otp.html')
	else:
		return render(request,'first/thankyou.html')

# def thankyou(request):
# 	#`email()
# 	return render(request,'first/thankyou.html')

#While going to the security page the object which is to be bought is lost

@require_POST
def getSecurityData(request):
	form=SecurityForm(request.POST)
	if request.POST['name_school']=='dps' and request.POST['mother_name']=='gita' and request.POST['first_car']=='nano':
		return redirect('otp')
	else:
		return redirect('error')

def securitypage(request):
	form=SecurityForm()
	context={'form':form}
	return render(request,'first/security.html',context)

def otp(request):
	form=OTP()
	context={'form':form}
	return render(request, 'first/otp.html', context)

def error(request):
	return render(request, 'first/error.html')

def contact(request):
	return render(request, 'first/contactUs.html')

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

"""
import datetime
now = datetime.datetime.now()
str_now=str(now)
2017-12-29 11:24:48.042720
date_time_split=str_now.split(" ")
full_date=date_time_split[0].split("-")
full_time=date_time_split[1].split(":")
year=full_date[0]
month=full_date[1]
date=full_date[2]
hour=full_time[0]
minute=full_time[1]
"""
