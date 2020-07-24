from django.shortcuts import render, get_object_or_404
from users.models import User
from core.models import Question, Answer
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import generics, permissions, status
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import action


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_question=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format)
    })