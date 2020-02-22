from django.shortcuts import HttpResponseRedirect
from django.urls import resolve
def login_register(get_response):
	def fun(request):
		url_name=resolve(request.path_info).url_name
		if url_name=='Logout' and request.user.is_authenticated:
			response=HttpResponseRedirect('http://localhost:8000/service/')
			#response=get_response(request)
		else:
			response=get_response(request)
		return response
	return  fun