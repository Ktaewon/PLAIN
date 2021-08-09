from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment
from Melody.models import Melody
from django.utils import timezone

# Create your views here.

def sub_page(request):
    return render(request, 'sub_page.html')

def comment(request, melody_id):
        if request.method == "POST" :
            comment = Comment()
            comment.body = request.POST['body']
            comment.pub_date = timezone.datetime.now()
            comment.writer = request.user
            comment.post = get_object_or_404(Melody, pk=melody_id)
            comment.save()

            return redirect(''+str(melody_id))
        else:
            return redirect(''+str(melody_id))

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    melody_id = comment.post.id
    comment.delete()
    return redirect(''+str(melody_id))