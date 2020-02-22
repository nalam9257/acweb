from django.conf.urls import url
from about import views
app_name='about'
urlpatterns=[
	url(r'^$',views.about,name='about_us'),
]