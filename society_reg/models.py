from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField
from django.contrib.auth.models import Group

class Society(models.Model):
    society  = models.OneToOneField(User,null=True, blank =True,on_delete=models.CASCADE)
    name = models.CharField(max_length =200,null=True)
    email = models.EmailField(null=True,blank =True)


    def __str__(self):
        return self.name





class Visitor(models.Model):


    VEHICLE = (
        ('None','No vehicle'),
        ('Bike','Bike'),
        ('Car','Car')
    )


  

    
    name = models.CharField(max_length =200,null=True)
    phone = models.CharField(max_length =200,null=True,blank=True, help_text='Contact phone number')
    vehicle = models.CharField(max_length =200,null=True,choices =  VEHICLE)
    in_time = models.DateTimeField(auto_now_add =True,blank=True,null=True)
    society = models.ForeignKey(Society,null=True, blank =True,on_delete=models.CASCADE)
    purpose = models.CharField(max_length =200,null=True)
    out_time = models.DateTimeField(auto_now_add =False,blank=True,null=True)

    def __str__(self):
        return self.name

