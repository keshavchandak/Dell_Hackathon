from django.shortcuts import render

from .models import First,Inventory
# Create your views here.

def index(request):
	context = {}
	return render(request, 'first/index.html', context)

def bank(request,model_no):
	model=Inventory.objects.get(model_No=model_no)
	print(model.model_price)
	context={}
	return render(request,'first/bank.html',context)
