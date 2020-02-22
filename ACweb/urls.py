"""ACweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from home import views
from users import views as users_views
from features import views as features_views
urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$',views.index,name='index'),
    url(r'^Logout/',users_views.logout_profile,name='Logout'),
    url(r'^service/',include('service.urls')),
    url(r'^about/',include('about.urls')),
    url(r'^contact_us/',include('contact_us.urls'),name='contact_us'),
    url(r'^signup/',include('users.urls')),
    url(r'gasfilling/',features_views.gasfilling,name='gasfilling'),
    url(r'dust/',features_views.dust,name='dust'),
    url(r'installation/',features_views.installation,name='installation'),
    url(r'compressor/',features_views.compressor,name='compressor'),
    url(r'fillter/',features_views.fillter,name='fillter'),
    url(r'repair/',features_views.repair,name='repair'),
    url(r'^info/',include('features.urls'),name='features'),
    
    

]
