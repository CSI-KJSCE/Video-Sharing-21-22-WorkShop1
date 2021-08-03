from django.shortcuts import render
from .models import User, Video, Comment
# Create your views here.


from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    user=User.ojects.filter(name=User.username)
    videos=Video.objects.all()
    return render(request,'homepage.html',{"user":user, "video":videos})


def video(request):
    comments=Comments.objects.all()
    if request.method=="POST":
        #Make the thumbs up and down icon a button
        #likes++ dislikes++
        comment=request.POST["comment"]
        # add videoid=
        commentobj=Comment(user=User.username,comment=comment) #add which video he had selected.
    return render(request,'videoView.html',{"comments":comments})
