from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {'bbs' : bbs}
    return render(request, 'bboard/index.html', context)
