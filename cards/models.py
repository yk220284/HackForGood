from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

class Player(models.Model):
    colour = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Card(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    Card_face = models.ImageField(upload_to='card_faces/')
