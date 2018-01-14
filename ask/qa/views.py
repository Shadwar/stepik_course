from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.urls import reverse

from qa.models import Question

from qa.forms import AskForm, AnswerForm

from qa.models import Answer


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


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            new_question = Question(**form.cleaned_data)
            new_question.save()
            return HttpResponseRedirect(reverse('qa:question', kwargs={'id':new_question.id}))
    else:
        form = AskForm()
        return render(request, 'qa/question_new.html', {
            'form': form
        })


def question(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer(**form.cleaned_data)
            answer.save()
    question = get_object_or_404(Question, pk=id)
    form = AnswerForm()
    return render(request, 'qa/question.html', {
        'question': question,
        'form': form
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
