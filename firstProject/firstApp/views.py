from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>Hello, welcome to my first Django app!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current date and time: " + str(dt) + "</b>"
    return HttpResponse(s)

