from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Question

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addquestions(request):
    return render(request, 'addquestions.html')

def generateset(request):
    return render(request, 'generateset.html')

def questionset(request):
    # questions = Question.objects.all()
    return render(request, 'questionset.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

