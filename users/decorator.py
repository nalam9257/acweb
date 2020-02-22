from django.shortcuts import HttpResponseRedirect
def login_register_check(fun):
	def _is_logged_in(request,*args,**kwargs):
		if request.user.is_authenticated:
			#return fun(request,*args,**kwargs)
			return HttpResponseRedirect('index/')
		else:
			return fun(request,*args,**kwargs)
	return _is_logged_in