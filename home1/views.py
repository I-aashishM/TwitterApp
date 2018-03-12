from django.shortcuts import render
from .forms import HomeForm
from django.views.generic import TemplateView
from twitter.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Post,User
from django.db.models import F
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        # model = Post,User
        data = Post.objects.all()
        current = request.user
        friends = User.objects.exclude(id=request.user.id)
        image = UserProfile.objects.filter(user_id=F('user__post__user'))
        context = {'form' : form,
                   'comments': data,
                   'friends': friends,
                   'current': current,
                   'image': image
                   }
        return render(request, self.template_name, context)

    def post(self,request):
        form = HomeForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()

        args = {'form': form, 'text': text}

        return render(request, self.template_name, args)

def index(req):
    return render(req,'index.html')

# def homeview(req):
#     form = forms.CharField(max_length=500)
#     data = Comment.objects.all()
#     current = req.user
#     friends = User.objects.exclude(id=req.user.id)
#     # image = UserProfile.objects.filter(user__comment__post = F('first_name'))
#     image = UserProfile.objects.filter(user_id = F('user__comment__post'))
#     context = {'comments':data,
#                'friends': friends,
#                'current':current,
#                'image': image
#                }
#     return render(req,'qwerty.html',context)


#

    #
    # def get(self,request):
    #     form = CommentForm()
    #     return render(request,self.template_name)



    # def get(self,request):
    #     form = HomeForm()
    #     return render (request,self.template_name,{'form':form})
    #
    # def post(self,request):
    #     form = HomeForm(request.POST)
    #
    #     if form.is_valid():
    #         text = form.cleaned_data['post']
    #         form = HomeForm()
    #
    #
    #     args = {'form':form,'text':text}
    #
    #     return render(request,self.template_name,args)