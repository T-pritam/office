from email.policy import default
from xml.parsers.expat import model
from django.db import models
from datetime import datetime

# Create your models here.
class employee(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    join=models.DateField('date',default=datetime.now())

    def __str__(self):
        return self.fname