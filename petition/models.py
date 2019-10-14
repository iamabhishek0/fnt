from django.db import models

# Create your models here.
class petition_entry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    reason = models.CharField(max_length=1000)
    have_pet = models.BooleanField(null=True)
