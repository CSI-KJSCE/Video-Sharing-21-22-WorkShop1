from django.shortcuts import render
from django.contrib import messages
from .models import User, Comment, NewVideo
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

    comments=Comment.objects.all()
    #if request.method=="POST":
    return render(request,'videoView.html',{'video':video,'comments':comments})
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

class SearchResultsView(ListView):
    model = NewVideo
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return NewVideo.objects.filter(
            Q(title__icontains=query) 
        )