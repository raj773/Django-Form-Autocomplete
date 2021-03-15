from django.db import models

# Create your models here.
class Contact(models.Model):

    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=300)
    city=models.CharField(max_length=12)



    def __str__(self):
        return self.email

class City(models.Model):

    city_id=models.CharField(max_length=10)
    name=models.CharField(max_length=12)
    def __str__(self):
        return self.name
