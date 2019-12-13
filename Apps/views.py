from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Apps.Inventario.models import base12019

@login_required(login_url='/')
def home(request):
    count = base12019.objects.filter(user=request.user).count()
    template = 'index.html'
    return render(request, template, {'count':count})

@login_required(login_url='/')
def send(request):
    return redirect('home')