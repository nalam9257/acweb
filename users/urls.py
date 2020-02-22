from django.conf.urls import url
from users import views
app_name='users'
urlpatterns=[
url(r'^$',views.signup,name='signup'),
url(r'^login/',views.login_profile,name='login'),
url(r'^test/',views.test,name='test'),


]