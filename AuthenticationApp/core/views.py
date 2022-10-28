from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(render(request , 'login.html'))


def signup(request):
    pass

def signin_via_service(request):
    pass

def signin(request):
    pass

def signout(request):
    pass

def profile(request):
    pass

def upload_photo(request):
    pass

 