from django.urls import path
from . import views
from django.contrib.auth.views import login, logout
# from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static


app_name = "twitter"

urlpatterns = [
    # path(r'', views.home, name='home'),
    # path(r'', views.index, name="index"),
    path(r'register/', views.register, name="register"),
    path(r'search/', views.view_profile, name="view_profile"),
    path(r'profile/', views.view_profile, name="profile"),
    path(r'profile/(^?P<pk>\d+$)', views.view_profile, name="profile_with_pk"),
    path(r'edit_profile/', views.edit_profile, name="edit_profile"),
    # path(r'edit_profile/', views.edit_profileModel, name="edit_profileModel"),
    # path(r'login/', login, {'template_name' : 'includes/login.html'}, name="login"),
    path(r'logout/', logout, {'template_name' : 'includes/logout.html'}, name="logout"),
    path(r'change_password/', views.change_password, name="change_password"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)