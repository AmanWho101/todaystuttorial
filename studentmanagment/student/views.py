from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    all = Question.objects.filter(id=1).all()
    context = {
        "all": all
    }

    return render(request, 'student/index.html',context)

def view(request):

    return render(request, 'student/view.html')

def edit(request,id):
    
    return render(request, 'student/edit.html')

def delete(request):
    
    return HttpResponse('delete page')