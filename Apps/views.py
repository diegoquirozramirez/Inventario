from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def home(request):
    template = 'index.html'
    return render(request, template)

@login_required(login_url='/')
def send(request):
    return redirect('home')