from django.shortcuts import redirect, render, get_object_or_404
from .models import Melody, Comment, Follow
from .forms import MelodyForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def melody(request):
    #form = MelodyForm()
    #return render(request, 'melody_upload.html', {'form' : form })
    return render(request, 'melody_upload.html')
def detail(request, id):
    detail = get_object_or_404(Melody, pk=id)
    comments = Comment.objects.all().filter(Comment_post = detail)

    melody = get_object_or_404(Melody, pk=id)


    if detail.likes.filter(id=request.user.id):
        message= "좋아요 취소"
    else: 
        message = "좋아요"
    return render(request, 'melody_detail.html', 
    {'melody' : melody, 'detail' : detail, 'commnets': comments, 'message':message })

def upload_melody(request):
    if request.method == "POST":
        melody = Melody()
        melody.title = request.POST["title"]
        melody.deadline = request.POST["deadline"]
        melody.img = request.FILES.get("imgInput")
        if request.POST["body"]:
            melody.body = request.POST["body"]
        melody.owner = request.user
        melody.myInstrument = request.POST["mine"]
        melody.audio = request.FILES.get("melodyInput")
        melody.save()
        tags = request.POST["hashtag_data"].split(",")
        for tag in tags:
            tag = tag.strip()
            melody.hashtags.add(tag)
        melody.save()
        messages.warning(request, 'Upload Finish!')
        return redirect('detail', melody.id)

# Comments
def comment(request, melody_id):
        if request.method == "POST" :
            comment = Comment()
            comment.body = request.POST['body']
            comment.pub_date = timezone.datetime.now()
            comment.writer = request.user
            comment.post = get_object_or_404(Melody, pk=melody_id)
            comment.save()

            return redirect('/melody/'+str(melody_id))
        else:
            return redirect('/melody/'+str(melody_id))

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    melody_id = comment.post.id
    comment.delete()
    return redirect('/melody/'+str(melody_id))

# likes
def post_like(request, melody_id):
    melody = get_object_or_404(Melody, pk=melody_id)
    melody.delete()
    return redirect('/Melody')


def default(request):
    return render(request,'melody_default.html')

    user = request.user

    if melody.likes.filter(id=user.id):
        melody.likes.remove(user)
    else: 
        melody.likes.add(user)

    return redirect('/melody/detail/' + str(melody_id))


# follows
def follow(request, user_id):
    people = get_object_or_404(User, id=user_id)

    if request.user in people.follower.all():
        people.follower.remove(request.user)
    else: 
        people.follower.add(request.user)
    return redirect('', people.username)

