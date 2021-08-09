from django.shortcuts import render,redirect
from django.contrib import messages

from .models import User, Comment, NewVideo
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models import Q
from django.views.generic import TemplateView,ListView

class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    #username=User.objects.filter(name=User.username)
    videos=NewVideo.objects.all()
    return render(request,'homepage.html',{'videos':videos})


def video(request,pk):
    video = NewVideo.objects.get(pk=pk)
    print(video)
    comments=Comment.objects.filter(video = video)
    count = Comment.objects.filter(video = video).count()
    if request.method=="POST":
        print(request.POST)
        if 'Addcomment' in request.POST:
            text = request.POST['Addcomment']
            user = User.objects.first()
            comment = Comment.objects.create(
                user = user,
                text = text,
                video = video
            )
        

        return redirect('ViewVideo',pk=pk)

    return render(request,'videoView.html',{'video':video,'comments':comments,'count':count})
        #Make the thumbs up and down icon a button
        #likes++ dislikes++
        #comment=request.POST["comment"]
        # add videoid=
        #commentobj=Comment(user=User.username,comment=comment) #add which video he had selected.



def upload(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            thumbnail =  request.FILES['thumbnail']
            video =  request.FILES['video']
            
            videoobj= NewVideo(user=request.user,title=title,description=desc, date=date.today(),thumbnail=thumbnail,video=video )
            videoobj.save()
        return render(request,'upload.html',{})


class SearchResultsView(ListView):
    model = NewVideo
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return NewVideo.objects.filter(
            Q(title__icontains=query)
        )
