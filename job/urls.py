from django.urls import path
from .import views

urlpatterns = [
    path('', views.jobhome, name="jobhome"),
    path('<str:slug>', views.jobpost, name="jobpost")
]