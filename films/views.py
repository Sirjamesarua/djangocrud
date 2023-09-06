from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def films(request):
    template = loader.get_template('myfirsthtml.html')
    return HttpResponse(template.render())