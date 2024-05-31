from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Choice

def home(request):
    questions = Question.objects.all()
    return render(request, 'polls/home.html', {"questions": questions})

def vote(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    if request.method == 'POST':
        try:
            choice_id = request.POST['choice']
            c = Choice.objects.get(id=choice_id)
            c.votes += 1
            c.save()
            return redirect('polls:results', q_id=q_id)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/question.html', {
                "question": question,
                "error_message": "Debes seleccionar una opción válida."
            })
    return render(request, 'polls/question.html', {"question": question})

def results(request, q_id):
    try:
        question = Question.objects.get(id=q_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    
    choices = question.choice_set.all()
    labels = [choice.choice_text for choice in choices]
    data = [choice.votes for choice in choices]

    return render(request, 'polls/results.html', {
        "question": question,
        "labels": labels,
        "data": data,
    })
