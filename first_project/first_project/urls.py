"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , re_path , include
from first_app import views

"""re_path(r'^$',views.index,name='index')
   re_path(r'^first_app/',views.index,name='index')
   re_path , include
   we can add anything as our domain extensiom name
"""

urlpatterns = [
    #path('',views.welcome,name='welcome'),
    path('',views.index,name='index'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    #path('formpage/',views.form_name_view,name='form_name_view'),
    path('first_app/',include('first_app.urls')),
    path('admin/', admin.site.urls),
]