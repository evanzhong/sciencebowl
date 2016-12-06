from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting
from .models import Question

import parse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def addquestions(request):
    return render(request, 'addquestions.html')

def questionsconfirmed(request):
    return render(request, 'questionsconfirmed.html')

@csrf_exempt
def generateset(request):
    if request.method == 'POST':
        comp = request.POST.get('comp')
        if comp == "":
            raise RuntimeError("empty values")
        diff = request.POST.get('diff')
        if diff == "":
            raise RuntimeError("empty values")
        rndType = request.POST.get('rndType')
        if rndType == "":
            raise RuntimeError("empty values")
        numQs = request.POST.get('numQs')
        if numQs == "":
            raise RuntimeError("empty values")
        subs = request.POST.get('subs')
        if subs == "":
            raise RuntimeError("empty values")
        scrammbleQs = request.POST.get('scrammbleQs')
        if scrammbleQs == "":
            raise RuntimeError("empty values")
        questions = Question.objects.all()
        for sub in subs:
            questions = Question.objects.filter(comp__iexact=comp).filter(subject__iexact=sub).order_by('?')[:numQs]#.filter(subject__iexact=subs[0])
        return render(request, 'questionset.html', {'questions': questions})
    return render(request, 'generateset.html')

def questionset(request):
    questions = Question.objects.all()
    return render(request, 'questionset.html', {'questions': questions})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        text = request.POST.get('upload')
        if text == "":
            raise RuntimeError("upload is empty!")
        parse.parse(text)
    return render(request, 'index.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

