from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hey_view(request, name):
    return HttpResponse(f"Hello, {name}!")

def age_in(request, end, birthyear):
    return HttpResponse(end - birthyear)

def order_total(request, burger, fries, drinks):
    total = (4.50 * burger) + (1.5 * fries) + (1 * drinks)
    return HttpResponse(total)