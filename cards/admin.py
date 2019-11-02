from django.contrib import admin
from cards.models import Player, Card, Trade
# Register your models here.

admin.site.register(Player)
admin.site.register(Card)
admin.site.register(Trade)