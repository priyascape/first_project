
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index (request):
    print(request)
    return render(request, 'index.html')

def root (request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new (request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create (request):
    return redirect('/blogs')

def show (request,num):
    return HttpResponse(f"placeholder to display blog number:{num}")

def edit (request,num):
    return HttpResponse(f"placeholder to edit blog:{num}")

def destroy (request,num):
    return redirect('/blogs')

def json(request):
    print ("Hello")
    data = {
        'title': 'My first blog',
        'content': 'Lorem Inspsum dolore sit amit consectur adipsicpy'
    }
    return JsonResponse(data)