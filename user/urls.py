from django.urls import path
from .views import usrlogin, usrlogout, account, signup

urlpatterns = [
    path('', account, name="account"),
    path('login', usrlogin, name="login"),
    path('logout', usrlogout, name="logout"),
    path('signup', signup, name="signup"),
]