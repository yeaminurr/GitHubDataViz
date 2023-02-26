import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GithubDataViz.settings')
import django
django.setup()
import random
from firstapp.models import userss , fname
from faker import Faker
fak = Faker()
for i in range(20):
    # Users = userss()
    # fnamee = fname()
    myname = fak.name()

    #fname1 = fname.objects.get_or_create(name=myname)[0]
    #fname1.save()
    mlastname = fak.name()
    memail = fak.email()


    name= userss.objects.get_or_create(firstname = myname ,lastname = mlastname,email = memail)[0]
    #name.save()