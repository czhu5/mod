from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    SSN = models.CharField(max_length=30)
    home_address = models.CharField(max_length=100, blank=True)

#photo = models.ImageField(upload_to="gallery")