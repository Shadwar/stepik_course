from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.urls import reverse

from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def error(request, *args, **kwargs):
    raise Http404


def new_questions(request):
    limit = 10
    page = 1
    try:
        page = int(request.GET.get('page', 1))
    except TypeError:
        page = 1

    paginator = Paginator(Question.objects.new(), limit)
    paginator.baseurl = reverse('qa:new_questions')
    questions = paginator.page(page)

    return render(request, 'qa/new_question_list.html', {
        'page': page,
        'questions': questions,
        'paginator': paginator
    })


def question(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'qa/question.html', {
        'question': question
    })


def popular_questions(request):
    limit = 10
    page = 1
    try:
        page = int(request.GET.get('page', 1))
    except TypeError:
        page = 1

    paginator = Paginator(Question.objects.popular(), limit)
    paginator.baseurl = reverse('qa:popular_questions')
    questions = paginator.page(page)
    print(paginator.page_range)

    return render(request, 'qa/popular_question_list.html', {
        'page': page,
        'questions': questions,
        'paginator': paginator
    })
