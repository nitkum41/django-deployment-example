import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


###
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        top = add_topic() #get a topic

        #create entries for the models
        fake_name= fakegen.company()
        fake_date=fakegen.date()
        fake_url=fakegen.url()

        #webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        
        #access record entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('Populating script!!!')
    populate(20)
    print('populating done !!')
