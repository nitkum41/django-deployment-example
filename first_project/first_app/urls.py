from first_app import views
from django.urls import path

#TEMPLATE TAGGING
app_name = 'first_app'


urlpatterns=[
       path('',views.welcome_app,name='welcome_app'),

       path('readdb/',views.read_db,name='read_db'),
       #path('welcome/',views.welcome,name='welcome'),
       path('image/',views.image,name='image'),
       path('formpage/',views.form_name_view,name='form_name_view'),

       path('relative/',views.relative,name='relative'),
       path('other/',views.other,name='other'),
       #path('relative/',views.relative,name='relative'),
       path('register/',views.register,name='register'),
       path('user_login/',views.user_login,name='user_login')



]
