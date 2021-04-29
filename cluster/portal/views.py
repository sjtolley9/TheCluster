from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadJobForm

def create_job(request):
    template = 'portal/upload.html'
    if request.method == 'POST':
        form = UploadJobForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadJobForm()

    return render(request, 'portal/upload.html', {'form': form})

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Rockslide Portal")

def top(request):
    return redirect('/portal/')
