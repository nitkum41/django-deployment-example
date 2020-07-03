from django.contrib import admin
from first_app.models import Topic,AccessRecord,Webpage, UserProfileInfo   #import all models from app.models
# Register your models here.

admin.site.register(AccessRecord)  #register each model
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(UserProfileInfo)
