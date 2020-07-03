from django.shortcuts import render

#import models here
from first_app.models import AccessRecord,Webpage,Topic , User,UserProfileInfo
 #for registration
from first_app import forms  #for forms
from first_app.forms import UserForm , UserProfileInfoForm
"""from . import forms"""


#for login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout





# Create your views here.
def welcome(request):
    #my_dict = {'insert_me':"hello i am from views.py !!!"}  #key of this dictionary is same as the template tag variable
    #return render(request,'first_app/welcome.html',context=my_dict)
    return render(request,'first_app/welcome.html')

def welcome_app(request):
    #return HttpResponse("Welcome inside the first app of the first_project")
    return render(request,'first_app/welcome_app.html')


def read_db(request):
    webpages_list = AccessRecord.objects.order_by('date')  #extracting from the DM directly
    date_dict = {'access_records': webpages_list}
    #my_dict = {'insert_me':"hello i am from views.py !!!"}  #key of this dictionary is same as the template tag variable
    return render(request,'first_app/read_db.html',context=date_dict)  #path is set as the path of the html file in the templates folder
    #return HttpResponse("Hello World")



def image(request):
    return render(request,'first_app/image.html')



#basic form view
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':  #if form is submitted
        form = forms.FormName(request.POST)
        if form.is_valid():  #check if valid r not ...its auto validated
            print("validation successful")
            print("Name :" + form.cleaned_data['name'])
            print("Email :" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])

    return render(request,"first_app/form_page.html",{'form':form})



#templates
def index(request):
    #context_dict = {'text':"hello world",'number':100}
    return render(request,"first_app/index.html")

def other(request):
    return render(request,"first_app/other.html")

def relative(request):
    return render(request,"first_app/relative_url_templates.html")


#registration

def register(request):

    registered = False

    if request.method == 'POST':
        print('form filled')
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid( ) and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  #password hashing
            user.save()  #save user data


            profile = profile_form.save(commit = False)
            profile.user = user #one to one relation

            if 'profile_pic' in request.FILES:    #iterating over media files uploaded in the registration process
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            print('form saved')
        else:
            print(user_form.errors,profile_form.errors)   #error printing on the forms

    else:
        print('form created')
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,"first_app/registration.html",{'user_form':user_form,'profile_form':profile_form,'registered':registered})


#login

def user_login(request):


    if request.method == 'POST':
        username = request.POST.get('username')  #form variables
        password = request.POST.get('password')

        user = authenticate(username =username, password = password)  #automatic authentication by django
        if user:

            if user.is_active:  #checking succesful authentication or not
                login(request,user)  #login using login method
                return HttpResponseRedirect(reverse('index'))  #redirect it to index page

            else:
                return HttpResponse("account not active")

        else:
            print("login failed")
            print("username :{}  password:{}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:

        return render(request,"first_app/login.html",{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("you are logged in")
