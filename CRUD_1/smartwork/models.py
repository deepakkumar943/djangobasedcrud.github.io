from django.db import models
class user(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    mobile_no=models.IntegerField(max_length=12)



   
