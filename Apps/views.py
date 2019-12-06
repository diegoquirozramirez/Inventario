from django.shortcuts import render, redirect

def home(request):
    template = 'index.html'
    return render(request, template)

def send(request):
    return redirect('home')