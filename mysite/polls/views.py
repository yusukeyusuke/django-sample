from django.shortcuts import render_to_response,get_object_or_404,render
from django.http import HttpResponse
from polls.models import Poll
from django.http import Http404
import os

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #return HttpResponse(os.system("time /t >> d:\\home\\aa.txt"))
    return render(request, 'polls/index.html',
                              {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
