from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from .models import First,Inventory
from .forms import BankForm
# Create your views here.

def index(request):
	context = {}
	return render(request, 'first/index.html', context)

#print the model name and number in the bank page

def bank(request,model_no):
	model=Inventory.objects.get(model_No=model_no)
	print(model.model_price)

	form=BankForm()
	context={'form':form}
	return render(request,'first/bank.html',context)

@require_POST
def getBankData(request):
	form=BankForm(request.POST)
	print(request.POST['cvv'])
	return redirect('index')


def thankyou(request):
	return render(request,'first/thankyou.html')

#While going to the security page the object which is to be bought is lost

def securitypage(request):
	return render(request,'first/security.html')
