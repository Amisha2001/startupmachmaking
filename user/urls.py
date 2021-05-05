from django.urls import path
from .views import usrlogin, usrlogout, account, signup, profile,found_dash

urlpatterns = [
    path('', account, name="account"),
    path('login', usrlogin, name="login"),
    path('logout', usrlogout, name="logout"),
    path('signup', signup, name="signup"),
    path('profile', profile, name="profile" ),
    path('found_dash',found_dash,name="found_dash")
]