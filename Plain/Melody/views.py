from django.shortcuts import render
from .forms import MelodyForm

# Create your views here.
def melody(request):
    form = MelodyForm()
    return render(request, 'melody_upload.html', {'form' : form })