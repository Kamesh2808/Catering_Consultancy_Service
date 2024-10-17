from django.db import models

from django.db import models


class sign_up(models.Model):
    Uname=models.CharField(max_length=20)
    Mailid=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20) 
    Pass=models.CharField(max_length=20)
    Cpass=models.CharField(max_length=20)


class sign_up_cater(models.Model):
    Uname=models.CharField(max_length=20)
    Mailid=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20) 
    Pass=models.CharField(max_length=20)
    Cpass=models.CharField(max_length=20)

class catering_info(models.Model):
    Cname=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Menu=models.CharField(max_length=100)
    Cuisine=models.CharField(max_length=100)
    Availability=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Additionalservices=models.CharField(max_length=100)
    About=models.CharField(max_length=1000)
     # Foreign key to connect User and Catering_Info
    user=models.OneToOneField(sign_up_cater, on_delete=models.CASCADE, primary_key=True)
