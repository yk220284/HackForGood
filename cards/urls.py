from . import views
from django.conf.urls import url

app_name='cards'

urlpatterns=[
    #url(r'profile', views.profile, name='profile'),
    url(r'change_colour', views.change_colour, name='change colour'),
]