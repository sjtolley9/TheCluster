from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UploadJobForm
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/new/')
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return auth_view(request)
    else:
        form = LoginForm()

    return render(request, 'portal/login1.html', {'form': form})

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/new')
    else:
        pass
        return HttpResponseRedirect('/login/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def create_job(request):
    template = 'portal/upload.html'
    if request.method == 'POST':
        form = UploadJobForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/new/')
    else:
        form = UploadJobForm()

    return render(request, 'portal/home.html', {'form': form})

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {'user': request.user})

def top(request):
    return redirect('/portal/')
