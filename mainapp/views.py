from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class home_page(TemplateView):
    template_name = "index.html"

def regForm(request):
    return render(request,'mainapp/register.html', {})
