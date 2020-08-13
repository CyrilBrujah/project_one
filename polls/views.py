from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #output = '; '.join([str(q) for q in latest_question_list])
    return HttpResponse(template.render(context, request))
    #return HttpResponse(output)


def bindex(request):
    """My test function for experiments"""
    import requests
    response = requests.get('https://ru.wikipedia.org/wiki/HTTP')
    return HttpResponse(response.content)


def detail(request, question_id):
    #template = loader.get_template('polls/detail.html')
    #context = {
    #    'question_id': question_id,
    #}
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
