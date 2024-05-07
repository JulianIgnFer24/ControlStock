from django.db import models

# Create your models here.
class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()