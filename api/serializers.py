from rest_framework import serializers
from core.models import Question, Answer
from users.models import User





class QuestionSerializer(serializers.ModelSerializer):
    author_question = serializers.ReadOnlyField(source="author_question.username")
    class Meta:
        model = Question
        fields = ['id', 'title', 'ask_question', 'author_question', 'created_on']


class AnswerSerializer(serializers.ModelSerializer):
    author_answer = serializers.ReadOnlyField(source="author_answer.username")
    class Meta:
        model = Answer
        fields = ['id', 'answer_response', 'answered_on', 'author_answer', 'created_on', 'question']