from django.db import models

# Create your models here.
# models.py
from django.db import models
class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comments = models.TextField(max_length=255)
    class Meta:
        db_table="contactus"

# contacts/models.py

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
