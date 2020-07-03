from django import forms
from first_app.models import  UserProfileInfo
from django.contrib.auth.models import User

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)

#model forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class  UserProfileInfoForm(forms.ModelForm):

    #portfolio = forms.URLField(required = False)
    #picture = forms.ImageField(required = False)

    class Meta():
        model =  UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        #exclude = ('user',)
