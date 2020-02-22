from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
def contact_us(request):
	return render(request,'contactus.html')
# Create your views here.
def sendfun(request):
	try:
		
		name=request.POST.get("fullname")
		email=request.POST.get("email")
		subject=request.POST.get("subject")
		message="Name=  "+name+"  Subject="+subject+"  Message="+request.POST.get("message")+"  Email="+email

		send_mail(subject,message,'from@ACweb',['nalam9257@gmail.com'],fail_silently=False,
		)
		messages.success(request,"Successfully send.")
		success=True
		return render(request,'contactus.html',{'success':success})
	except:
		success=False
		messages.error(request,"Failed",{'success':success})