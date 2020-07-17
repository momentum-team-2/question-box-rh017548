from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Answer 
import datetime
from .forms import QuestionForm, AnswerForm
from django.views import View
from users.models import User


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
    form = AnswerForm()
    answers = question.answers.order_by('answered_on')
    return render(request, 'questions/show_question.html', {'question': question, 'pk': pk, 'form': form, 'answers': answers})

  
def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.instance
            question.author_question = request.user
            question.save()
            return redirect(to='list_questions')
    return render(request, 'questions/add_question.html', {'form': form})


def edit_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect(to='list_questions')
    else:
        form = QuestionForm(instance=question)

    return render(request, 'questions/edit_question.html', {'form': form, 'question': question})


def delete_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted.')
        return redirect(to='list_questions')
        
    return render(request, 'questions/delete_question.html', {'question': question})


def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.instance
            answer.author_answer = request.user
            answer.question =question
            
            answer.save()
            return redirect(to='show_question', pk=pk)
    return render(request, 'questions/add_answer.html', {'form': form, 'question': question,})