from django.conf.urls import url
from contact_us import views
app_name='contact_us'
urlpatterns=[
		url(r'^$',views.contact_us,name='contact_us'),
		url(r'^send/',views.sendfun,name='sendfun'),

]