# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import Q
# Create your models here.

class QuestionManager(models.Manager):
	def get_unanswered(self, user):
		q1 = Q(useranswer__user=user)
		qs = self.exclude(q1)
		return qs


class Question(models.Model):
	text = models.TextField()
	# active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	objects = QuestionManager()
	image = models.FileField(upload_to='questions',blank=True)

	def __str__(self):
		return self.text[:10]


class Answer(models.Model):
	question  = models.ForeignKey(Question)
	text      = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	image     = models.FileField(upload_to='answers',blank=True)

	def __str__(self): 
		return self.text[:10]



class UserAnswer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)  
	my_answer = models.ForeignKey(Answer, related_name='user_answer')
	my_points = models.IntegerField(default=-1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.my_answer.text[:10]




















