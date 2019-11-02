from django.shortcuts import render
from .forms import ProfileForm
from .models import Player, Card
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def profile(request):
    player = Player.objects.get(user=request.user)
    context = {'player': player}
    return render(request, 'cards/profile.html', context)


def change_colour(request):
    if request.method != 'POST':
        pass
    else:
        player = Player.objects.get(user=request.user)
        player.colour = request.POST['colour']
        player.save()
        return HttpResponseRedirect(reverse('cards:profile'))
    return render(request, 'cards/change_colour.html')


def create_profile(request):
    if request.method != 'POST':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.user = request.user
            new_player.save()
            return HttpResponseRedirect(reverse('cards:change colour'))
    context = {'form': form}
    return render(request, 'cards/create_profile.html', context)


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('cards:create profile'))

    context = {'form': form}
    return render(request, 'cards/register.html', context)
