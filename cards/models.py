from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

class Player(models.Model):
    colour = models.CharField(max_length=50, default='please choose a colour')
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Card(models.Model):
    card_name = models.CharField(max_length=200, default='No card name')
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    card_colour = models.CharField(max_length=50, default='No colour')
    original_owner = models.CharField(max_length=50)
    Card_face = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_name
