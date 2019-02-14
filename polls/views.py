from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.
def poll(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in q_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/poll.html')
    context = {
        'q_list': q_list,
    }
    return HttpResponse(template.render(context, request))
    # context = {}
    # context['hello'] = "here is poll"
    # return render(request, "polls/poll.html", context)


# template = loader.get_template('polls/poll.html')
# return HttpResponse(template.render(context, reuest))
def search_form(request):
    return render_to_response('polls/search.html')


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'you searched: ' + request.GET['q']
    else:
        message = 'you submitted a empty table'
    return HttpResponse(message)


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = 'you sent: ' + request.POST['q']
    return render(request, "polls/search.html", ctx)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("this question not found")
    # question = get_object_or_404(Question.object.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "please choice one.",
        })
    # selected_choice = question.choice_set.get(pk=request.POST['choice', None]) #set default choice=None
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def test(request, p):
    return HttpResponse("test path is: %s" % p)
