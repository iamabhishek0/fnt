from django.db import models

# Create your models here.
class petition_entry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    reason = models.CharField(max_length=1000)
    have_pet = models.BooleanField(null=True)


class rescue_entry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    scenario = models.CharField(max_length=1000)
    identification_mark = models.CharField(max_length=100)
    dog_type = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)