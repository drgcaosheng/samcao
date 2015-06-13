from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def test(request):
    return HttpResponse("test_views")
