import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')
import django
django.setup()

from crudapp.models import *
from faker import Faker
# from faker import Faker
from random import *
faker=Faker()
def sudhakar(n):
    for i in range(n):
        fempno=randint(100,999)
        fempname=faker.name()
        fempsal=randint(25000,50000)
        fempaddress=faker.city()
        emp_record=Employee.objects.get_or_create(empno=fempno,
                                                  empname=fempname,
                                                  empsal=fempsal,
                                                  empaddress=fempaddress)
sudhakar(15)