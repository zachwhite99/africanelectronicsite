from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
import urllib.request
import urllib.parse
import json

# Create your views here.

def home(request):
    return HttpResponse("emily rules!")
