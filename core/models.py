from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    ask_question = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author_question = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="questions")
    favorited_by = models.ManyToManyField(to=User,
                                          related_name='favorite_questions')  
    def __str__(self):
        return f"{self.title} -  {self.author_question}"


class Answer(models.Model):
    answer_response = models.TextField()
    answered_on = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  related_name="answers")
    author_answer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="response")
    favorited_by = models.ManyToManyField(to=User,
                                          related_name='favorite_answers')
    def __str__(self):
        return f"{self.question} - {self.author_answer}"