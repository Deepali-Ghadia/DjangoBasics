# This file is created by me
from django.http import HttpResponse

def index(request):
    return HttpResponse("Landing page of my first django website")

def about(request):
    return HttpResponse("<html>Hii,<br> I am Deepali developing my first django website</html>")

def home(request):
    return HttpResponse("This is the home page of my website...")