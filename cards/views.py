from django.shortcuts import render
from .forms import ProfileForm
from .models import Player, Card
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from collections import defaultdict


# Create your views here.
@login_required
def profile(request):
    player = Player.objects.get(user=request.user)
    cards = player.card_set.order_by('-date_added')
    d = defaultdict(list)
    for c in cards:
        if c.card_colour in d:
            d[c.card_colour].append(c)
        else:
            d[c.card_colour] = [c]
    dict(d)
    context = {'player': player, 'dict': d.items()}
    return render(request, 'cards/profile.html', context)

@login_required
def change_colour(request):
    if request.method != 'POST':
        pass
    else:
        player = Player.objects.get(user=request.user)
        player.colour = request.POST['colour']
        player.save()
        return HttpResponseRedirect(reverse('cards:avatar'))
    return render(request, 'cards/change_colour.html')

@login_required
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

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('cards:login'))


@login_required
def gain_card(request):
    player = Player.objects.get(user=request.user)

    c = Card.objects.create(card_name='None', owner=player, card_colour=player.colour, original_owner=player)
    context = {'card': c}
    return HttpResponseRedirect(reverse('cards:profile'))

@login_required
def avatar(request):
    if request.method != 'POST':
        pass
    else:
        player = Player.objects.get(user=request.user)
        player.profile_image = request.POST['profile_image']
        player.save()
        return HttpResponseRedirect(reverse('cards:profile'))
    return render(request, 'cards/avatar.html')