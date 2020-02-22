from django.shortcuts import render
from features.models import details1
from django.http import HttpResponse
from django.contrib import messages
def gasfilling(request):
	return render(request,'gas.html')
def dust(request):
	return render(request,'dust.html')
def installation(request):
	return render(request,'installation.html')
def repair(request):
	return render(request,'ac-repair.html')
def fillter(request):
	return render(request,'filter.html')
def compressor(request):
	return render(request,'compressor.html')

def customer_details(request):
	try:
		name1=request.POST.get("name",None)
		email1=request.POST.get("email",None)
		mobile1=request.POST.get("mobile",None)
		order1=request.POST.get("order",None)
		actype1=request.POST.get("actype")
		address1=request.POST.get("address",None)
	
		a=details1(name1=name1,email1=email1,mobile1=mobile1,order1=order1,actype1=actype1,address1=address1)
	
		a.save()
		success=True
		messages.success(request,'your information is successully saved. We will follow you soon.')
		showing=details1.objects.all()
	
		return render(request,'service.html',{'showing':showing,
										'success':success})
	except:
		success=False
		messages.error(request,"your information is not successfully saved.")
		return render(request,'service.html',{
										'success':success})	
	
	
