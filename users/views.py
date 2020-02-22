from django.shortcuts import render
from users.form import signupform
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.test import Client
from users.decorator import login_register_check


def logout_profile(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_register_check
def signup(request):
	registered=False
	if request.method=='POST':
		profile=signupform(request.POST)
		if profile.is_valid():
			user=profile.save()
			user.save()
			registered=True
		else:
			print(profile.errors)
	else:
		profile=signupform()

	return render(request,'registration.html',{'profile':profile,'registered':registered})
# Create your views here.
def login_profile(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("not inactive username and password")
		else:
			return HttpResponse("invalid username and password")
	else:
		return render(request,'login.html')



def test(self):
	c=Client()
	response=c.post('/signup/login/',{'username':'john','password':'smith1234'})
	response.status_code
	response=c.get('http://127.0.0.1:8000/')
	#response.content
	return HttpResponse(response.content)

