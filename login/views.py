from django.shortcuts import render
from matplotlib.style import context

# Create your views here.
def home(request):
    return render (request, "home.html")





