from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def quiz(request):
  templates = loader.get_templates('index.html')
  return HttpResponse(templates.render())