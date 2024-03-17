from django.db import models

# Create your models here.

class SupportForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    queryTitle = models.CharField(max_length=50)
