from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs = {
            'placeholder' : 'Enter something here',
            'class' : 'form-control'
        }
    ))

    class Meta():
        model = Post
        fields = ('post',)


