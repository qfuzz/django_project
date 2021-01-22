from django.http import HttpResponse 
import datetime

def hello(request):
    return HttpResponse("Hello, World")

def get_current_time(request):
    now = datetime.datetime.now()
    html = "<html><body> Current time %s </body></html>" % now
    return HttpResponse(html)

def welcome(request):
    return HttpResponse("Welcome on Django Project Example")
