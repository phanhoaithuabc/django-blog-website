from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return render(requests, 'blog/home.html')

def about(requests):
    return HttpResponse("<h1>about</h1>")