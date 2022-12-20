from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    startingPrice = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)

    class Condition(models.TextChoices):
        NEW = 'New'
        USED = 'Used'
        REFURB = 'Refurbished'
        NW = 'Not Working/For Parts'

    condition = models.CharField(
        max_length=21,
        choices = Condition.choices,
        default=Condition.NEW
    )

class Bid(models.Model):
    amount = models.IntegerField()
    listing = Listing()
    user = User()
    date = models.DateField()
    time = models.TimeField()

class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = User()
    date = models.DateField()
    time = models.TimeField()
