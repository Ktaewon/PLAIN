from django.shortcuts import render

# Create your views here.
def melody(request):
    return render(request, 'melody_upload.html')