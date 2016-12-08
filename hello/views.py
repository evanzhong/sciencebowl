from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Greeting
from .models import Question

import parse
# #User has been created, therefore this code is commented out
# from django.contrib.auth.models import User
# user = User.objects.create_user(username='ScienceBowl',
#                                  email='',
#                                  password='cowseatcereal888')

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

@login_required
def addquestions(request):
    return render(request, 'addquestions.html')
@login_required
def questionsconfirmed(request):
    return render(request, 'questionsconfirmed.html')

@login_required
@csrf_exempt
def generateset(request):
    if request.method == 'POST':
        comp = request.POST.get('comp')
        if comp == "":
            raise RuntimeError("empty values")
        if comp == "NSB":
            isNOSB = False
        else:
            isNOSB = True
        diff = request.POST.getlist('diff[]')
        if diff == "":
            raise RuntimeError("empty values")
        rndType = request.POST.get('rndType')
        if rndType == "":
            raise RuntimeError("empty values")
        if rndType == "1":
            TUAB = False
        else:
            TUAB = True
        numQs = request.POST.get('numQs')
        if numQs == "":
            raise RuntimeError("empty values")
        subs = request.POST.getlist('subs[]')
        if subs == "":
            raise RuntimeError("empty values")
        scrammbleQs = request.POST.get('scrammbleQs')
        if scrammbleQs == "":
            raise RuntimeError("empty values")
        if not TUAB:
            questions = Question.objects.filter(comp__iexact=comp).filter(subject__in=subs).order_by('?')[:numQs]
            return render(request, 'questionset.html', {'questions': questions})
        elif TUAB:
            tt = int(numQs) * 2
            # vvvvvvvvv Old code vvvvvvvvv
            # questions = Question.objects.filter(comp__iexact=comp).filter(subject__in=subs).order_by('?')[:tt]

            # Generation of Toss-Ups
            questions = Question.objects.filter(comp__iexact=comp).filter(subject__in=subs).order_by('?')[:numQs]
            subsOfQuestions = {}
            for question in questions:
                qSub = question.subject
                subsOfQuestions[qSub] = (subsOfQuestions[qSub] + 1) if (subsOfQuestions[qSub] == qSub) else (subsOfQuestions[qSub] + 0);

            # Generation of Bonuses
            bonusQuestions = {}
            for key, value in subsOfQuestions.iteritems():
                bonusQuestions[key] = Question.objects.filter(comp__iexact=comp).filter(subject__in=key).order_by('?')[:value]
            return render(request, 'questionset.html', {'questions': questions, 'includeBonuses': TUAB})
    return render(request, 'generateset.html')

@login_required
def questionset(request):
    questions = Question.objects.all()
    return render(request, 'questionset.html', {'questions': questions})

@login_required
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        text = request.POST.get('upload')
        if text == "":
            raise RuntimeError("upload is empty!")
        parse.parse(text)
    return render(request, 'index.html')

@login_required
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

