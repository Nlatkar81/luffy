from django.db import models

# Create your models here.
class Home(models.Model):
    fname=models.CharField(max_length=110)
    lname=models.CharField(max_length=110)
    email=models.CharField(max_length=110)
    area=models.CharField(max_length=110)

    