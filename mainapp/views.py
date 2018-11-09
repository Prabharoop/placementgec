from django.shortcuts import render
from django.views.generic.base import TemplateView
# from .forms import MainForm

# Create your views here.

class home_page(TemplateView):
    template_name = "index.html"

def regForm(request):
    # if request.method=="POST":
    #     form = MainForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    #         form = MainForm()
    #
    # else:
    #     form = MainForm()
    #


    return render(request,'mainapp/register.html', {})
