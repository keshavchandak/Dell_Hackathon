from django.shortcuts import render,redirect

from .models import First,Inventory
from .forms import BankForm
# Create your views here.

def index(request):
	context = {}
	return render(request, 'first/index.html', context)

def bank(request,model_no):
	model=Inventory.objects.get(model_No=model_no)
	print(model.model_price)

	form=BankForm()
	context={'form':form}
	return render(request,'first/bank.html',context)

def getBankData(request):
	form=BankForm(request.POST)
	print(request.POST['name'])

	return redirect('index')
