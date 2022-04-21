import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from . models import Circle


def home(request):
    return render(request, "home.html")


def area(request):
    radius = request.POST['radius']
    if radius != "":
        circle = Circle()
        circle.radius = float(radius)
        res = circle.area()
        return render(request, "results.html", {'area': res, 'name': 'Victor', 'msg': 'Successful'})
    return render(request, "results.html", {'area': radius, 'name': 'Victor', 'msg': 'Click back to enter radius'})
