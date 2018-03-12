from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='')
    phoneNo = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    profile_image = models.FileField(upload_to='profile_image', null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)