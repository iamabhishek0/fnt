from django.db import models

# Create your models here.
class petition_entry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    reason = models.CharField(max_length=1000)
    have_pet = models.BooleanField(null=True)


class rescue_entry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    scenario = models.CharField(max_length=1000,blank=True)
    identification_mark = models.CharField(max_length=100,blank=True)
    dog_type = models.CharField(max_length=100,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)