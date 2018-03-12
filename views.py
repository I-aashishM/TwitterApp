from django.shortcuts import render, redirect,get_object_or_404

from django.views.generic import TemplateView,CreateView
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser, EditProfile , ImageUpload
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from home1.models import Post
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models import F

# Create your views here.
# def index(req):
#     return render(req, 'qwerty.html')

def register(req):
    if req.method == 'POST':
        form = RegisterUser(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/home/index')

    else:
        form = RegisterUser()
        context = {'form' : form}
        return render(req, 'includes/registration.html', context)

@login_required
def view_profile(req, pk=None):
    instance = get_object_or_404(UserProfile, user=req.user)

    if pk:
        user = User.objects.get(pk=pk)
        blog_post=None
        profile_comment = Post.objects.filter(user_id=user.id)


    else:
        user = req.user
        blog_post = Post.objects.filter(user_id=user.id)
        profile_comment =None


        if req.method == 'POST':
            form = ImageUpload(req.POST or None, req.FILES or None, instance=instance)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = req.user
                profile.save()

                text = form.cleaned_data['profile_image']

        else:
            form = ImageUpload(instance=instance)
            blog_post = Post.objects.filter(user_id=user.id)
            return render(req,'includes/profile.html',{'form':form , 'blog':blog_post})

    context = {"user" : user,
               'blog' : blog_post,
               'profile_comment':profile_comment,
               'form':form,
               'profile':profile,
               'text':text,
               'instance':instance
              }
    return render(req, 'includes/profile.html', context)


@login_required
def edit_profile(req):
    if req.method == 'POST':
        form = EditProfile(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('/twitter/profile')

    else:
        form = EditProfile(instance=req.user)
        data = UserProfile.objects.filter(user = req.user)
        context = {'form' : form,'data': data}
        return render(req, 'includes/edit_profile.html', context)


def change_password(req):
    if req.method == 'POST':
        form = PasswordChangeForm(data=req.POST, user=req.user)
        if form.is_valid():
            form.save()
            return redirect('/twitter/profile')
    else:
        form = PasswordChangeForm(user=req.user)
        context = {'form' : form}
        return render(req,'includes/change_password.html',context)


