from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.

def near_hundred(request, n):
  return HttpResponse((abs(100 - n) <= 10) or (abs(200 - n) <=10))

def lone_sum(request, a, b, c):
  if c == b and c == a  and a == b:
    return HttpResponse(0)
  elif a == b:
    return HttpResponse(c)
  elif a == c:
    return HttpResponse(b)
  elif b == a:
    return HttpResponse(c)
  elif b == c:
    return HttpResponse(a)
  elif c == a:
    return HttpResponse(b)
  elif c == b:
    return HttpResponse(a)
  else:
    return HttpResponse(a + b + c)

def string_splosion(request, str):
  result = ""
  for i in range(len(str)):
    result += str[:i+1]
  return HttpResponse(result)