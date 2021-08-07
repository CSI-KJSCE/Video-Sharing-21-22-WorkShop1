from django.shortcuts import render
from django.contrib import messages
from .models import User, Comment, NewVideo
from datetime import date
# Create your views here.


from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    #username=User.objects.filter(name=User.username)
    #videos=Video.objects.all()
    return render(request,'homepage.html',{})
#"user":user, "video":videos

def video(request):
    #comments=Comments.objects.all()
    #if request.method=="POST":
    return render(request,'videoView.html',{})
        #Make the thumbs up and down icon a button
        #likes++ dislikes++
        #comment=request.POST["comment"]
        # add videoid=
        #commentobj=Comment(user=User.username,comment=comment) #add which video he had selected.

    #{"comments":comments}


def upload(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        thumbnail =  request.FILES['thumbnail']
        video =  request.FILES['video']


        videoobj= NewVideo(user=request.user,title=title,description=desc, date=date.today(),thumbnail=thumbnail,video=video )
        videoobj.save()

        #print('\n\n\n' + request.user + '\n\n')

    return render(request,'upload.html',{})
