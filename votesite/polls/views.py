from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    #response = "Looking at question %s."
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNoteExist:
        raise Http404("Question does not exist.")
    return render(request,'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("Looking at resuls of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Looking at vote on question %s" % question_id)