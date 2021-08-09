from django.shortcuts import redirect, render, get_object_or_404
from .models import Melody
from .forms import MelodyForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def melody(request):
    #form = MelodyForm()
    #return render(request, 'melody_upload.html', {'form' : form })
    return render(request, 'melody_upload.html')
def detail(request, id):
    melody = get_object_or_404(Melody, pk=id)
    return render(request, 'melody_detail.html', {'melody' : melody})
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

def delete(request, melody_id):
    melody = get_object_or_404(Melody, pk=melody_id)
    melody.delete()
    return redirect('/Melody')


def default(request):
    return render(request,'melody_default.html')

