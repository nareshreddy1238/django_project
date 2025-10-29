from django.shortcuts import render
from django.http import HttpResponse


def display_quote(request):
    s = """
      The only limit to our realization of tomorrow is our doubts of today. 
        - Franklin D. Roosevelt"
    """
    return HttpResponse(s)    