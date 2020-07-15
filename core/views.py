from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Answer 
import datetime
from .forms import QuestionForm, AnswerForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_questions')
    return render(request, 'questions/home.html')

  
def list_questions(request):
    questions = request.user.questions.all()
    return render(request, 'questions/list_questions.html', {'questions': questions})

  
def show_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    form = QuestionForm()
    answers = question.answers.order_by('answered_on')
    return render(request, 'questions/show_question.html', {'question': question, 'pk': pk, 'form': form, 'answers': answers})

  
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to='list_questions')
    else:
        form = QuestionForm()

    return render(request, 'questions/add_question.html', {'form': form})