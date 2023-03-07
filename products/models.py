from email.policy import default
from optparse import Option
from random import choices
from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.IntegerField(default=1000)
    options=(
        ("4G","4G"),
        ("5G","5G"),
        ("3G","3G")
    )
    band=models.CharField(max_length=200,choices=options,default="4G")
    doption=(
        ("LED","LED"),
        ("SMOLED","SMOLED"),
        ("AMOLED","AMOLED")
    )
    display=models.CharField(max_length=200,choices=doption,default="LED")