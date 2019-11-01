from django.shortcuts import render
from .forms import ChangeColourForm
from .models import Player, Card
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


# Create your views here.


def change_colour(request):
    if request.method != 'POST':
        pass
    else:
        player = Player.objects.get(user=request.user)
        player.colour = request.POST['colour']
        player.save()
        return HttpResponseRedirect(reverse('cards:change colour'))
    return render(request, 'cards/change_colour.html')


