from django.shortcuts import render

from .models import Question

# Create your views here.
def home(request):
    questions = Question.objects.all()
    #return HttpResponse("Welcome Home")
    return render(request, 'polls/home.html', {
        "questions": questions
    })

def vote(request, q_id):
    pass

def results(request, q_id):
    pass