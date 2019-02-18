from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_page.as_view()),
    path('form', views.regForm , name="registration"),
    path('invento',views.invento, name = "Invento"),
    path('daksha',views.daksha, name = "Daksha"),
    path('achievements',views.achieve, name = "Achievements"),
    path('stories',views.story, name = "Story"),
]
