from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_page.as_view()),
    #path('/form',views.regForm, name = 'registrationform')
]
