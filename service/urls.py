from django.conf.urls import url
from service import views
# SET THE NAMESPACE!
app_name = 'service'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^',views.servicefun,name='service_'),
    
    

 
 ]
