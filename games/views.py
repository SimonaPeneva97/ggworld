from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to GGWorld")


