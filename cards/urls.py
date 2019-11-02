from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView

app_name='cards'

urlpatterns=[
    url(r'profile', views.profile, name='profile'),
    url(r'^change_colour/$', views.change_colour, name='change colour'),
    url(r'^login/$', LoginView.as_view(template_name='cards/login.html'), name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create_profile/$', views.create_profile, name='create profile')
]