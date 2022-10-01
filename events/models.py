import email
from multiprocessing import managers
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name' ,max_length=200)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=150)
    phone = models.CharField('Contact Phone', max_length=150)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')
    owner = models.IntegerField("Vanue owner", default=1, blank=False)

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name =models.CharField(max_length=150)
    last_name =models.CharField(max_length=150)
    email_address = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + '' + self.last_name

class Event(models.Model):
    name = models.CharField('Event name', max_length=200)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description =models.TextField(null=True, blank=True)
    attendees  = models.ManyToManyField(MyclubUser, null=True, blank=True)

    def __str__(self):
        return self.name