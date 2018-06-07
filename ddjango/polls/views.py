from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import *
import datetime


# Create your views here.

def index(request):
    poll = Poll.objects.all()
    return render(request, 'polls/index.html', {'polls': poll})


def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    return render(request, 'polls/detail.html', {'poll': poll})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    choices = Choice.objects.all()
    if request.method == "POST":
        try:
            choice = p.choice_set.get(pk=request.POST['vote'])
        except Exception, e:
            return render(request, 'polls/detail.html', {'message': "you didn't select vote",'choices':choices,'poll':p})
        choice.vote += 1
        choice.save()

        return render(request, 'polls/vote.html',{'choices':choices,'poll':p})


