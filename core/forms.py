from django import forms
from django.forms import ModelForm, Textarea
from .models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'question_ask',
        ]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer_response',
            
        ]