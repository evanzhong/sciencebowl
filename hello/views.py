from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting
from .models import Question

import csv_parse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addquestions(request):
    return render(request, 'addquestions.html')

def questionsconfirmed(request):
    return render(request, 'questionsconfirmed.html')

def generateset(request):
    return render(request, 'generateset.html')

def questionset(request):
    questions = Question.objects.all()
    return render(request, 'questionset.html', {'questions': questions})

@csrf_exempt
def upload_tsv(request):
    if request.method == 'POST':
        text = request.POST.get('upload')
        if text == "":
            raise RuntimeError("upload is empty!")
        csv_parse.parse(text)
    return render(request, 'index.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

