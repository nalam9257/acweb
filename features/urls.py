from features import views
from django.conf.urls import url
app_name='features'
urlpatterns=[
	url(r'^$',views.customer_details,name="customer_details"),
]