from django.urls import path
# from django.conf.urls import url
from . import views

from django.contrib.auth.views import login, logout
from .views import HomeView


app_name = "home1"

urlpatterns = [
    path(r'index/', HomeView.as_view(), name="index"),
    path(r'', login, {'template_name': 'index.html'},name="index1"),
    # path(r'index/',views.homeview,name="index"),
    # path(r'login/', login, {'template_name': 'index.html'}, name="login"),
    ]