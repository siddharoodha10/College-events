from django.db import models


CHOICES_TYPE = (
    ('cultural','Cultural'),
    ('technical','Technical'),
    
)
# Create your models here.
class Event(models.Model):
    E_id = models.CharField(max_length=100)
    E_name=models.CharField(max_length=100)
    E_type=models.CharField(max_length=100,choices=CHOICES_TYPE, default='Cultural')
    E_location=models.CharField(max_length=100)
    E_date = models.DateField(default=2021-9-12)
    E_time=models.TimeField()
    E_fees=models.IntegerField(default=30)
    E_coordinator_no=models.CharField(max_length=100)
    E_image=models.ImageField(upload_to='pics',default='static/image1.jpg')


        
class student(models.Model):
    USN = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30)
    sem = models.IntegerField()
    college = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100,default=0)
    Even_fees=models.IntegerField(default=30)
    payment_mode = models.CharField(max_length=100,default=0)
    account_no = models.CharField(max_length=100,default=0)
    cvv = models.IntegerField(default=0)
    exp_date = models.DateField(default=2021-12-1)
    E_id = models.ForeignKey(Event,default=-1,on_delete=models.SET_DEFAULT)
    E_name=models.CharField(max_length=100)


