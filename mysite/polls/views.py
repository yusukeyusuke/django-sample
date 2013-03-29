from django.shortcuts import render_to_response,get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll,Choice
from django.http import Http404
from django.template import Context, loader
import os

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html',
#                               {'latest_poll_list': latest_poll_list})

# def detail(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html',{'poll':poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
