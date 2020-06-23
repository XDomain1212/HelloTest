from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. you're at the News index.")

def detail(request,news_id):
    return HttpResponse("You're looking as news %s ." %news_id)
    