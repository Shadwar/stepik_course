from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, related_name='question_likes')
    objects = QuestionManager()

    def get_absolute_url(self):
        return reverse('qa:question', kwargs={'id': self.id})


class Answer(models.Model):
    text = models.TextField(max_length=100)
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


