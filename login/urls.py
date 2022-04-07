from django.urls import path
from .views import  home


app_name="login"

urlpatterns=[
    path('',home,name='home')
]