from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import MainForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

class home_page(TemplateView):
    template_name = "index.html"

def regForm(request):
    if request.method=="POST":
        form = MainForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = MainForm()

    else:
        form = MainForm()



    return render(request,'mainapp/register1.html', {'form':form})

def invento(request):

    return render(request,'invento/invento.html',{})

def daksha(request):

    return render(request, 'daksha/daksha.html',{})

def achieve(request):

    return render(request, 'achievement/achieve.html',{})

def story(request):
    
    return render(request, 'stories/Alumni_Stories.html',{})

def Story(request):

    return render(request, 'stories/Alumni_Stories1.html',{})