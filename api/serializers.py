from rest_framework import serializers
from core.models import Question, Answer
from users.models import User




class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    author_answer = serializers.ReadOnlyField(source="author_answer.username")
    question_id = serializers.IntegerField()
    class Meta:
        model = Answer
        fields = ['id', 'answer_response', 'answered_on', 'author_answer', 'question_id']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    author_question = serializers.ReadOnlyField(source="author_question.username")
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'title', 'ask_question', 'author_question', 'created_on', 'answers']





