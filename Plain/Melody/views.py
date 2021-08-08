from django.shortcuts import redirect, render
from .models import Melody
from .forms import MelodyForm
from django.utils import timezone

# Create your views here.
def melody(request):
    #form = MelodyForm()
    #return render(request, 'melody_upload.html', {'form' : form })
    return render(request, 'melody_upload.html')
def upload_melody(request):
    if request.method == "POST":
        melody = Melody()
        form = MelodyForm(request.POST, instance=melody)
        if form.is_valid():
            print(form)
            form.owner = request.user
            form.created_at = timezone.datetime.now()
            form.save()
            return render(request, 'melody_upload.html', {'form' : form })
            #return redirect('melody' + str(melody.id))
