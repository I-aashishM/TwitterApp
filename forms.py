from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class RegisterUser(UserCreationForm):
    email = forms.EmailField(max_length=50 , widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your Email Id',
            'class' : 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user_1 = super(RegisterUser, self).save(commit=False)
        user_1.first_name = self.cleaned_data['first_name']
        user_1.last_name = self.cleaned_data['last_name']
        user_1.email = self.cleaned_data['email']

        if commit:
            user_1.save()
        return user_1

class EditProfile(UserChangeForm):
    template_name = 'includes/edit_profile.html'

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )

class ImageUpload(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = (
            'profile_image',
        )