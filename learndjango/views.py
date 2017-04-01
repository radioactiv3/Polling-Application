from django.shortcuts import render
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import get_object_or_404 
from .models import Choice, Question



def index(request):
    latest_question_list =Question.objects.order_by('-pub_date')[:5]
    output =', '.join(q.question_text for q in latest_question_list)
    return HttpResponse(output)

    #Detail Function here

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'learndjango/detail.html', {'question': question})
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'learndjango/result.html',{'question':question})



def vote(request, question_id): 
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist): 
        return render(request,'learndjango/details.html',{
            'question':question,
            'error_message':"You did not select a valid choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect('learndjango:results',args=(question_id,))



	#return HttpResponse("You're voting on question %s." question_id)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = get_template('learndjango/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))