from django.db import models

class UserDetails(models.Model):
    user_name = models.CharField(max_length=150,blank=False,null=False)
    user_age = models.IntegerField()
    user_email = models.EmailField(max_length=250)
    user_phone_number = models.IntegerField(null= True,blank = True,default =1)
    user_entrolment_id = models.CharField(max_length=20)
    user_specialization = models.CharField(max_length=250,default ="unni")
    user_address =models.CharField(max_length=300,default ="unni")
    user_password =models.CharField(max_length =25 ,default='siju')
